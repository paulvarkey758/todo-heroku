from unicodedata import name
from django.urls import path
from . import views
urlpatterns=[
    path('',views.mainfun,name="mainfun"),
    path('getdata',views.get_data, name="getdata"),
    path('deldata <int:task_id>',views.del_data, name="deldata"),
]
