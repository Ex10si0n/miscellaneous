from django.shortcuts import render
from . import models
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

# Create your views here.
class PostListView(ListView):
    model = models.post
    template_name = 'posts.html'

class PostCreateView(CreateView):
    model = models.post
    template_name = 'create_post.html'
    fields = ['title', 'body']
