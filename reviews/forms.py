from django import forms
from .models import ReviewPost

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewPost
        fields = ['title', 'content', 'image']

    # def clean_title(self, *args, **kwargs):
    #     instance = self.instance
    #     title = self.cleaned_data.get('title')
    #     qs = ReviewPost.objects.filter(title__iexact=title)
    #     if instance is not None:
    #         qs = qs.exclude(pk=instance.pk)
    #     if qs.exists():
    #         raise forms.ValidationError("This title has already been used. Please select another title.")
    #         return title
