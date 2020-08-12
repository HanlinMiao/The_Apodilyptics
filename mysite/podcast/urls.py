from django.urls import path
from . import views
from .views import PodListView, PodDetailView, test

urlpatterns =[
	path('', PodListView.as_view(), name ='podcast-home'),
	path('podcast/<int:pk>/', PodDetailView.as_view(), name ='podcast-detail'),
	path('test/', views.test, name ='test'),
]