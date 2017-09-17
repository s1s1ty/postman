from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^send-product/add/$', views.send_product_add, name='add_send_product'),
    url(r'^qr-code/$', views.view_qr_code, name='qr_code'),
]
