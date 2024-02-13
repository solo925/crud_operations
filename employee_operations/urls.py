from django.urls import path
from . import views

urlpatterns = [
    path('',views.register,name ="register"),
    path('list/',views.List,name ="list"),
    path('update/<int:pk>/',views.Update,name ="update"),
    path('delete/<int:pk>/',views.Delete,name ="delete"),
]
