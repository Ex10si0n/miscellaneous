from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import models


# Create your views here.
class HomePageView(ListView):
    model = models.Message
    template_name = 'home.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'home'
        return context

    def get_queryset(self):
        return models.Message.objects.order_by('-date')

class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Message
    fields = ['title', 'body']
    template_name = 'edit_message.html'

class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Message
    template_name = 'delete_message.html'
    success_url = reverse_lazy('home')

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = models.Message
    template_name = 'new_message.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'new_message'
        return context
