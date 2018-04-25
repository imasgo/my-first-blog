from django import forms

from .models import HistoryNote

class HistoryNoteForm(forms.ModelForm):
    article_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название статьи'}))
    author_before = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Старый автор'}))
    name_in_sources = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя в источниках'}))
    titles = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Титулы'}))
    life_dates = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Даты жизни'}))
    biography = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','rows':'3', 'placeholder': 'Биография'}))
    family_relationship = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Семейные отношения'}))
    others = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Другое'}))
    sources = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Источники'}))
    literature = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Литература'}))

    class Meta:
        model = HistoryNote
        fields=('article_name','name_in_sources','author_before',
                'titles','biography','life_dates','family_relationship',
                'sources','literature','others')
