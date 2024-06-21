# prog.movil-backend

Para ejecutar el backend primero crear el virtual enviroment, luego correr el requierements.txt en el terminal

```
python -m venv pokedex
.\pokedex\Scripts\activate
pip install -r requierements.txt
```

Despues realizar las migraciones

```
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```
