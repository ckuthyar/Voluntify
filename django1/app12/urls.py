from django.urls import path
from app12.views import home,image1,home1
urlpatterns = [
	path('', home,name='image1'),
    path('home1',home1),
]