


# Django
from django.contrib import admin

# Models
from tracks.models import Track




@admin.register(Track)
class TracksModel(admin.ModelAdmin):
    """ Add model to Django admin """
    
    list_display = ( 'artistName','trackName' )




