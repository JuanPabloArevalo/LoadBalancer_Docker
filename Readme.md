# Load BAlancer

Ejemplo Balanceo de Carga con Ngnix con 3 Servicios API REST.

  - Almacena una Cadena de Texto en una Base de Datos MongoDB
  - Muestra los 10 ultimos registros de Texto con la IP y La fecha
  - Balaceo Utilizanda Round Robin a 3 Servicios


### Tecnologias 

Desarrollado usando tecnologias:

* [Python] - Flask Rest Framework - Gunicorn.
* [Docker] - Gestion de contenedores y despliegue.
* [MongoDB] - Base de datos No relacional.
* [Nginx] - Servidor de aplicaciones.

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

### Instalación

Para la instalación requiere [Docker](https://www.docker.com/) y [Docker Compose](https://docs.docker.com/compose/).

Clonar el proyecto e ingresar al directorio creado

```sh
$ git clone https://github.com/profefonso/LoadBalancer_docker.git
$ cd LOADBALANCER_DOCKER
```

Descargar y construir las imagenes necesarias

```sh
$ docker-compose build
$ docker-compose up 
```

### Probar App

Ingrese a la direccion para ver la documentacion del API en swagger
[http://localhost:8080/](http://localhost:8080/)

Llamar al Servicio.

```sh
$ curl http://127.0.0.1:8080\?cadena=Ejemplo 
```
### Implementacion en AWS

![Alt text](https://www.nginx.com/wp-content/uploads/2018/08/NGINX-logo-rgb-large.png "Ngnix")


License
----

MIT