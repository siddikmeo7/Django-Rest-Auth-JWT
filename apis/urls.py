from .views import *
from django.urls import path

urlpatterns = [
    # Actor URLs
    path("actors/", ActorListAPIView.as_view(), name="actor_list"),
    path("actors/create/", ActorCreateAPIView.as_view(), name="actor_create"),
    path("actors/<int:pk>/delete/", ActorDestroyAPIView.as_view(), name="actor_delete"),
    path("actors/<int:pk>/", ActorRetrieveAPIView.as_view(), name="actor_detail"),
    path("actors/<int:pk>/update/", ActorRetrieveUpdateAPIView.as_view(), name="actor_update"),
    
    # Director URLs
    path("directors/", DirectorListAPIView.as_view(), name="director_list"),
    path("directors/create/", DirectorCreateAPIView.as_view(), name="director_create"),
    path("directors/<int:pk>/delete/", DirectorDestroyAPIView.as_view(), name="director_delete"),
    path("directors/<int:pk>/", DirectorRetrieveAPIView.as_view(), name="director_detail"),
    path("directors/<int:pk>/update/", DirectorRetrieveUpdateAPIView.as_view(), name="director_update"),
    
    # Genres URLs
    path("genres/", GenresListAPIView.as_view(), name="genres_list"),
    path("genres/create/", GenresCreateAPIView.as_view(), name="genres_create"),
    path("genres/<int:pk>/delete/", GenresDestroyAPIView.as_view(), name="genres_delete"),
    path("genres/<int:pk>/", GenresRetrieveAPIView.as_view(), name="genres_detail"),
    path("genres/<int:pk>/update/", GenresRetrieveUpdateAPIView.as_view(), name="genres_update"),
    
    # Movie URLs
    path("movies/", MovieListAPIView.as_view(), name="movie_list"),
    path("movies/create/", MovieCreateAPIView.as_view(), name="movie_create"),
    path("movies/<int:pk>/delete/", MovieDestroyAPIView.as_view(), name="movie_delete"),
    path("movies/<int:pk>/", MovieRetrieveAPIView.as_view(), name="movie_detail"),
    path("movies/<int:pk>/update/", MovieRetrieveUpdateAPIView.as_view(), name="movie_update"),
    
    # Reviewer URLs
    path("reviewers/", ReviewerListAPIView.as_view(), name="reviewer_list"),
    path("reviewers/create/", ReviewerCreateAPIView.as_view(), name="reviewer_create"),
    path("reviewers/<int:pk>/delete/", ReviewerDestroyAPIView.as_view(), name="reviewer_delete"),
    path("reviewers/<int:pk>/", ReviewerRetrieveAPIView.as_view(), name="reviewer_detail"),
    path("reviewers/<int:pk>/update/", ReviewerRetrieveUpdateAPIView.as_view(), name="reviewer_update"),
    
    # Movie Cast URLs
    path("movie-cast/", MovieCastListAPIView.as_view(), name="movie_cast_list"),
    path("movie-cast/create/", MovieCastCreateAPIView.as_view(), name="movie_cast_create"),
    path("movie-cast/<int:pk>/delete/", MovieCastDestroyAPIView.as_view(), name="movie_cast_delete"),
    path("movie-cast/<int:pk>/", MovieCastRetrieveAPIView.as_view(), name="movie_cast_detail"),
    path("movie-cast/<int:pk>/update/", MovieCastRetrieveUpdateAPIView.as_view(), name="movie_cast_update"),
    
    # Movie Genres URLs
    path("movie-genres/", MovieGenresListAPIView.as_view(), name="movie_genres_list"),
    path("movie-genres/create/", MovieGenresCreateAPIView.as_view(), name="movie_genres_create"),
    path("movie-genres/<int:pk>/delete/", MovieGenresDestroyAPIView.as_view(), name="movie_genres_delete"),
    path("movie-genres/<int:pk>/", MovieGenresRetrieveAPIView.as_view(), name="movie_genres_detail"),
    path("movie-genres/<int:pk>/update/", MovieGenresRetrieveUpdateAPIView.as_view(), name="movie_genres_update"),
    
    # Rating URLs
    path("ratings/", RatingListAPIView.as_view(), name="rating_list"),
    path("ratings/create/", RatingCreateAPIView.as_view(), name="rating_create"),
    path("ratings/<int:pk>/delete/", RatingDestroyAPIView.as_view(), name="rating_delete"),
    path("ratings/<int:pk>/", RatingRetrieveAPIView.as_view(), name="rating_detail"),
    path("ratings/<int:pk>/update/", RatingRetrieveUpdateAPIView.as_view(), name="rating_update"),
    
    # Movie Direction URLs
    path("movie-directions/", MovieDirectionListAPIView.as_view(), name="movie_direction_list"),
    path("movie-directions/create/", MovieDirectionCreateAPIView.as_view(), name="movie_direction_create"),
    path("movie-directions/<int:pk>/delete/", MovieDirectionDestroyAPIView.as_view(), name="movie_direction_delete"),
    path("movie-directions/<int:pk>/", MovieDirectionRetrieveAPIView.as_view(), name="movie_direction_detail"),
    path("movie-directions/<int:pk>/update/", MovieDirectionRetrieveUpdateAPIView.as_view(), name="movie_direction_update"),
]
