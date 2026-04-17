from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Alumno

from django.urls import reverse 
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


#------------------------------------- ALTAS -------------------------------------
class CrearAlumno(LoginRequiredMixin, SuccessMessageMixin, CreateView):  
    model = Alumno
    form = Alumno
    fields = "__all__"
    success_message = "Alumno AGREGADO con ÉXITO!!"

    def get_success_url(self):
        return reverse('listar')
    
#------------------------------------- BAJAS -------------------------------------
class EliminarAlumno(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Alumno
    form = Alumno
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Alumno ELIMINADO correctamente!!!'
        messages.success(self.request, success_message)
        return reverse('listar')
    
#------------------------------------- CAMBIOS -------------------------------------
class ActualizarAlumno(LoginRequiredMixin, SuccessMessageMixin, UpdateView):  
    model = Alumno
    form = Alumno
    fields = "__all__"
    success_message = "Alumno MODIFICADO con ÉXITO!!"

    def get_success_url(self):
        return reverse('listar')
    
#------------------------------------- CONSULTAS -------------------------------------
class DetalleAlumno(LoginRequiredMixin, DetailView):  
    model = Alumno
   
class ListarAlumnos(LoginRequiredMixin, ListView):
    model = Alumno

#------------------------------------- REGISTRO -------------------------------------
class RegistroUsuario(CreateView):
    form_class = UserCreationForm
    template_name = 'alumnos/login.html'
    
    def form_valid(self, form):
        form.save()
        return redirect('login')

    def form_invalid(self, form):
        return render(self.request, self.template_name, {
            'form': form,
            'mostrar_registro': True 
        })