from rest_framework import serializers
from .models import Director, Movie, Review



class DirectorSerializer(serializers.ModelSerializer):
    movies = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = '__all__'

    def get_movies(self, obj):
        movies_count = obj.movie_set.count()
        return movies_count

class DirectorItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text movie stars'.split()

class ReviewItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'title description duration director reviews average_rating'.split()


    def get_average_rating(self, movie):
        reviews = movie.reviews.all()
        if reviews:
            sum_reviews = sum(i.stars for i in reviews)
            average_rating = round(sum_reviews / len(reviews), 2)
            return average_rating
        else:
            return None

class MovieItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'