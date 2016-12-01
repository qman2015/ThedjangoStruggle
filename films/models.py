from __future__ import unicode_literals

# from django.db import models

from django.db import models

class Film(models.Model):
	title = models.CharField(max_length=100, blank=True, default='')
	year_prod = models.IntegerField()
	genre = models.CharField(max_length=100, blank=True, default='')

	class Meta:
		ordering = ('title',)


class Theater(models.Model):
	theater_name = models.CharField(max_length=100, blank=True, default='')
	year_built = models.IntegerField()
	location = models.CharField(max_length=100, blank=True, default='')

	class Meta:
		ordering = ('theater_name',)

class Genre(models.Model):
        genre_basic_type = models.CharField(max_length=100, blank=True, default='')
        subgenre_type = models.CharField(max_length=100, blank=True, default='')
        genre_classification = models.CharField(max_length=100, blank=True, default='')
#        FilmGenre = models.ForeignKey(Film)
                                    
        class Meta:
                ordering = ('genre_classification',)
                
                
            
