from django import forms


class BlogPostForm(forms.Form):
    title = forms.CharField(label="Title:")
    author = forms.CharField(label="Author:")
    body = forms.CharField(
        label="Post Body:",
        widget=forms.Textarea(attrs={'placeholder': 'Insert comment Here'}))


class BlogCommentForm(forms.Form):
    title = forms.CharField(label="Title:")
    rating = forms.IntegerField(label="Rating:", max_value=5, min_value=1)
    author = forms.CharField(label="Author:")
    body = forms.CharField(
        label="Comment Body:",
        widget=forms.Textarea(attrs={'placeholder': 'Insert comment Here'}))
