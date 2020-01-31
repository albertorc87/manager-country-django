# Customizar managers con Django

Este es un tutorial hecho en mi web, para verlo podéis pinchar aquí [https://cosasdedevs.com/posts/customizar-managers-en-django/](https://cosasdedevs.com/posts/customizar-managers-en-django/)

Para utilizarlo tenéis que crear el entorno virtual y lanzar el siguiente comando para instalar las librerías:

```
pip install -r requirements.txt
```

Una vez hecho esto podéis hacer pruebas lanzando el siguiente comando que os abrirá una consola:

```
python manage.py shell_plus --ipython
```

Un ejemplo para listar los paises de Asia:

```python
countries = Country.asia_objects.all()
for country in countries:
	print(country.name)
```