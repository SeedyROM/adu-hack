from django.urls import path
from . import views

app_name = 'connections'
urlpatterns = [
    path('search/', views.search, name='search'),
    path('searchCont/', views.searchTwo, name='searchTwo'),
    # path('results/', views.results, name='results'),
    # path('profile/', views.profile, name='profile'),
]
