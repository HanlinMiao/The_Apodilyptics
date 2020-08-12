from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import podcast
# Create your views here.
def home(request):
    context = {
        'podcasts': podcast.objects.all()
    }
    return render(request, 'podcast/home.html', context)
def test(request):
	return render(request, 'podcast/test.html')
	
class PodListView(ListView):     #<app>/<model>_<viewtype>.html
	model = podcast
	template_name = 'podcast/home.html'
	context_object_name = 'podcasts'
	paginate_by = 5
	ordering = ['-date_posted']

class PodDetailView(DetailView):
	model = podcast