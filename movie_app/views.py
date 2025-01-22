from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Director, Review
from rest_framework import status
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, DirectorItemSerializer, \
    MovieItemSerializer, ReviewItemSerializer, DirectorValidateSerializer, MovieValidateSerializer, \
    ReviewValidateSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class DirectorDetailAPIVew(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        director = self.get_object()
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        director.name = serializer.validated_data.get('name')
        director.save()
        return Response(data=DirectorItemSerializer(director).data, status=status.HTTP_201_CREATED)



class DirectorListCreateAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    def create(self, request, *args, **kwargs):
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': serializer.errors})

        name = serializer.validated_data.get('name')

        director = Director.objects.create(
            name=name
        )
        return Response(data=DirectorItemSerializer(director).data, status=status.HTTP_201_CREATED)



class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        movie = self.get_object()
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        movie.title = serializer.validated_data.get('title')
        movie.description = serializer.validated_data.get('description')
        movie.duration = serializer.validated_data.get('duration')
        movie.director_id = serializer.validated_data.get('director_id')
        movie.save()
        return Response(data=MovieItemSerializer(movie).data, status=status.HTTP_201_CREATED)



class MovieListCreateAPIVew(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': serializer.errors})

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')

        movie = Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id
        )
        return Response(data=MovieItemSerializer(movie).data, status=status.HTTP_201_CREATED)



class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        review = self.get_object()
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        review.text = serializer.validated_data.get('text')
        review.movie_id = serializer.validated_data.get('movie_id')
        review.stars = serializer.validated_data.get('stars')
        review.save()
        return Response(data=ReviewItemSerializer(review).data, status=status.HTTP_201_CREATED)





class ReviewListCreateAPIVew(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def create(self, request, *args, **kwargs):
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': serializer.errors})

        text = serializer.validated_data.get('text')
        movie_id = serializer.validated_data.get('movie_id')
        stars = serializer.validated_data.get('stars')

        review = Review.objects.create(
            text=text,
            movie_id=movie_id,
            stars=stars
        )
        return Response(data=ReviewItemSerializer(review).data, status=status.HTTP_201_CREATED)














