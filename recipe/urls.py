from django.urls import path
from .views import receipe_list,create, update

urlpatterns = [
   path('receipe/', receipe_list),
   path('receipe/create/', create),
   path('receipe/<id>/', update),
]
