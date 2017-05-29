"""HyrComputerVisionServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from HyrComputerVision import views as hyr_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login$', hyr_views.login, name='login'),
    url(r'^register$', hyr_views.register, name='register'),
    url(r'^myaccount_server$', hyr_views.myaccount_server, name='myaccount_server'),
    url(r'^buy_product$', hyr_views.buy_product, name='buy_product'),
    url(r'^emotion$', hyr_views.emotion, name='emotion'),
    url(r'^emotion_file$', hyr_views.emotion_file, name='emotion_file'),
    url(r'^face$', hyr_views.face, name='face'),
    url(r'^face_file$', hyr_views.face_file, name='face_file'),
    url(r'^carPlate$', hyr_views.carPlate, name='carPlate'),
    url(r'^carPlate_file$', hyr_views.carPlate_file, name='carPlate_file'),
    url(r'^object$', hyr_views.object, name='object'),
    url(r'^object_file$', hyr_views.object_file, name='object_file'),

    url(r'^app.html$', hyr_views.app_html, name='app'),
    url(r'^carPlate.html$', hyr_views.carPlate_html, name='carPlate'),
    url(r'^document.html$', hyr_views.document_html, name='document'),
    url(r'^emotion.html$', hyr_views.emotion_html, name='emotion'),
    url(r'^face.html$', hyr_views.face_html, name='face'),
    url(r'^index.html$', hyr_views.index_html, name='index'),
    url(r'^login.html$', hyr_views.login_html, name='login'),
    url(r'^myAccount.html$', hyr_views.myAccount_html, name='myAccount'),
    url(r'^object.html$', hyr_views.object_html, name='object'),
    url(r'^price.html$', hyr_views.price_html, name='price'),
    url(r'^registered.html$', hyr_views.registered_html, name='registered'),

]
