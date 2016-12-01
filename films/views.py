from films.models import Film, Genre
from films.serializers import FilmSerializer, GenreSerializer
from rest_framework import generics
from rest_framework.response import Response

class FilmList(generics.ListCreateAPIView):
   queryset = Film.objects.all()
   serializer_class = FilmSerializer
   
   def get(self, request, *args, **kwargs):
        k = request.GET.keys()
        filter_dict = {}
        if(k):
            for key, value in request.GET.items():
                filter_dict[key] = value
            films = Film.objects.filter(**filter_dict)
            serialized_films = FilmSerializer(films, many=True)
            return Response(serialized_films.data)
        else:
            return Response(FilmSerializer(Film.objects.all(), many=True).data)
   
#    def get(self, request, *args, **kwargs):
#        year_prod = request,GET,get('year_prod',' ')
#        # year_prod = 2012
#        films = Film.objects.filer(year_prod=year_prod)
#        serialized_films = FilmSerializer(films, many=True)
#        return Response(serialized_films.data)

class FilmDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Film.objects.all()
   serializer_class = FilmSerializer
   
class GenreList(generics.ListCreateAPIView):
     queryset = Genre.objects.all()
     serializer_class = GenreSerializer
    
class GenreDetail(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer




#from films.models import Film
#from films.serializers import FilmSerializer
#from django.http import Http404
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status


#class FilmList(APIView):
#   """
#   List all films, or create a new film.
#   """
#   def get(self, request, format=None):
#       films = Film.objects.all()
#       serialized_films = FilmSerializer(films, many=True)
#       return Response(serialized_films.data)

#   def post(self, request, format=None):
#       film = FilmSerializer(data=request.data)
#       if film.is_valid():
#           film.save()
#           return Response(film.data, status=status.HTTP_201_CREATED)
#       return Response(film.errors, status=status.HTTP_400_BAD_REQUEST)


#class FilmDetail(APIView):
#   """
#   Retrieve, update or delete a film instance.
#   """
#   def get_object(self, pk):
#       try:
#           return Film.objects.get(pk=pk)
#       except Film.DoesNotExist:
#           raise Http404

#   def get(self, request, pk, format=None):
#       film = self.get_object(pk)
#       serialized_film = FilmSerializer(film)
#       return Response(serialized_film.data)

#   def put(self, request, pk, format=None):
#       film = self.get_object(pk)
#       serialized_film = FilmSerializer(film, data=request.data)
#       if serialized_film.is_valid():
#           serialized_film.save()
#           return Response(serialized_film.data)
#       return Response(serialized_film.errors, status=status.HTTP_400_BAD_REQUEST)

#   def delete(self, request, pk, format=None):
#       film = self.get_object(pk)
#       film.delete()
#       return Response(status=status.HTTP_204_NO_CONTENT)



#class GenreList(APIView):
#   """
#   List all genres or create a new genre.
#   """
#   def get(self, request, format=None):
#       genres = Genre.objects.all()
#       serialized_genres = GenreSerializer(films, many=True)
#       return Response(serialized_genres.data)

#   def post(self, request, format=None):
#       genre = GenreSerializer(data=request.data)
#       if genre.is_valid():
#           genre.save()
#           return Response(genre.data, status=status.HTTP_201_CREATED)
#       return Response(genre.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
##@api_view(['GET', 'POST'])
##def genre_list(request, format=None):
##    """
##    List all snippets, or create a new film.
##    """
##    if request.method == 'GET':
##        theater = Genre.objects.all()
##        serializer = GenreSerializer(theater, many=True)
##        return Response(serializer.data)

##    elif request.method == 'POST':
##        serializer = GenreSerializer(data=request.data)
##        if serializer.is_valid():
##            serializer.save()
##            return Response(serializer.data, status=status.HTTP_201_CREATED)
##        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#class GenreDetail(APIView):
#   """
#   Retrieve, update or delete a film instance.
#   """
#   def get_object(self, pk):
#       try:
#           return Genre.objects.get(pk=pk)
#       except Genre.DoesNotExist:
#           raise Http404

#   def get(self, request, pk, format=None):
#       genre = self.get_object(pk)
#       serialized_genre = GenreSerializer(film)
#       return Response(serialized_film.data)

#   def put(self, request, pk, format=None):
#       genre = self.get_object(pk)
#       serialized_genre = GenreSerializer(genre, data=request.data)
#       if serialized_genre.is_valid():
#           serialized_genre.save()
#           return Response(serialized_genre.data)
#       return Response(serialized_genre.errors, status=status.HTTP_400_BAD_REQUEST)

#   def delete(self, request, pk, format=None):
#       genre = self.get_object(pk)
#       genre.delete()
#       return Response(status=status.HTTP_204_NO_CONTENT)



#from django.shortcuts import render

## Create your views here.
#from rest_framework import status
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
#from films.models import Film, Theater, Genre
#from films.serializers import FilmSerializer, TheaterSerializer, FilmGenreSerializer


#@api_view(['GET', 'POST'])
#def film_list(request, format=None):
#    """
#    List all snippets, or create a new film.
#    """
#    if request.method == 'GET':
#        films = Film.objects.all()
#        serializer = FilmSerializer(films, many=True)
#        return Response(serializer.data)

#    elif request.method == 'POST':
#        serializer = FilmSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#@api_view(['GET', 'PUT', 'DELETE'])
#def film_detail(request, pk, format=None):
#    """
#    Retrieve, update or delete a film instance.
#    """
#    try:
#        film = Film.objects.get(pk=pk)
#    except Film.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)

#    if request.method == 'GET':
#        serializer = FilmSerializer(film)
#        return Response(serializer.data)

#    elif request.method == 'PUT':
#        serializer = FilmSerializer(film, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#    elif request.method == 'DELETE':
#        film.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)

        
#@api_view(['GET', 'POST'])
#def theater_list(request, format=None):
#    """
#    List all snippets, or create a new film.
#    """
#    if request.method == 'GET':
#        theater = Theater.objects.all()
#        serializer = TheaterSerializer(theater, many=True)
#        return Response(serializer.data)

#    elif request.method == 'POST':
#        serializer = TheaterSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#@api_view(['GET', 'PUT', 'DELETE'])
#def theater_detail(request, pk, format=None):
#    """
#    Retrieve, update or delete a film instance.
#    """
#    try:
#        theater = Theater.objects.get(pk=pk)
#    except Theater.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)

#    if request.method == 'GET':
#        serializer = TheaterSerializer(film)
#        return Response(serializer.data)

#    elif request.method == 'PUT':
#        serializer = TheaterSerializer(theater, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#    elif request.method == 'DELETE':
#        film.delete()
##        return Response(status=status.HTTP_204_NO_CONTENT)/