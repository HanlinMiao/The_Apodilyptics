from django.urls import path
from . import views
from .views import PodListView, PodDetailView, test, resume_hanlin, choice

urlpatterns =[
	path('', PodListView.as_view(), name ='podcast-home'),
	path('gallery/', views.gallery, name ='podcast-gallery'),
	path('resume/', views.choice, name = 'choice'),
	path('resume/hanlin/', views.resume_hanlin, name = 'resume-hanlin'),
	path('podcast/<int:pk>/', PodDetailView.as_view(), name ='podcast-detail'),
	path('podcast/<int:pk>/comment/', views.add_comment_to_podcast, name='add_comment_to_podcast'),
	path('test/', views.test, name ='test'),
]