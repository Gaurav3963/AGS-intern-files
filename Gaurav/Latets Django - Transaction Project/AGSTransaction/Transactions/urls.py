from django.urls import path,include
from Transactions import views

urlpatterns = [
    path('',views.index,name ="home")
]
