from django.shortcuts import render
from .models import HistoryNote
from django.views.generic.list import ListView


def post_list(request):
	historynotes = HistoryNote.objects.order_by('name_in_sources')
	return render(request, 'testsite/post_list.html', {'historynotes': historynotes})

def index(request):
	return render(request, 'testsite/index.html')

def gramota(request):
	historynotes = HistoryNote.objects.order_by('name_in_sources')
	return render(request, 'testsite/gramota.html', {'historynotes': historynotes})

# class Gramota(ListView):
# 	template_name = 'gramota.html'
# 	model = HistoryNote
#
# 	def get_queryset(self):
# 		return HistoryNote.objects.all()