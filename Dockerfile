FROM bitnami/opencart:3

RUN echo 'Mutex posixsem' >>/opt/bitnami/apache2/conf/httpd.conf