"""tcc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

import apptcc.views.bacia_hidrografica as bacia_hidrografica
import apptcc.views.rio as rio
import apptcc.views.ponto as ponto
import apptcc.views.home as home
import apptcc.views.substancia as substancia
import apptcc.views.coleta as coleta
import apptcc.views.entorno as entorno
import apptcc.views.caso as caso


urlpatterns = [
    
    url(r'^$', home.home),
    url(r'^bacia-hidrografica/$', bacia_hidrografica.listar),
    url(r'^bacia-hidrografica/add/$', bacia_hidrografica.add),
    url(r'^bacia-hidrografica/edit/(?P<bh_id>\d+)/$', bacia_hidrografica.edit),
    url(r'^bacia-hidrografica/delete/(?P<bh_id>\d+)$', bacia_hidrografica.delete),

    url(r'^rio/$', rio.listar),
    url(r'^rio/add/$', rio.add),
    url(r'^rio/edit/(?P<rio_id>\d+)/$', rio.edit),
    url(r'^rio/delete/(?P<rio_id>\d+)/$', rio.delete),

    url(r'^ponto/$', ponto.listar),
    url(r'^ponto/add/$', ponto.add),
    url(r'^ponto/edit/(?P<ponto_id>\d+)/$', ponto.edit),
    url(r'^ponto/delete/(?P<ponto_id>\d+)/$', ponto.delete),

    url(r'^substancia/$', substancia.listar),

    url(r'^coleta/$', coleta.listar),
    url(r'^coleta/add/$', coleta.add),    
    url(r'^coleta/delete/(?P<coleta_id>\d+)/$', coleta.delete),

    url(r'^entorno/$', entorno.listar),
    url(r'^entorno/add/$', entorno.add),
    url(r'^entorno/edit/(?P<entorno_id>\d+)/$', entorno.edit),
    url(r'^entorno/delete/(?P<entorno_id>\d+)/$', entorno.delete),

    url(r'^caso/$', caso.listar),
    url(r'^caso/add/$', caso.add),
    url(r'^caso/edit/(?P<caso_id>\d+)/$', caso.edit),
    url(r'^caso/delete/(?P<caso_id>\d+)/$', caso.delete),
    url(r'^caso/pesquisar/$', caso.pesquisar),
    url(r'^caso/utilizar-solucao/(?P<caso_id>\d+)/(?P<monitoramento_id>\d+)/$', caso.utilizar_solucao),

]
