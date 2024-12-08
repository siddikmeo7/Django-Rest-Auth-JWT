from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import *
from .serialaizes import *


# Actor Views
class ActorListAPIView(generics.ListAPIView):
    queryset = Actor.objects.filter(is_deleted=False).order_by("-id")
    serializer_class = Actorserial

    @action(detail=True, methods=["POST"])
    def restore(self, request, pk=None):
        actor = Actor.objects.filter(id=pk).first()
        if actor and actor.is_deleted:
            actor.restore()
            return Response("Object restored", status=status.HTTP_200_OK)

    @action(detail=True, methods=["DELETE"])
    def hard_delete(self, request, pk=None):
        try:
            actor = Actor.objects.get(pk=pk)
            actor.delete()
            return Response({"message": "Actor deleted permanently."}, status=status.HTTP_204_NO_CONTENT)
        except Actor.DoesNotExist:
            return Response({"error": "Actor not found."}, status=status.HTTP_404_NOT_FOUND)


class ActorCreateAPIView(generics.CreateAPIView):
    serializer_class = Actorserial


class ActorRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = Actorserial


class ActorRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Actor.objects.all()
    serializer_class = Actorserial


class ActorDestroyAPIView(generics.DestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = Actorserial


# Director Views
class DirectorListAPIView(generics.ListAPIView):
    queryset = Director.objects.all().order_by("-id")
    serializer_class = DirectorrSerial


class DirectorCreateAPIView(generics.CreateAPIView):
    serializer_class = DirectorrSerial


class DirectorRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorrSerial


class DirectorRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorrSerial


class DirectorDestroyAPIView(generics.DestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorrSerial


# Genres Views
class GenresListAPIView(generics.ListAPIView):
    queryset = Genre.objects.all().order_by("-id")
    serializer_class = GenresSerial


class GenresCreateAPIView(generics.CreateAPIView):
    serializer_class = GenresSerial


class GenresRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenresSerial


class GenresRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenresSerial


class GenresDestroyAPIView(generics.DestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenresSerial


# Movie Views
class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all().order_by("-id")
    serializer_class = MovieSerial


class MovieCreateAPIView(generics.CreateAPIView):
    serializer_class = MovieSerial


class MovieRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerial


class MovieRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerial


class MovieDestroyAPIView(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerial


# Reviewer Views
class ReviewerListAPIView(generics.ListAPIView):
    queryset = Reviewer.objects.all().order_by("-id")
    serializer_class = ReviewerSerial


class ReviewerCreateAPIView(generics.CreateAPIView):
    serializer_class = ReviewerSerial


class ReviewerRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerial


class ReviewerRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerial


class ReviewerDestroyAPIView(generics.DestroyAPIView):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerial


# Movie Cast Views
class MovieCastListAPIView(generics.ListAPIView):
    queryset = MovieCast.objects.all().order_by("-id")
    serializer_class = Movie_castSerial


class MovieCastCreateAPIView(generics.CreateAPIView):
    serializer_class = Movie_castSerial


class MovieCastRetrieveAPIView(generics.RetrieveAPIView):
    queryset = MovieCast.objects.all()
    serializer_class = Movie_castSerial


class MovieCastRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = MovieCast.objects.all()
    serializer_class = Movie_castSerial


class MovieCastDestroyAPIView(generics.DestroyAPIView):
    queryset = MovieCast.objects.all()
    serializer_class = Movie_castSerial


# Movie Genres Views
class MovieGenresListAPIView(generics.ListAPIView):
    queryset = MovieGenre.objects.all().order_by("-id")
    serializer_class = Movie_genresSerial


class MovieGenresCreateAPIView(generics.CreateAPIView):
    serializer_class = Movie_genresSerial


class MovieGenresRetrieveAPIView(generics.RetrieveAPIView):
    queryset = MovieGenre.objects.all()
    serializer_class = Movie_genresSerial


class MovieGenresRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = MovieGenre.objects.all()
    serializer_class = Movie_genresSerial


class MovieGenresDestroyAPIView(generics.DestroyAPIView):
    queryset = MovieGenre.objects.all()
    serializer_class = Movie_genresSerial


# Rating Views
class RatingListAPIView(generics.ListAPIView):
    queryset = Rating.objects.all().order_by("-id")
    serializer_class = RatingSerial


class RatingCreateAPIView(generics.CreateAPIView):
    serializer_class = RatingSerial


class RatingRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerial


class RatingRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerial


class RatingDestroyAPIView(generics.DestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerial


# Movie Direction Views
class MovieDirectionListAPIView(generics.ListAPIView):
    queryset = MovieDirection.objects.all().order_by("-id")
    serializer_class = Movie_directionSerial


class MovieDirectionCreateAPIView(generics.CreateAPIView):
    serializer_class = Movie_directionSerial


class MovieDirectionRetrieveAPIView(generics.RetrieveAPIView):
    queryset = MovieDirection.objects.all()
    serializer_class = Movie_directionSerial


class MovieDirectionRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = MovieDirection.objects.all()
    serializer_class = Movie_directionSerial


class MovieDirectionDestroyAPIView(generics.DestroyAPIView):
    queryset = MovieDirection.objects.all()
    serializer_class = Movie_directionSerial
