from django.shortcuts import render,redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from blog.models import Comment, Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm


# Create your views here.
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        
    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 3:
            raise ValidationError('password')
        return password
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class RegisterUser(CreateView):
    form_class = UserRegistrationForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')

class LoginUser(LoginView):
    template_name = 'blog/login.html'
    def get_success_url(self):
        return reverse_lazy('profile')

def home_view(request):
    return render(request,'blog/index.html')

def profile_view(request):
    if request.method == 'GET':
        user = request.user
        context = {"user": user}
        return render(request,'blog/profile.html',context)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    
    context = {
        'form': form,
        'user': request.user
    }
    return render(request, 'blog/profile.html', context)

class PostCreateView(CreateView):
    model = Post
    fields = ['title','content']
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('post-create')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class PostListView(ListView):
    model = Post
    template_name = 'blog/posts_list.html'
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all().order_by('-created_at')
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            return redirect('post-detail', pk=self.object.pk)
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_update.html'

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'  
    success_url = reverse_lazy('posts')      

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your comment here...',
                'rows': 4,
            }),
        }
        labels = {
            'content': '',
        }

    def clean_content(self):
        content = self.cleaned_data.get('content', '').strip()
        if not content:
            raise ValidationError("Comment cannot be empty.")
        if len(content) < 3:
            raise ValidationError("Comment is too short (minimum 3 characters).")
        if len(content) > 500:
            raise ValidationError("Comment is too long (maximum 500 characters).")
        forbidden_words = ['badword1', 'badword2', 'offensive']  
        for word in forbidden_words:
            if word.lower() in content.lower():
                raise ValidationError("Your comment contains inappropriate language.")

        return content
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.post.pk})

def landing_posts(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/landing_posts.html', {'posts': posts})