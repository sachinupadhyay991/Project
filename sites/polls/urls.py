from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('viewmore/<int:id>', views.viewmore, name='view')
]