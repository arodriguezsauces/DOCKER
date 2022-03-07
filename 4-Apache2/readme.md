# httpd - Servidor web
[Docker hub: image httpd](https://hub.docker.com/_/httpd "Imagen httpd en docker hub")

## Ejecutar el comando para contruir una imagen Docker

```batch
 $docker build -t my-apache2 .
```

## Ejecutar la imagen docker
```batch
  $ docker run -dit --name my-running-app -p 8080:80 my-apache2
  
  ```
  
## Ejecutar la imagen usando un directorio  compartido
En Windows:
```batch 

docker run --rm -it -d -p 8000:80 -v "%cd%\public-html:/usr/local/apache2/htdocs/ my-apache2
```
En Linux:
```batch
docker run --rm -it -d -p 8000:80 -v "$(pwd)"\public-html:/usr/local/apache2/htdocs/ my-apache2
```

En PowerShell
```batch
docker run --rm -it -d -p 8000:80 -v "%{PWD}"\public-html:/usr/local/apache2/htdocs/ my-apache2
```
