from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Question(models.Model):
    id = models.IntegerField(primary_key = True)
    question = models.TextField()
    answer = models.TextField(default="")
    BOOL_CHOICES = ((True, 'job'), (False, 'nationality'))
    option = models.BooleanField(choices=BOOL_CHOICES,default=False)

    def get_absolute_url(self):
        return reverse("interview:interview_all")
