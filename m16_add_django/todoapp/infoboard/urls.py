from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name='losses'),
    path("sync/", views.sync_losses_list, name="lossessync"),
]