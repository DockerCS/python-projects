from django import forms

# 评论
class CommentForm(forms.Form):
    comment = forms.CharField(label='', widget=forms.Textarea(attrs={'cols': '60', 'rows': '6'}))



