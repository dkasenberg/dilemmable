from django.conf.urls import include, url


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/', include('user.urls')),
    url(r'^dilemma/', include('dilemma.urls')),
]
