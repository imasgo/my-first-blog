from django.db import models
from django.utils import timezone
NOTETYPE=(
    (1, "Грамота"),
    (2, "Летопись")
)


class HistoryNote(models.Model):
    article_name = models.TextField(null=True)
    author = models.ForeignKey('auth.User', default='hello', on_delete=models.DO_NOTHING)
    note_type = models.SmallIntegerField(choices=NOTETYPE, default=1)
    author_before = models.CharField(max_length=100, null=True, blank=True)
    name_in_sources = models.CharField(max_length=250, null=True, blank=True)
    titles = models.TextField(null=True, blank=True)
    life_dates = models.CharField(max_length=100, null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    family_relationship = models.TextField(null=True, blank=True)
    others = models.TextField(null=True, blank=True)
    sources = models.TextField(null=True, blank=True)
    literature = models.TextField(null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return ' {} | {} '.format(self.article_name, self.name_in_sources)
