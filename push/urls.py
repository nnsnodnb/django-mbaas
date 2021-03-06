# coding: utf-8

from django.conf.urls import url
from push import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^download_device_token$', views.download_device_token, name = 'download_device_token'),
    url(r'^sender', views.sender, name = 'sender'),
    url(r'^notification_list', views.notification_list, name = 'notification_list'),
    url(r'^notification_detail/(?P<notification_id>\d+$)', views.notification_detail, name = 'notification_detail'),
    url(r'^notification_modify$', views.notification_modify, name = 'notification_modify'),
    url(r'^settings', views.settings, name = 'settings'),
    url(r'^notification', views.notification, name = 'notification'),
    url(r'^(?P<username>\w+)/register$', views.device_token_register, name = 'device_token_register'),
    url(r'^delete/device_token/(?P<device_token_id>\d+)$', views.delete_device_token, name = 'delete_device_token'),
    url(r'^device_token/(?P<device_token_id>\d+)', views.detail_device_token, name = 'detail_device_token'),
    url(r'^delete_pem$', views.delete_pem, name = 'delete_pem'),
    url(r'^change_notification_status$', views.change_notification_status, name = 'change_notification_status'),
]
