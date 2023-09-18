from django.shortcuts import render
from .models import Movie, Cast, Review
from rest_framework import generics
from .serializers import MovieSerializer, CastSerializer, ReviewSerializer
from rest_framework.filters import SearchFilter, OrderingFilter 
from rest_framework.permissions import AllowAny


# Create your views here.


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['media_type']


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CastList(generics.ListCreateAPIView):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer


class CastDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class MovieCastList(generics.ListAPIView):
    serializer_class = CastSerializer

    def get_queryset(self):
        movie_id = self.kwargs['pk']

        return Cast.objects.filter(movie__id=movie_id)
    
class MovieReviewsList(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        movie_id = self.kwargs['pk']

        return Review.objects.filter(movie__id=movie_id)
    

class MovieTypeSearch(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        movie_type = self.kwargs['movie_type']

        return Movie.objects.filter(media_type__iexact=movie_type)
    

