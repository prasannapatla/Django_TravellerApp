from django.urls import path
# from .views import demoView,addView
from . import views
urlpatterns = [
    path('',views.demoView,name="Demo"),
    path('add',views.addView,name="add")
    
]