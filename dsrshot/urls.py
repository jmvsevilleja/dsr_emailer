from django.urls import path

from . import views

app_name = 'dsrshot'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_screenshot', views.get_screenshot, name='get_screenshot')
]
