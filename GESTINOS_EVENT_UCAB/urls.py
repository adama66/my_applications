from django.urls import path
from  GESTINOS_EVENT_UCAB  import views 






urlpatterns = [
    path("",views.index, name='index'),

]