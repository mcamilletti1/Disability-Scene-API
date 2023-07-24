from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieList.as_view(), name='movie_list'),
    path('cast', views.CastList.as_view(), name='cast_list'),
    path('reviews', views.ReviewList.as_view(), name='review_list'),
    path('movies', views.MovieList.as_view(), name='movie_list'),
    path('movies/<int:pk>', views.MovieDetail.as_view(), name='movie_detail'),
    path('cast/<int:pk>', views.CastDetail.as_view(), name='cast_detail'),
    path('reviews/<int:pk>', views.ReviewDetail.as_view(), name='review_detail'),
    path('movies/<int:pk>/cast/', views.MovieCastList.as_view(), name='movie-cast-list'),
    path('movies/<int:pk>/reviews/', views.MovieReviewsList.as_view(), name='movie-reviews-list'),
    path('movies/search/type/<str:movie_type>/', views.MovieTypeSearch.as_view(), name='movie-type-search'),
]