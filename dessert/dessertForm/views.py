from django.shortcuts import render          # for us to use "render"
from .form import dessertForm                # for us to create a new "dessertForm"
from .models import Dessert                  # for us to work with different data models
from django.http import HttpResponseRedirect # for us to redirect users to different pages

# this home function will create the form and render it to the html page for users to see and fill out
def home(request):

    # this only happenes after the users "submit" the form 
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = dessertForm(request.POST)
        print(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            print('Valid')
            form.save() # save the data in the form into the database! super important
            return HttpResponseRedirect('/display/') # after submitting the form successfully, we should take the user to the "display" page and display the results
    
    # if a GET (or any other method) we'll create a blank form
    # when the page first gets loaded, it will come into this else statement because there isn't any form submittion happening
    else:
        form = dessertForm() # create a new dessert form
        return render(request, 'dessertForm/form.html', {'form': form}) # render this and send the empty new form to the html page and display to the user   

# this function renders all desserts to the display.html page and displays all the desserts
def display(request):
    all_desserts = Dessert.objects.all() # grab all the desserts from the database
    return render(request, 'dessertForm/display.html', {'all_desserts': all_desserts}) # render all the desserts data to the display.html page

def delete(request, id):
    selectedDessert = Dessert.objects.get(id=id) # get the dessert that the user wants to delete
    selectedDessert.delete() # delete the selected dessert
    # all_desserts = Dessert.objects.all() # grab the rest of the desserts from the database
    # print(selectedDessert)
    # return render(request, 'dessertForm/display.html', {'all_desserts': all_desserts})
    return HttpResponseRedirect('/display/')

def edit(request, id):
    selectedDessert = Dessert.objects.get(id=id)

    # how to prepopulate the form data?
    data = {'name': selectedDessert.name,
            'description': selectedDessert.description,
            'price': selectedDessert.price}
    form = dessertForm(data)
    print(form)

    return render(request, 'dessertForm/editForm.html', {'selectedDessert': selectedDessert, 'form': form})

def update(request):
    if request.method == 'POST':
        # print(request.POST) 
        print(request.POST.get('name')) # request.POST is a "QueryDict", so we must use "get" with the "key" to retrieve the "data"
       
        selectedDessert = Dessert.objects.filter(id = request.POST.get('id')) # 
        selectedDessert.update(name = request.POST.get('name'), description = request.POST.get('description'), price = request.POST.get('price'))

    return HttpResponseRedirect('/display/')
    
