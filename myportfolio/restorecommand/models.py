from django.db import models

# Create your models here.
# class Restaurant():
#   __tablename__ = 'restaurant'
#   id = Column(Integer, primary_key = True)
#   name = Column(String)
#   address = Column(String)
#   image = Column(String)
#
#
#   #Add a property decorator to serialize information from this database
#   @property
#   def serialize(self):
#     return {
#       'name': self.name,
#       'address': self.address,
#       'image' : self.image,
#       'id' : self.id
#       }
