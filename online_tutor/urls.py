"""online_tutor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from online_tutor import settings
from tutor_app import user_urls, admin_urls, student_urls, tutour_urls, parent_urls
from tutor_app.views import IndexView, RegisterView,RegisterView1,RegisterView2,LoginViews

urlpatterns = [
    path('', IndexView.as_view()),
    path('register', RegisterView.as_view()),
    path('register1',RegisterView1.as_view()),
    path('register2',RegisterView2.as_view()),
    path('login', LoginViews.as_view()),
    path('user/', user_urls.urls()),
    path('admin/',admin_urls.urls()),
    path('student/', student_urls.urls()),
    path('tutor/', tutour_urls.urls()),
    path('parent/',parent_urls.urls()),




]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
