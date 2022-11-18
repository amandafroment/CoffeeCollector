from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Coffee, Rating
from .forms import LocationForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def coffees_index(request):
    coffees = Coffee.objects.filter(user=request.user)
    return render(request, 'coffees/index.html', { 'coffees': coffees })

@login_required
def coffees_detail(request, coffee_id):
    coffee = Coffee.objects.get(id=coffee_id)
    ratings_coffee_doesnt_have = Rating.objects.exclude(id__in = coffee.ratings.all().values_list('id'))
    location_form = LocationForm()
    return render(request, 'coffees/detail.html', { 'coffee': coffee, 'location_form' : location_form, 'ratings' : ratings_coffee_doesnt_have })

@login_required
def assoc_rating(request, coffee_id, rating_id):
    Coffee.objects.get(id=coffee_id).ratings.add(rating_id)
    return redirect('detail', coffee_id=coffee_id)

@login_required
def add_location(request, coffee_id):
    form = LocationForm(request.POST)
    if form.is_valid():
        new_location = form.save(commit=False)
        new_location.coffee_id = coffee_id
        new_location.save()
    return redirect('detail', coffee_id=coffee_id)

class CoffeeCreate(LoginRequiredMixin, CreateView):
    model = Coffee
    fields = ['name', 'type', 'size', 'price', 'description']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CoffeeUpdate(LoginRequiredMixin, UpdateView):
    model = Coffee
    fields = '__all__'

class CoffeeDelete(LoginRequiredMixin, DeleteView):
    model = Coffee
    success_url = '/coffees/'

class RatingList(LoginRequiredMixin, ListView):
  model = Rating

class RatingDetail(LoginRequiredMixin, DetailView):
  model = Rating

class RatingCreate(LoginRequiredMixin, CreateView):
  model = Rating
  fields = '__all__'

class RatingUpdate(LoginRequiredMixin, UpdateView):
  model = Rating
  fields = ['name']

class RatingDelete(LoginRequiredMixin, DeleteView):
  model = Rating
  success_url = '/ratings/'