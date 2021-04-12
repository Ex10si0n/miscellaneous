from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('post/new/', views.BlogCreateView.as_view(), name='new_post'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='edit_post'),
    path('post/<int:pk>/del/', views.BlogDeleteView.as_view(), name='delete_post'),
]