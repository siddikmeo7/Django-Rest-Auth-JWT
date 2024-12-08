from rest_framework.serializers import ModelSerializer
from .models import *

class Actorserial(ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"
        read_only_fields = ("is_deleted","deleted_at")
        
class DirectorrSerial(ModelSerializer):
    class Meta:
        model =  Director
        fields = "__all__"
        
        
        
class ReviewerSerial(ModelSerializer):
    class Meta:
        model =  Reviewer
        fields = "__all__"
        
class RatingSerial(ModelSerializer):
    class Meta:
        model =  Rating
        fields = "__all__"
        
        
class MovieSerial(ModelSerializer):
    class Meta:
        model =  Movie
        fields = "__all__"
        

class Movie_castSerial(ModelSerializer):
    class Meta:
        model =  MovieCast
        fields = "__all__"

class Movie_genresSerial(ModelSerializer):
    class Meta:
        model =  MovieGenre
        fields = "__all__"

class Movie_directionSerial(ModelSerializer):
    class Meta:
        model =  MovieDirection
        fields = "__all__"
        
class GenresSerial(ModelSerializer):
    class Meta:
        model =  Genre
        fields = "__all__"    