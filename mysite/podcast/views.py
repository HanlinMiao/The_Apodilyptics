from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import podcast
from .forms import CommentForm
# Create your views here.
def home(request):
    context = {
        'podcasts': podcast.objects.all()
    }
    return render(request, 'podcast/home.html', context)
def test(request):
	return render(request, 'podcast/test.html')
def choice(request):
	return render(request, 'podcast/choice.html')
def resume_hanlin(request):
	return render(request, 'podcast/resume_hanlin.html')
def gallery(request):
	return render(request, 'podcast/gallery.html')


def add_comment_to_podcast(request, pk):
	Podcast = get_object_or_404(podcast, pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.podcast = Podcast
			comment.save()
			return redirect('podcast-detail', pk = Podcast.pk)
	else:
		form = CommentForm()
	return render(request, 'podcast/add_comment_to_podcast.html', {'form':form})
	
class PodListView(ListView):     #<app>/<model>_<viewtype>.html
	model = podcast
	template_name = 'podcast/home.html'
	context_object_name = 'podcasts'
	paginate_by = 5
	ordering = ['-date_posted']

class PodDetailView(DetailView):
	model = podcast
