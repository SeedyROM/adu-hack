from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login', views.login_user, name='login'),
    path('logout', views.log_out, name='logout'),
    path('register_owner', views.register_property_owner_user, name='register_property_owner_user'),
    path('register_contractor', views.register_contractor_user, name='register_contractor_user'),
    path('profile', views.profile, name='profile'),
    path('smithjones', views.smithjones, name='smithjones'),
]
