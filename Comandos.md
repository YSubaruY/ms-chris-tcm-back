1) Clonar el proyecto: git clone <URL_DEL_PROYECTO> y luego entrar a la carpeta con cd <NOMBRE_DEL_PROYECTO>.
 - git clone https://github.com/YSubaruY/ms-chris-tcm-back.git
 - git clone https://github.com/YSubaruY/ms-chris-tcm-back.git -b (NOMBRE_DE_LA_RAMA) => Comando para clonar una rama especifica

2) Verificar que esté instalado Python 3.12.1 :
 - python --version

3) Instalar virtualenv en cmd
 - pip install virtualenv==20.26.3

4) Crear el entorno virtual dentro de la ruta del proyecto 
 - python -m venv venv

5) Activar el entorno virtual con 
 - .\venv\Scripts\activate

6) Instalar Django con 
 - pip install Django==5.1.7

7) Instalar las dependencias del proyecto con 
 - pip install -r requirements.txt

8) Iniciar el proyecto 
 - python manage.py runserver


###Otros comandos

#Django
 - django-admin startproject nombre_proyecto  => Crear un proyecto principal en Django
 - python manage.py startapp nombre_app       => Crear una aplicación dentro del proyecto
 - python manage.py runserver                 => Iniciar el servidor de desarrollo
 - python manage.py makemigrations            => Preparar las migraciones (crear archivos de migración)
 - python manage.py migrate                   => Aplicar las migraciones a la base de datos
 - python manage.py createsuperuser           => Crear un superusuario para acceder al admin


#Dockers
 - docker build -t dev/tcmback-dev .
 - docker run -p 8000:8000 dev/tcmback-dev
 - docker run -v "directory/":/app - 8000:8000 dev/swmgecmpa-dev