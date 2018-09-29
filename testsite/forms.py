from django import forms

from .models import HistoryNote

class HistoryNoteForm(forms.ModelForm):
    article_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название статьи'}))
    author_before = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Старый автор', }))
    name_in_sources = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя в источниках', 'id':'keyboard'}), required=False)
    note_type = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Папка'}))
    titles = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Титулы'}), required=False)
    life_dates = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Даты жизни'}), required=False)
    biography = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Биография'}), required=False)
    family_relationship = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Семейные отношения'}), required=False)
    others = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Другое'}), required=False)
    sources = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Источники'}), required=False)
    literature = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Литература'}), required=False)

    class Meta:
        model = HistoryNote
        fields =['article_name','name_in_sources','author_before','note_type',
                'titles','biography','life_dates','family_relationship',
                'sources','literature','others']
