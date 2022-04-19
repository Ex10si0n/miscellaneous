from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('message/new/', views.MessageCreateView.as_view(), name='new_message'),
    path('message/edit/<int:pk>', views.MessageUpdateView.as_view(), name='edit_message'),
    path('message/delete/<int:pk>', views.MessageDeleteView.as_view(), name='delete_message'),
]
