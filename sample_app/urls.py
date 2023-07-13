from django.urls import path
from .import views

urlpatterns = [
    path('',views.list_content,name='list_content'),
    path('add/',views.add_content,name='add_content'),
    path('edit/<int:pk>/',views.edit_content,name='edit_content'),
    path('delete/<int:pk>/',views.delete_content,name='delete_content'),
]