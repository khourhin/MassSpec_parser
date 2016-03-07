from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.CompareMSView.as_view(), name='compare_ms'),
    url(r'^register$', views.create_user, name='create_user'),
    url(r'^done/$', views.done, name='done'),
]
