from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Restaurant(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 1000)
    address = models.TextField(max_length = 1000)
    image = models.CharField(max_length = 1000)

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse("resto_index")

    def __str__(self):
        return self.name
  # #Add a property decorator to serialize information from this database
  # @property
  # def serialize(self):
  #   return {
  #     'name': self.name,
  #     'address': self.address,
  #     'image' : self.image,
  #     'id' : self.id
  #     }

class Query(models.Model):
    location = models.CharField(max_length=1000)
    mealType = models.CharField(max_length=1000)
