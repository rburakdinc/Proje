from django.urls import path
from . import views

# 127.0.0.1:8000/movies
# 127.0.0.1:8000/movies/2
# 127.0.0.1:8000/movies/search

urlpatterns = [
    path('', views.index, name= 'hayvanlar'),
    path('<int:hayvan_id>', views.detail, name= 'detail'),
    path('search', views.search, name= 'search'),
]