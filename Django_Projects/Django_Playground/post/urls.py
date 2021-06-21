from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='posts'),
    path('create/', views.PostCreateView.as_view(), name='create_post'),
]