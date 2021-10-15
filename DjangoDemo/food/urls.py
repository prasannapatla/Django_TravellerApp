from django.urls import path
# from .views import demoView,addView
from . import views
urlpatterns = [
    path('',views.homeView,name="Demo"),
    
    
]