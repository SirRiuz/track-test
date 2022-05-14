# Django Traks Test


En este repositorio se encuentra todo el código fuente de la prueba técnica que estoy<br/>
realizando para el puesto de Python Backend Developer en [Spotcloud](https://spotcloud.io/) .

La oprueba tecnica consiste en la creacion de una api utilizando python - Django que me permita
crear , actualizar <br/>y obtener Tracks . Si bien la aplicación es algo muy simple de hacer el proceso de desarrollo es algo complejo y llevo<br/>tiempo
:blush: 

Para este proyecto estoy tulizando:

* [Django](https://www.djangoproject.com/) Como framework base
* [Django rest Framework (DRF)](https://www.django-rest-framework.org/) para la creacion de la api
* [Heroku](https://heroku.com/) para desplegar el proyecto en un servidor

<br/>

### Instalacion

Para ejecurar el proyecto correctamente es indispensable tener `Docker` instalado en tu computador.
```
$ git clone https://github.com/SirRiuz/track-test
$ cd track-test
$ sudo docker-compose build
$ sudo docker-compose up
```
Tambien puedes ir a [tracks-api-test.herokuapp](https://tracks-api-test.herokuapp.com/api/v1/tracks/) y hacer uso del proyecto desplegado en heroku,
es mas facil porque<br/> no tienes que instalar nada solo tienes que realizar las peticiones y listo.

<br/>

## Endpoints

Estas son todas las rutas que me permitem interactiar con los `Tracks`. [Live demo](https://tracks-api-test.herokuapp.com/api/v1/track/)

Method | HTTP request | Description
 ------------- | ------------- | -------------
**GET** | [/tracks/](https://tracks-api-test.herokuapp.com/api/v1/tracks/) | Devuelve los 50 mejores pistas
**GET** | [/tracks/?q=bailar](https://tracks-api-test.herokuapp.com/api/v1/tracks/?q=bailar)| Busca pistas por su nombre
**GET** | [/tracks/?artist=Bad Bunny](https://tracks-api-test.herokuapp.com/api/v1/tracks/?artist=Bad%20Bunny)| Busca pistas por artista
**GET** | [/tracks/?gender=pop](https://tracks-api-test.herokuapp.com/api/v1/tracks/?gender=pop)| Busca pistas por genero
**POST** | [/track/](https://tracks-api-test.herokuapp.com/api/v1/track/)| Permite crear nuevas pistas. [Mira los parametros aqui](https://tracks-api-test.herokuapp.com/api/v1/track/)
**GET** | [/track/{id}/](https://tracks-api-test.herokuapp.com/api/v1/track/1/)| Devuelve una pista por medio de su id
**DELETE** | [/track/{id}/](https://tracks-api-test.herokuapp.com/api/v1/track/1/)| Elimina una pista por medio de su id




