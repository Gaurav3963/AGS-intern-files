from django.urls import path
from django.urls.conf import include
from .views import index,tableview
urlpatterns = [
    path('', index, name='Home'),
    path('displaytable',tableview , name= 'tabledata')
]