from django.shortcuts import render
from .models import HistoryNote

def post_list(request):
	historynotes = HistoryNote.objects.order_by('name_in_sources')
	return render(request, 'testsite/post_list.html', {'historynotes': historynotes})
