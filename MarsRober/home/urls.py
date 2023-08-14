from django.contrib import admin
from django.urls import path
from home import views
from django.urls import include


urlpatterns = [
    path('',views.control, name='control'),
    path('run/', views.run_script, name='run_script'),
]


