from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from . import forms

from . import findARestaurant

@login_required
def index(request):
    # if request.method == 'GET':
  		# RETURN ALL RESTAURANTS IN DATABASE
		# restaurants = session.query(Restaurant).all()
    return render(request,'restorecommand/index.html')


def newRestaurants():
	if request.method == 'POST': # MAKE A NEW RESTAURANT AND STORE IT IN DATABASE
		location = request.form['location']
		mealType = request.form['mealType']
		restaurant_info = findARestaurant(mealType, location)
		newRestaurants = Restaurant(name = str(restaurant_info['name']), address = str(restaurant_info['address']), image = restaurant_info['image'])
		session.add(newRestaurants)
		session.commit()
		restaurants = session.query(Restaurant).all()
		return render_template('restaurants.html', restaurants = restaurants)
	else:
		return render_template('newRestaurants.html')
