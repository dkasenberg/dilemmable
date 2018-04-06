from django.conf.urls import include, url


from . import views

urlpatterns = [
    url(r'^new$', views.new_dilemma, name='new'),
    url(r'^create$', views.create_dilemma, name='create'),
    url(r'^view/(?P<dilemma_id>[0-9]+)$', views.view_dilemma, name='view'),
]
