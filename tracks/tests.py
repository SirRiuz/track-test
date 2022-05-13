

# Python
import json


# Models
from tracks.models import Track





def consumerApiTracks() -> (None):
    
    """
      Esta funcion se carga de registrar
      automaticamente todos los traks que 
      de estan en la api " rss.applemarketingtools.com "
    """
    
    isEmpty= Track.objects.all()
    trackList = []
    
    if not isEmpty:
        
        print('[I] La base de datos esta bacia')
        
        trackData = ''
        tracks = open('tracksdata.json','r')
        trackData = json.loads(tracks.read())['feed']['results']
        tracks.close()
        
        for track in trackData:
            trackList.append(Track(
                artistName=track['artistName'],
                trackName=track['name'],
                trackGender=track['genres'][0]['name']
            ))
            
        print('[I] Añadiendo datos de prueba')
        Track.objects.bulk_create(trackList)
        print('[I] Los datos se añadieron .... [OK]')
        
    
    else:
        print('[I] La base de datos no esta bacia')



consumerApiTracks()



