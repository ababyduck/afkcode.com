from django import forms


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            'id': 'comment-form-author',
            'class': 'form-control',
            'placeholder': 'Your name'
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            'id': 'comment-form-body',
            'class': 'form-control',
            'placeholder': 'Leave a comment!',
            'rows': 4
        })
    )
