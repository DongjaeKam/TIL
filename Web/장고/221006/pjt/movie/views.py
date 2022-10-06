from distutils.file_util import move_file
from django.shortcuts import render,redirect
from .models import movie
from .forms import MovieForm

# Create your views here.
app_name = "movie"

def index(request):

    movies = movie.objects.order_by('-pk')
    # Template에 전달한다. 
    print(len(movies))
    context = {
        'movies': movies
    }
    

    return render(request,'movie/index.html',context)


def create(request):
    if request.method == 'POST':
        # DB에 저장하는 로직
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movie_form.save()
            print("save")
            return redirect('movie:index')
    else: 
        movie_form = MovieForm()
        print("else")
    context = {
        'movie_form': movie_form
    }
    return render(request, 'movie/new.html', context=context)
    

def delete(request,pk):

    print('hello')

    Movie = movie.objects.get(pk=pk)
    Movie.delete()

    return redirect('movie:index')


def update(request,pk):

    print('hello')

    Movie = movie.objects.get(pk=pk)
    Movie.delete()

    return redirect('movie:index')