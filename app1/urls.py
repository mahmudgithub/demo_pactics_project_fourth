#from django.conf.urls import url
#from django.contrib import admin

#from boards import views

#urlpatterns = [
   # url(r'^$', views.home, name='home'),
   # url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
   # url(r'^admin/', admin.site.urls),
#]


from django.urls import path
from .views import sos, bos

urlpatterns = [
path('',sos.as_view(),name='home1'),
path('bos/',bos.as_view(),name='home2'),
]