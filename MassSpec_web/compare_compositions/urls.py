from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.compare_ms, name='compare_ms'),
]
