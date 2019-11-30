
from django.db import ModelForm
from .models import Article


class article_model_form(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
              'title',
              'content',
              'active'
        ]
