# Django Traks Test


En este repositorio se encuentra todo el código fuente de la prueba técnica que estoy<br/>
realizando para el puesto de Python Backend Developer en [Spotcloud](https://spotcloud.io/) .

La prueba técnica consiste en la creación de una API utilizando python - Django que me permita crear, actualizar<br/>y obtener Tracks . Si bien la aplicación es algo muy simple de hacer el proceso de desarrollo<br/> es algo complejo y llevo un poco tiempo :blush: 

Para este proyecto estoy utilizando:

* [Django](https://www.djangoproject.com/) Como framework base
* [Django rest Framework (DRF)](https://www.django-rest-framework.org/) para la creacion de la api
* [Heroku](https://heroku.com/) para desplegar el proyecto en un servidor

<br/>

### Instalación

Para ejecutar el proyecto correctamente es indispensable tener `Docker` instalado en tu computador.
```
$ git clone https://github.com/SirRiuz/track-test
$ cd track-test
$ sudo docker-compose build
$ sudo docker-compose up
```
Tambien puedes ir a [tracks-api-test.herokuapp](https://tracks-api-test.herokuapp.com/api/v1/tracks/) y hacer uso del proyecto desplegado en heroku,
es más fácil porque<br/> no tienes que instalar nada, solo tienes que realizar las peticiones y listo.
<br/>

## Endpoints

Estas son todas las rutas que me permitem interactuar con los `Tracks`. [Live demo](https://tracks-api-test.herokuapp.com/api/v1/tracks/)

Method | HTTP request | Description
 ------------- | ------------- | -------------
**GET** | [/tracks/](http://tracks-api-test.herokuapp.com/api/v1/tracks/?format=json&limit=50) | Devuelve los 50 mejores pistas
**GET** | [/tracks/?q=querer](https://tracks-api-test.herokuapp.com/api/v1/tracks/?format=json&q=querer)| Busca pistas por su nombre
**GET** | [/tracks/?artist=Bad Bunny](https://tracks-api-test.herokuapp.com/api/v1/tracks/?artist=Bad+Bunny&format=json)| Busca pistas por artista
**GET** | [/tracks/?gender=Rap](https://tracks-api-test.herokuapp.com/api/v1/tracks/?format=json&gender=Rap)| Busca pistas por genero
**POST** | [/track/](https://tracks-api-test.herokuapp.com/api/v1/track/?format=json)| Permite crear nuevas pistas. [Mira los parámetros aquí](https://github.com/SirRiuz/track-test/blob/master/tracks/serializers.py)
**GET** | [/track/{id}/](https://tracks-api-test.herokuapp.com/api/v1/track/4/?format=json)| Devuelve una pista por medio de su id
**DELETE** | [/track/{id}/](https://tracks-api-test.herokuapp.com/api/v1/track/4/?format=json)| Elimina una pista por medio de su id




