from django.shortcuts import render, get_object_or_404, redirect
from .models import HistoryNote
from .forms import HistoryNoteForm
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

def show_gramota(request, pk):
    historynote = get_object_or_404(HistoryNote, pk=pk)
    return render(request, 'testsite/show_gramota.html', {'historynote': historynote})


def update_gramota(request, pk):
    historynote = get_object_or_404(HistoryNote, pk=pk)
    if request.method == "POST":
        form = HistoryNoteForm(request.POST, instance=historynote)
        if form.is_valid():
            historynote = form.save(commit=False)
            historynote.author = request.user
            historynote.save()
            return redirect('show_gramota', pk=historynote.pk)
    else:
        form = HistoryNoteForm(instance=historynote)
    return render(request, 'testsite/update_gramota.html', {'form': form})

def symbols_panel(request):
    return render(request, 'testsite/symbols_panel.html')
