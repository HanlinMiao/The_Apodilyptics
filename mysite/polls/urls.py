from django.urls import path
from . import views
urlpatterns =[
	path('polls', views.index , name ='polls-home'),
	path('polls/<int:question_id>/', views.detail, name='polls-detail'),
    # ex: /polls/5/results/
    path('polls/<int:question_id>/results/', views.results, name='polls-results'),
    # ex: /polls/5/vote/
    path('polls/<int:question_id>/vote/', views.vote, name='polls-vote'),
]