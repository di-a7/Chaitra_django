from django.shortcuts import render, redirect
from .models import Recipe
# Create your views here.
def receipe_list(request):
   recipe = Recipe.objects.all()
   context = {
      "title" : "Recipe Book",
      "recipes" : recipe
   }
   return render(request, 'list.html',context)

def create(request):
   if request.method == "POST":
      name = request.POST.get('name')
      ingredient = request.POST.get('ingredient')
      instruction = request.POST.get('instruction')
      time = request.POST.get('time')
      Recipe.objects.create(name = name, ingredient = ingredient, instruction = instruction, time = time)
      return redirect('/receipe/')
   return render(request,'create.html')

def update(request,id):
   recipe = Recipe.objects.get(id = id)
   context = {'recipe':recipe}
   if request.method == 'POST':
      name = request.POST.get('name')
      ingredient = request.POST.get('ingredient')
      instruction = request.POST.get('instruction')
      time = request.POST.get('time')
      recipe.name = name
      recipe.ingredient = ingredient
      recipe.instruction = instruction
      recipe.time = time
      recipe.save()
      return redirect('/receipe/')
   return render(request,'update.html',context)

# delete : 
# function in view, url , button in list.html