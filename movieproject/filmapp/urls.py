
from django.urls import path
import filmapp

from . import views
app_name='filmapp'
urlpatterns = [

   #path('',views.first,name='first'),
    #path('',views.second,name='second'),
    #path('',views.third,name='third'),
    #path('film/<int:film_id>/',views.detail,name='detail'),        #third+detail
   # path('',views.link1,name='link1'),                             #detail+link1
  # path('film/<int:film_id>/',views.particular,name='particular'),  #particular+link1
   # path('',views.link2,name='link2'),                                #detail+link2
  # path('film/<int:film_id>/',views.stylin,name='stylin'),            #|
   #path('',views.link3,name='link3'),                                 #stylin+link3
   path('film/<int:film_id>/',views.stylish,name='stylish'),
   path('',views.link4,name='link4'),
   path('add/',views.add,name='add'),
   path('edit/<int:id>/',views.edit,name='edit'),
   path('delete/<int:id>/',views.delete,name='delete'),
]
