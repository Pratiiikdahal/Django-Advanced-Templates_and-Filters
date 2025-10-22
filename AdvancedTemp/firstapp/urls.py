from django.contrib import admin
from django.urls import path,include
from firstapp import views
from firstapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('forms/',views.formIndex,name='form'),
    path('business/',views.business,name='business'),
    path('info/',views.info,name='info'),
    path('portfolio/',views.portfolio,name='portfolio'),
]