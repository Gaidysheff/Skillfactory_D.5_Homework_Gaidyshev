
from django import forms
from django.core.exceptions import ValidationError

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['author',
                  'categoryType',
                  'title',
                  'text',
                  'rating',
                ]

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("text")
        if description is not None and len(description) < 10:
            raise ValidationError({
                "text": "Сообщение не может быть менее 10 символов."
            })

        name = cleaned_data.get("title")
        if name == description:
            raise ValidationError(
                "Заголовок не должен быть идентичен тексту поста."
            )

        return cleaned_data

