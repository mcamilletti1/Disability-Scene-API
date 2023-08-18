from rest_framework import serializers
from . models import *

class CastSerializer(serializers.HyperlinkedModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(
        queryset = Movie.objects.all(),
        write_only=True
    )

    class Meta:
        model = Cast
        fields = ('id', 'movie', 'name', 'credits', 'title', 'character_name', 'img')


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    cast_members = CastSerializer(
        many=True,
        read_only=True
    )

    movie_url = serializers.ModelSerializer.serializer_url_field(
        view_name='movie_detail'
    )

    class Meta:
        model = Movie
        fields = ('id', 'movie_url', 'title', 'media_type', 'year', 'genre', 'duration', 'disabilities', 'cast_members', 'themes', 'img', 'description')


class ReviewSerializer(serializers.HyperlinkedModelSerializer):

    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())

    class Meta:
        model = Review
        fields = ('id', 'movie', 'title', 'reviewer_name', 'review_text', 'date', 'casting_score', 'character_score', 'originality_score', 'accuracy_score')

    def create(self, validated_data):
        return Review.objects.create(**validated_data)