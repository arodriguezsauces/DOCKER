# Crear un directorio compartido entre la máquina principal y el contenedor
1. Descargar la imagen de HTTP
`docker pull httpd`
2. Descargar la web 2-http, que contiene un directorio **/app.**
3. Crear un contenedor de Apache que comparta el directorio **/app** del host con el **/usr/local/apache2/htdocs/**. El comando %cd% nos proporciona el directorio actual.
`docker run -d --name apache1 -p 80:80 -v %cd%\app:/usr/local/apache2/htdocs httpd`
4. Podemos añadir otro contenedor usando el mismo volumen.
5.`docker run -d --name apache2 -p 81:80 --volumes-from apache1 httpd`
