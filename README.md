# Proyecto Biblioteca Django

## Instalación

1. Crear entorno virtual:
python -m venv env
env\Scripts\activate

2. Instalar dependencias:
pip install -r requirements.txt

3. Migraciones:
python manage.py migrate

4. Ejecutar servidor:
python manage.py runserver

## Cargar datos

python manage.py shell
exec(open("poblar_datos.py").read())

## Admin
http://127.0.0.1:8000/admin/
