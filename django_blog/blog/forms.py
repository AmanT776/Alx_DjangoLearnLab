from django.core.exceptions import ValidationError
from .models import Comment
from django import forms
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