from django.db import models #imports the models package from django.db. If you used startapp, this line will already be in your file.

# provide data layer tha Django uses to construct database
# When you create a model, Django executes SQL to create a corresponding table in the database
# without you having to write a single line of SQL.

# After creating all the models, must migrate before use
# 1. python manage.py makemigrations
# 2. python manage.py migrate

# The order of the classes matters!!!!!!! This Maker model needs to be declared before the "Dessert" model for the "Dessert" model to be able to reference it

# Each Django model must inherit from Django’s Model class.
# Dessert Maker Model
class Maker(models.Model):
    name = models.CharField(max_length=100)
    # why do I MUST HAVE default for age before I can migrate?
    nationality = models.CharField(max_length=100, default="United States")
    # why do I MUST HAVE default for age before I can migrate?
    age = models.CharField(max_length=10, default="30")

    # we do this so that when we run the python shell, we can see more useful information about the data
    def __str__(self):
        return self.name + " from " + self.nationality

# Dessert Company Model
class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    phone = models.CharField('Contact Phone', max_length=20)
    web = models.URLField('Web Address')
    email_address = models.EmailField('Email Address')

    # we do this so that when we run the python shell, we can see more useful information about the data
    def __str__(self):
        return self.name

# Main Dessert Model
class Dessert(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True) # that means this field can be empty
    price = models.CharField(max_length=32)
    company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE) # many to one relationship, many different kinds of desserts can be made by the same company
    makers = models.ManyToManyField(Maker) # many to many relationship, same kind of dessert could be made by multiple makers, vice versa

    # this method generates a string representation of any Python bject, this will help us see the Dessert names after we type "Dessert.objects.all()"
    def __str__(self):
        return self.name
