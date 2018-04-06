from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

TOKEN_STR = r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$'

urlpatterns = [
    # TODO: fix dashboard view
    url(r'^logout/$', views.user_logout, name='logout'),

    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),

    url(r'^signup/$', views.signup, name='signup'),

    url(r'^login/$', auth_views.login, name='login',
        kwargs={'template_name': 'user/login.html'}),

    url(r'^password_change/$', auth_views.password_change,
        name='user/change_password', kwargs={
            'template_name': 'user/password_change_form.html'}),
    url(r'^password_change/done/$', auth_views.password_change_done,
        name='password_change_done', kwargs={
            'template_name': 'user/password_change_done.html'}),

    url(r'^password_reset/done/$', views.password_reset_save, name = 'password_reset_done'),
    url(r'^password_reset/$', views.password_reset_submit, name = 'password_reset'),
    # url(r'^password_reset/$', auth_views.password_reset,
    #     name='password_reset',
    #     kwargs={'template_name': 'user/password_reset_form.html'}),
    # url(r'^password_reset/done/$', auth_views.password_reset_done,
    #     name='password_reset_done',
    #     kwargs={'template_name': 'user/password_reset_done.html'}),

    url(TOKEN_STR, auth_views.password_reset_confirm,
        name='password_reset_confirm',
        kwargs={'template_name': 'user/password_reset_confirm.html'}),

    url(r'^reset/done/$', auth_views.password_reset_complete,
        name='password_reset_complete',
        kwargs={'template_name': 'user/password_reset_complete.html'}),

    # url(r'^settings/$', views.settings, name='user_settings'),
    # url(r'^superuser/$', views.superuser, name='superuser'),
    # Todo: user profile
]
