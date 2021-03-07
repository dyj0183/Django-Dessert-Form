from django.urls import path # for us to use "path"
from . import views          # for us to call functions in the views.py

# take us to different functions in the views.py based on the url path
urlpatterns = [
    path('', views.home, name='home'),               # default and empty url, call the home function to show user the form
    path('display/', views.display, name="display"), # call the display function to display all the desserts for users to see 
    path('delete/<int:id>', views.delete, name="delete"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('update/', views.update, name="update")
]