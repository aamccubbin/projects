from django.conf.urls import patterns,  url
from app1.views import inicio,alumno_lista

urlpatterns = patterns('',

    url(r'^inicio/$', inicio),
    url(r'^alumno_lista/$', alumno_lista),
)
