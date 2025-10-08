from django.shortcuts import render,redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import CreateView,ListView,DetailView
from blog.models import Post
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
    template_name = 'blog/create_blog.html'
    success_url = reverse_lazy('post-create')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class PostListView(ListView):
    model = Post
    template_name = 'blog/posts.html'
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'