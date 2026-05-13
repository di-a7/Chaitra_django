from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
   # return HttpResponse("This is home page")
   people = [
      {
         "name": "Sarah Chen","age": 29,"city": "San Francisco",
      },
      {
         "name": "Marcus Thorne","age": 42,"city": "London",
      },
      {
         "name": "Elena Rodriguez","age": 31,"city": "Madrid",
      },
      {
         "name": "Kenji Sato","age": 25,"city": "Tokyo",
      },
      {
         "name": "Marcus Thorne","age": 42,"city": "London",
      },
      {
         "name": "Marcus Thorne","age": 42,"city": "London",
      },
      {
         "name": "Ram","age": 22,"city": "nepal",
      },
   ]
   context = {
      "title":"Homepage",
      "body":"Home Page.",
      "people": people
   }
   return render(request,'home.html',context)

def about_us(request):
   return render(request, 'aboutus.html')

def contact_page(request):
   return HttpResponse("This is contact page")

# aboutus, contact html
# dynamic html
# view data send, html render