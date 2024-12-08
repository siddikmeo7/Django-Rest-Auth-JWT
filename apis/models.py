from django.db import models
from django.utils import timezone


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = models.Manager()
    active_objects = SoftDeleteManager()

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super().delete()

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Reviewer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    language = models.CharField(max_length=50)
    release_date = models.DateField(auto_now=True)
    release_country = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class MovieCast(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name="movie_casts")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_casts")
    role = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.role} in {self.movie.title}"


class MovieDirection(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name="directed_movies")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_directions")

    def __str__(self):
        return f"{self.director} directing {self.movie}"


class MovieGenre(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="movie_genres")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_genres")

    def __str__(self):
        return f"{self.genre.title} in {self.movie.title}"


class Rating(models.Model):
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE, related_name="ratings")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="ratings")
    stars = models.IntegerField()
    number_of_ratings = models.IntegerField()

    def __str__(self):
        return f"Rating for {self.movie.title}"
