from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Your email"}),
            "message": forms.Textarea(attrs={"placeholder": "Write your comment...", "rows": 4}),
        }
