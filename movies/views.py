from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})

# def index(request):
#     movies = Movie.objects.all()
#     output = ', '.join([m.title for m in movies])
    
#     # Example queries:
#     # SELECT * FROM movies_movie
#     # Movie.objects.filer(release_year=1985)
#     # SELECT * FROM movies_movie WHERE release_year=1985
#     # Movie.objects.get(id=1)

#     return HttpResponse(output)
