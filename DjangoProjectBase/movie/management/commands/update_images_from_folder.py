from movie.models import Movie
from django.core.management.base import BaseCommand
import os
import requests
from django.utils.text import slugify


class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        movies = Movie.objects.all()

        print(f"Found {movies.count()} movies")

        for movie in movies:
            try:
                safe_title = slugify(movie.title).replace('-','_')  # replaces spaces/special chars with "-"
                movie.image = f'movie/images/m_{safe_title}.png'
                movie.save()
                print(f"Saved and updated image for: {movie.title}")


            except Exception as e:
                print(f"Failed for {movie.title}: {e}")
            


        print("Process finished (only first movie updated).")
