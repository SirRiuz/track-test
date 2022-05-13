


# Django
from rest_framework import serializers



# Models
from tracks.models import Track





class TracksPaginationSerializer(serializers.ModelSerializer):
  
    """ This class it allow serialize the tracks for pagination """
  
    class Meta(object):
        model = Track
        fields = '__all__'




class TrackSerializer(serializers.Serializer):
  

    artistName = serializers.CharField(required=True)
    trackName = serializers.CharField(required=True)
    trackGender = serializers.CharField(required=True)
    
    
    
    def get(self,**kwargs) -> (dict):
        
      """ This method it allow get a track by a id """
        
      model = kwargs['model']
      id = kwargs['trackId']
      trackObject = model.objects.filter(id=id).values()

        
      if trackObject:
        return trackObject[0]
          
    
    
    def create(self,**kwargs) -> (dict):
      
      """ This method it allow create a new track """
      
      model = kwargs['model']
      artistName = kwargs['artistName']
      trackName = kwargs['trackName']
      trackGender = kwargs['trackGender']
      
      
      trackObject = model.objects.create(
        artistName=artistName,
        trackName=trackName,
        trackGender=trackGender
      )
      
      return ({
        'id':trackObject.id,
        'artistName':trackObject.artistName,
        'trackName':trackObject.trackName,
        'trackGender':trackObject.trackGender
      })
      
        
        
    def delete(self,**kwargs) -> (bool):
      
      """ This method it allow a track by a id """
      
      id = kwargs['trackId']
      model = kwargs['model']
      
      trackObject = model.objects.filter(id=id)
      if trackObject:
        trackObject = trackObject[0]
        trackObject.delete()
        return True
      




