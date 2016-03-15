from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.compare_ms, name='compare_ms'),
    url(r'^register$', views.create_user, name='create_user'),
    url(r'^done$', views.done, name='done'),
]
