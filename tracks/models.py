

# Django
from django.db import models



# id - Id the track
# artistName - Name the artist
# trackName - Name the track
# releaseDate - track creation date
# trackGender - Name the gender the track


class Track(models.Model):
    
        
    artistName = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Name the artist'
    )

    trackName = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Name the track'
    )

    releaseDate = models.DateField(
        auto_now_add=True,
        help_text='track creation date'
    )

    trackGender = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Name the gender the track'
    )
    
    
    
    def __str__(self) -> str:
        return self.trackName
    
    
    
    