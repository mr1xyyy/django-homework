# news/forms.py
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from .models import News

class ArticleForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Maqolaning sarlavhasi",
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "E'lon maqolasi",
            }),
            "date": DateTimeInput(attrs={ 
                'class': 'form-control',
                'placeholder': "nashr etilgan sana",
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Maqola yozuvi',
            })
        }