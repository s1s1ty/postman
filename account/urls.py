from django.conf.urls import url, include

from account import views

urlpatterns = [
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
]
