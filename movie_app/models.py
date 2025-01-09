from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    STARS = (
        (1, '⭐'),
        (2, '⭐ ⭐'),
        (3, '⭐ ⭐ ⭐'),
        (4, '⭐ ⭐ ⭐ ⭐'),
        (5, '⭐ ⭐ ⭐ ⭐ ⭐')
    )

    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(choices=STARS, default=1)

    def __str__(self):
        return self.text

