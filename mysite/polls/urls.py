from django.urls import path
from . import views
urlpatterns =[
	path('polls', views.IndexView.as_view() , name ='polls-home'),
	path('polls/<int:pk>/', views.DetailView.as_view(), name='polls-detail'),
    # ex: /polls/5/results/
    path('polls/<int:pk>/results/', views.ResultsView.as_view(), name='polls-results'),
    # ex: /polls/5/vote/
    path('polls/<int:question_id>/vote/', views.vote, name='polls-vote'),
]