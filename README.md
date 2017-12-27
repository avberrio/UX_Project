# README

Integrantes:

* Aldo Berrios
* Rodolfo Jaramillo
* Gabriel Arjona

Versión de Python utilizada: 3.6.3.

Versión de Django utilizada: 2.0.0.



# Instrucciones de ejecución

En la carpeta raíz del proyecto ejecute el siguiente comando:

```python
python manage.py runserver
```

Posteriormente, para ir al prototipo de la interfaz usuaria por favor diríjase a http://localhost:8000

**Nota:** Debido a que el login no ha sido implementado, sólo basta con presionar el botón "Ingresar" en el formulario de Login para poder acceder a las vistas de usuario que debería observar el usuario una vez autentificado en el sistema.



## Problemas comunes

Existe la posibilidad de que luego de ejecutar `python manage.py runserver`, la consola de python arroje un error debido a que *django* no se encuentra instalado en su equipo. Para solucionar esto, debe instalar django a través de:

```python
pip3 install django
```

**Nota:** Se recomienda hacer lo anterior en un entorno virtual con python 3.6.x.