from django.urls import path
from .views import receipe_list,create

urlpatterns = [
   path('receipe/', receipe_list),
   path('receipe/create/', create),
]