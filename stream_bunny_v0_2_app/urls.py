from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_search),
    # path('get_movies', views.get_movies),
    path('search/<str:query>', views.search),
    path('get_movie/<str:movie_id>', views.get_movie),
    path('like/<int:movie_id>', views.like), 
    # path('unlike/<int:movie_id>', views.unlike), 
    path('search-like-div/<int:imdb_id>', views.search_like_div), 
    # search-like-div/${this.getAttribute("movie-id")}
]