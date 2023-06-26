from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.streamer_list),
    path('<int:pk>', views.streamer_details),
    path('<int:pk>/vote', views.streamer_vote),
]
