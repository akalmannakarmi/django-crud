from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from . import models,forms

class CreateInfo(CreateView):
    context_object_name = "info"
    model = models.Info
    form_class = forms.InfoForm
    template_name = "createInfo.html"
    success_url = reverse_lazy("crud:infos")

class Infos(ListView):
    allow_empty = True
    context_object_name = "infos"
    model = models.Info
    template_name = "infos.html"

class Info(DetailView):
    context_object_name = "info"
    model = models.Info
    template_name = "info.html"

class EditInfo(UpdateView):
    context_object_name = "info"
    model = models.Info
    form_class = forms.InfoForm
    template_name = "updateInfo.html"
    success_url = reverse_lazy("crud:infos")

class DeleteInfo(DeleteView):
    context_object_name = "info"
    model = models.Info
    template_name = "deleteInfo.html"
    success_url = reverse_lazy("crud:infos")
