

# Django
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.status import ( HTTP_400_BAD_REQUEST,
                                   HTTP_200_OK )

from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination


# Models
from .models import Track


# Serializers
from .serializers import ( TrackSerializer,
                          TracksPaginationSerializer )






class TracksApiView(ListAPIView):
    

    serializer_class = TracksPaginationSerializer
    pagination_class = LimitOffsetPagination
    
    
    def get_queryset(self):

        """
        
          This method allows me to get custom query sets,depending 
          on what is to be searched for.
          
          Search queries :
          
            tracks/?q=track_query            Search by track name
            tracks/?artist=artist_name       Search by artist name
            tracks/?gender=track_gender      Search by gender
            tracks/                          Get all tracks
          
        """
        
        trackQuery = self.request.GET.get('q')
        artistName = self.request.GET.get('artist')
        trackGender = self.request.GET.get('gender')
        
        
        if trackQuery:
            # Search by track name
            return Track.objects.filter(trackName__contains=trackQuery)

        if artistName:
            # Search by artist name
            return Track.objects.filter(artistName__contains=artistName)

        if trackGender:
            # Search by gender
            return Track.objects.filter(trackGender__contains=trackGender)


        return Track.objects.all()
    





class TrackApiView(APIView):
    
    """      
      This method contains the logic of the endpoints that 
      allow to create and delete tracks
    """
    
    
    def get(self,request,**kwargs) -> (Response):
        
        """
          This endpoint allows to obtain the data of a track 
          by means of its id
        """
        
        trackId = kwargs.get('trackId',None)
        trackData = TrackSerializer().get(
            model=Track,
            trackId=trackId
        )
        
        if not trackData:
            return Response({
                'status':'error',
                'error':{
                    'messege':f'The track id ({trackId}) not found',
                    'type':'track-not-found'
                }
            },status=HTTP_400_BAD_REQUEST)
        
        return Response({
            'status':'ok',
            'data':trackData
        },status=HTTP_200_OK)



    def post(self,request,**kwargs) -> (Response):
        
        """
          This endpoint allows to create a new track
        """
        
        trackData = TrackSerializer(data=request.data)
        
        if not trackData.is_valid():
            return Response({
                'status':'error',
                'error':trackData.error_messages
            },status=HTTP_400_BAD_REQUEST)
            
                
        trackData = trackData.create(**trackData.data,model=Track)
        
        return Response({
            'status':'ok',
            'data':trackData
        },status=HTTP_200_OK)
    
    
    
    def delete(self,request,**kwargs) -> (Response):
       
        """
          This endpoint allows to delete a track
        """
        
        trackId = kwargs.get('trackId')
        trackData = TrackSerializer().delete(
            trackId=trackId,
            model=Track
        )
        
        if not trackData:
            return Response({
                'status':'error',
                'error':{
                    'messege':f'The track id {trackId} not found',
                    'type-error':'track-not-found'
                }
            },status=HTTP_400_BAD_REQUEST)
        
        return Response({
            'status':'ok',
            'data':{
                'messege':'Track deleted !'
            }
        },status=HTTP_200_OK)
    
    





