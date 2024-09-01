from django.urls import path
from message_app import views

urlpatterns = [
    path('',views.home),
    path('create',views.create),
    path('output',views.output),
    path('delete/<rid>',views.delete),
    path('edit/<rid>',views.edit),
]
