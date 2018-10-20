from django.urls import path
from . import views

app_name = 'connections'
urlpatterns = [
    path('search/', views.mock_search, name='search'),
    # path('results/', views.results, name='results'),
    # path('profile/', views.profile, name='profile'),
]
