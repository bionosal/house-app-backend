from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.post_list),
    path('<int:pk>', views.post_details),
]
