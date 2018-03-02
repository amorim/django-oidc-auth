from django.conf.urls import url

import views

urlpatterns = [
    url(r'^login/$', views.login_begin, name='oidc-login'),
    url(r'^complete/$', views.login_complete, name='oidc-complete'),
]
