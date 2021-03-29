from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):  # class is the keyword for defining a class
    #  models.Model makes the class inherit from the Models class and get treated as a model to store in a database
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # link to another model
    # cascade tells the database to delete everything in a cascading fashion
    # between linked databases
    title = models.CharField(max_length=200)  # How you define text with a limited number of characters
    text = models.TextField() # Long text without limit
    created_date = models.DateTimeField(default=timezone.now)  # this is date and time
    published_date = models.DateTimeField(blank=True, null=True)
    # allows the date and time of published_date to be either blank or null

#  functions indented so that they belong to the class

    def publish(self):
        self.published_date = timezone.now()  # Sets the published_date date and time upon website publish
        self.save()

    def __str__(self):  # dunder method that overwrites the str method and
        # tells the class what should be used when somebody tries to convert an object of the class type into a string
        return self.title

    # everything above is the blueprint for what happens within the class for objects later
