from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Restaurant,Query
from .forms import RestaurantForm,QueryForm

from .findARestaurant import findARestaurant,findAllRestaurant

@login_required
def index(request):
    if request.method == 'GET':
  # 		RETURN ALL RESTAURANTS IN DATABASE
        restaurants = findAllRestaurant()
        return render(request,'restorecommand/restorecommand_index.html',{'restaurants': restaurants})

@login_required
def showRestaurants(request):
    if request.method == 'GET':
        restaurants = Restaurant.objects.all()
        return render(request,'restorecommand/restaurants.html', {'restaurants': restaurants})


@login_required
def newRestaurants(request):
    if request.method == "POST":
        form = QueryForm(request.POST)
        if form.is_valid():

            location = form.cleaned_data['location']
            mealType = form.cleaned_data['mealType']

            # use this information
            restaurant_info = findARestaurant(mealType, location)
            return render(request,'restorecommand/restaurants.html', {'restaurants': restaurant_info})
    else:
        form = QueryForm()
    return render(request, 'restorecommand/newRestaurants.html', {'form': form})


@login_required
def addRestaurants(request):
    if request.method == "POST":
        # data = request.POST['dataabc']
        data = request.GET.get('dataabc',None)
        print(data)
        # restaurant_info = findARestaurant(restaurant_name, restaurant_address)
        # print(restaurant_info)
        # newRestaurants = Restaurant(name = str(restaurant_info['name']), address = str(restaurant_info['address']), image = restaurant_info['image'])
        #
        # newRestaurants.save()
        restaurants = Restaurant.objects.all()
        return render(request,'restorecommand/restaurants.html', {'restaurants': restaurants})
    else:
        form = QueryForm()
    return render(request, 'restorecommand/newRestaurants.html', {'form': form})

@login_required
def deleteRestaurants(request,restaurant_id):
	restaurantToDelete = Restaurant.objects.filter(id=restaurant_id)
	if request.method == 'POST':
		restaurantToDelete = Restaurant.objects.filter(id=restaurant_id).delete()
		return redirect('restorecommand:restaurants')
	else:
		return render(request,'restorecommand/deleteRestaurants.html',{'restaurant': restaurantToDelete})

@login_required
def editRestaurants(request,restaurant_id):
  editedRestaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
  if request.method == 'POST':
      if request.form['name']:
        editedRestaurant.name = request.form['name']
        # flash('Restaurant Successfully Edited %s' % editedRestaurant.name)
        return redirect(url_for('showRestaurants'))
  else:
  	return render_template('editRestaurants.html', restaurant = editedRestaurant)
