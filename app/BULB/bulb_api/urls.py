from django.conf.urls import url
from . import views

app_name = 'bulb_api'
urlpatterns = [
    url('', views.index, name='index'),
]