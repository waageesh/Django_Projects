from django.urls import path
from .views  import *

urlpatterns = [
			path("user",User_view.as_view()),

]

