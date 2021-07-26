from os import name
from django.urls import path,include
from Transactions import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('',views.index,name ="home"),
    path('upload/',views.upload,name="upload")
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
