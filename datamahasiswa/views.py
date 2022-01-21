from dataclasses import field, fields
from pyexpat import model
from statistics import mode
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import TabelMahasiswa

class IndexMahasiswa(ListView):
    queryset = TabelMahasiswa.objects.all()
    
class TambahMahasiswa(CreateView):
    model = TabelMahasiswa
    fields = "__all__"
    success_url = reverse_lazy('mahasiswa:index')
    
class UpdateMahasiswa(UpdateView):
    model = TabelMahasiswa
    fields = '__all__'
    success_url = reverse_lazy('mahasiswa:index')
    
class DetailMahasiswa(DetailView):
    model = TabelMahasiswa
    
class HapusMahasiswa(DeleteView):
    model = TabelMahasiswa
    success_url = reverse_lazy('mahasiswa:index')