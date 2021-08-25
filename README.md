## BooksWeb

Django Web app with REST

## Instalación de dependencias

```bash
pip install -r requirements.txt
```

# Rutas 

- Lista de libros - GET

`/`

- Crear libro - POST

`/new`

- Editar libro - PUT

`/edit/<int:isbn>/`>

# Rutas API

- Lista de libros en formato JSON - GET

`/api/books/`

- Libro por id - GET

`/api/book/<int:id>/`

- Crear libro - POST

`/api/create-book/`

# Admin

- User: superusuariopy
- Password: pysuper123

`/admin`