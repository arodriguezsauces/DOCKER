## Descargamos una versión concreta de UBUNTU
FROM ubuntu:20.04

## Actualizamos el sistema e Instalamos nginx
RUN apt-get update && apt-get install -y nginx

## Creamos un fichero index.html en el directorio por defecto de nginx
## RUN echo "Mi primer Dockerfile" > /usr/share/nginx/html/index.html

ADD web  /usr/share/nginx/html

## Arrancamos NGINX a través de ENTRYPOINT para que no pueda ser
## modfiicar en la creación del contenedor
ENTRYPOINT ["/usr/sbin/nginx", "-g","daemon off;"]

## Exponemos el Puerto 80
EXPOSE 80