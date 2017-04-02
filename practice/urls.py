from django.conf.urls import url

from . import views

app_name = 'practice'
urlpatterns = [
    url(r'^$', views.jquery_view, name='jquery'),
]