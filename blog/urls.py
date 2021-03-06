from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    # path('', views.index, name='index'),
    # path('', views.index),
    path('', views.IndexView.as_view(),name='index'),
    # path('<int:pk>/', views.detail,name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.results,name='results'),
    path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote,name='vote'),
]
