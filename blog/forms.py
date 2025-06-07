from django import forms
from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your comment', 'rows': 4}),
        }
