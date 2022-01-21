from django.urls import path

from . import views

app_name = 'mahasiswa'

urlpatterns = [
    path('tambah/', views.TambahMahasiswa.as_view(), name='tambah'),
    path('edit/<pk>/', views.UpdateMahasiswa.as_view(), name='ubah'),
    path('detail/<pk>/', views.DetailMahasiswa.as_view(), name='detail'),
    path('hapus/<pk>/', views.HapusMahasiswa.as_view(), name='hapus'),
    path('', views.IndexMahasiswa.as_view(), name='index'),
]
