from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('wordtopdf',views.w2p,name='wordtopdf'),
]