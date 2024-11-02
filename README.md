## Descripcion
GrowSmart es un proyecto con fines didacticos que consiste en una solución para el cuidado de plantas,
ofreciendo caracteristicas como el monitoreo de macetas inteligentes en tiempo real, consulta de datos de tus macetas,
autenticación de usuarios, etc. Este repositorio en especifico es la parte del backend de todo este proyecto y en el cual
se albergan gran parte de las funcionalidades como las que mencione anteriormente.

## Información tecnica

python version: 3.12.5

instalación del proyecto:

Ejecuta este comando en powershell mientras estas posicionado en un directorio pertinente:
```bash        
git clone https://github.com/ivanErnestoDelgado/GrowSmartServidor.git
```
instalación de dependencias:
```bash
cd GrowSmartServidor
pip install -r requirements.txt
```

Uso:
    Para iniciar el servidor:
```bash
python manage.py runserver
```

Dependencias utilizadas en este proyecto:
-asgiref 3.8.1
-Django 5.1.1
-djangorestframework 3.15.2
-sqlparse 0.5.1
-tzdata 2024.1
