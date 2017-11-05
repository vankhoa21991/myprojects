from django import forms

from .models import Restaurant,Query

class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ('location','mealType')


class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = ('id','name', 'address','image')
