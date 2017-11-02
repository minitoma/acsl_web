from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^gallerie/$',views.gallerie_list, name='gallerie_list'),
    url(r'^gallerie/(?P<pk>\d+)/$', views.photo_detail, name='photo_detail'),
]
