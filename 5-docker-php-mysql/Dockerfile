FROM php:7.4-apache

  RUN apt-get update && apt-get install -q -y mailutils ca-certificates curl git zlib1g-dev libpng-dev  && rm -rf /var/lib/apt/lists/*
  RUN a2enmod rewrite
  RUN docker-php-ext-install mysqli
  RUN docker-php-ext-install pdo_mysql
  RUN docker-php-ext-install gd
  RUN docker-php-ext-install bcmath
  RUN docker-php-ext-install sockets
  RUN curl -sS https://getcomposer.org/installer -o composer-setup.php
  RUN php composer-setup.php --install-dir=/usr/local/bin --filename=composer
  RUN rm -rf /var/lib/apt/lists/*

  RUN pecl install xdebug-2.9.0 && docker-php-ext-enable xdebug
  RUN echo 'zend_extension="/usr/local/lib/php/extensions/no-debug-non-zts-20151012/xdebug.so"' >> /usr/local/etc/php/php.ini
  RUN echo 'xdebug.remote_port=9000' >> /usr/local/etc/php/php.ini
  RUN echo 'xdebug.remote_enable=1' >> /usr/local/etc/php/php.ini
  RUN echo 'xdebug.remote_connect_back=1' >> /usr/local/etc/php/php.ini
  
