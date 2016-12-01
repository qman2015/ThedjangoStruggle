from rest_framework import serializers
from films.models import Film, Theater, Genre


class FilmSerializer(serializers.ModelSerializer):
    # genre = GenreSerializer()

    class Meta:
        model = Film
        fields = ('id', 'title', 'year_prod', 'genre')
        depth = 1

class FilmWriteSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), allow_null=True)

    class Meta:
        model = Film
        fields = ('id', 'title', 'year_prod', 'genre')
        
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
      model = Genre
      fields = ('genre_basic_type', 'subgenre_type', 'genre_classification')

#class FilmSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Film
#        fields = ('id', 'title', 'year_prod', 'genre')
        
##class TheaterSerializer(serializers.ModelSerializer):
##    class Meta:
##        model = Theater
##        fields = ('id', 'theater_name', 'year_built', 'location')
        

        

#class FilmGenreSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = FilmGenre
#        fields = ('film_genre_basic_type', 'film_subgenre_type', 'film_genre_classification')