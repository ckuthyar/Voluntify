from django.urls import path
from app11.views import home
urlpatterns = [
	path('', home),]