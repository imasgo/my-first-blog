from django.shortcuts import render, get_object_or_404, redirect
from .models import HistoryNote
from .forms import HistoryNoteForm
from django.views.generic.list import ListView

# coding=<utf-8>


def post_list(request):
    historynotes = HistoryNote.objects.order_by('name_in_sources')
    return render(request, 'post_list.html', {'historynotes': historynotes})


def index(request):
    return render(request, 'index.html')


def gramota(request):
    gramotas = HistoryNote.objects.filter(note_type=1)
    return render(request, 'gramota.html', {'gramotas': gramotas})

# class Gramota(ListView):
# 	template_name = 'gramota.html'
# 	model = HistoryNote
#
# 	def get_queryset(self):
# 		return HistoryNote.objects.all()

def show_gramota(request, pk):
    historynote = get_object_or_404(HistoryNote, pk=pk)
    return render(request, 'show_gramota.html', {'historynote': historynote})


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
    return render(request, 'update_gramota.html', {'form': form})


def all(request):
    letopises = HistoryNote.objects.all()
    return render(request, 'all_historynotes.html', {'letopises': letopises})


def show_note(request, pk):
    historynote = get_object_or_404(HistoryNote, pk=pk)
    return render(request, 'show_note.html', {'historynote': historynote})


def add_note(request):
    form = HistoryNoteForm()
    if request.method == "POST":
        form = HistoryNoteForm(request.POST)
        if form.is_valid():
            print("all is ok")
            historynote = form.save(commit=False)
            historynote.author = request.user
            historynote.save()
            return redirect('show_note', pk=historynote.pk)
        else:
            form = HistoryNoteForm()
    return render(request, 'add_note.html', {'form': form})


def one(request):
    letopises_one = HistoryNote.objects.filter(note_type='1112-1122')
    return render(request, '1112-1122.html', {'letopises_one': letopises_one})


def eightfivetwo(request):
    letopises_eight = HistoryNote.objects.filter(note_type__contains='852-963')
    return render(request, '852-963.html', {'letopises_eight': letopises_eight})


def twelve(request):
    letopises_XII = HistoryNote.objects.filter(note_type__contains='XII век')
    return render(request, 'XII.html', {'letopises_XII': letopises_XII})


def jews(request):
    letopises_jews = HistoryNote.objects.filter(note_type__contains='Еврейско-хазарская переписка Х века')
    return render(request, 'jews.html', {'letopises_jews': letopises_jews})


def cambridge(request):
    letopises_cambridge = HistoryNote.objects.filter(note_type__contains='Киевское письмо и Кембриджский документ')
    return render(request, 'cambridge.html', {'letopises_cambridge': letopises_cambridge})


def novgorod(request):
    letopises_novgorod = HistoryNote.objects.filter(note_type__contains='Новгород')
    return render(request, 'novgorod.html', {'letopises_novgorod': letopises_novgorod})


def saga(request):
    letopises_saga = HistoryNote.objects.filter(note_type__contains='Сага об Олаве Трюгвассоне')
    return render(request, 'saga.html', {'letopises_saga': letopises_saga})


def sophia(request):
    letopises_sophia = HistoryNote.objects.filter(note_type__contains='София Киевская')
    return render(request, 'sophia.html', {'letopises_sophia': letopises_sophia})


def symbols_panel(request):
    return render(request, 'symbols_panel.html')
