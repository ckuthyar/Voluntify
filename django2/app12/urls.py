from django.urls import path
from app12.views import home
urlpatterns = [
	path('', home),]