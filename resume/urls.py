from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_main_page, name='show_main_page'),
    path('/resume/', views.show_resume, name='show_resume'),
    path('/certificates/', views.show_certificates, name='show_certificates'),
]
