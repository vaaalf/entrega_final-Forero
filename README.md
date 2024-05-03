# Wonderland Blog
La aplicación se llama Wonderland Blog, consta de 3 modelos llamados: `Perfil`, `Entrada`, `Comentario` y `Usuario`.
En esta aplicación puedes crear entradas de blog, personalizar tu perfil y dejar comentarios para interactuar con otros usuarios.

## ¿Cómo probar?
- Para empezar debes registrarte y luego iniciar sesión.
- Luego deberías completar tu perfil, pero no te preocupes, puedes interactuar con la plataforma sin hacer este paso.
- Puedes crear una entrada compartiendo tus pensamientos, editarla y borrarla. 
- También puedes buscar sobre los nombres de todas las entradas.
- Puedes dejar un comentario en cualquier entrada.
- Si deseas probar la aplicación como Admin deberás crear un superuser usando el comando `python manage.py createsuperuser`.
- Te invito a leer el About me page y conocer más de mi.

## Código
El código está ubicado en dos aplicaciones de Django `blog` usando los archivos `models.py`, `forms.py`, `views.py` y `urls.py`. Para manejar todos los procesos que tienen que ver con las entradas y comentarios. 
También podrás encontrar la aplicación `accounts` usando los archivos `models.py`, `forms.py`, `views.py` y `urls.py`. Donde se encuentra lo relacionado a los usuarios y perfiles: registro, login, cambio de contraseña y edición de perfiles. 

Podrás ver que las vistas estan construidas usando `django.views.generic`, una de las muchas facilidades de Django.