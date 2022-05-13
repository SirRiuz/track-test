


# Django
from django.urls import path


# Views
from tracks.views import (TrackApiView,TracksApiView)



urlpatterns = [
    path('tracks/',TracksApiView.as_view()),
    path('track/<int:trackId>/',TrackApiView.as_view()),
    path('track/',TrackApiView.as_view())
]


