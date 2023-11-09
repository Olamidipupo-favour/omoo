from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('register/', views.registration_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('otp/', views.otp_view, name='otp'),
    path('vote/', views.vote_page, name='vote'),
    path('admin/results/', views.admin_results_view, name='admin_results'),



    # Define more URL patterns as needed
]
