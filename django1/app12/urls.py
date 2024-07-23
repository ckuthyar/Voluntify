from django.urls import path
from app12.views import home,image1
urlpatterns = [
	path('', home,name='image1'),
]