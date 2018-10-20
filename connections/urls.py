from django.urls import path
from . import views

app_name = 'connections'  # for namespacing
urlpatterns = [
<<<<<<< HEAD
    # path('search/', views.search, name='search'),
    # path('results/', views.results, name='results'),
    # path('profile/', views.profile, name='profile'),
=======
    path('search/', views.search, name='search'),
    path('results/', views.results, name='results'),
    path('profile/', views.profile, name='profile'),
>>>>>>> 215a6ef77300000cedcfffea79a96bc0f0660fab
]
