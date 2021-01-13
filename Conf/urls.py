from django.urls import path
from . import views

app_name = 'Conf'

urlpatterns = [
    path('view/<int:file_id>/', views.data, name = 'data'),
    path('view/', views.list, name = 'list'),
    path('edit/<int:file_id>/save_edit', views.save_edit, name='save_edit'),
    path('edit/<int:file_id>/', views.edit, name='edit'),
    path('edit/', views.list2, name = 'list2'),
    path('new/new_save/',views.new_save, name = 'new_save'),
    path('new/',views.new, name = 'new'),
]