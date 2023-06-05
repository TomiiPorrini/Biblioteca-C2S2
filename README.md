# Biblioteca-C2S2

# Cómo comenzar:
1. Clonar el repositorio e ir a la consola y colocar el siguiente comando:

```
    pip install -r requirements.txt
```
Ahora que ya tenemos todas las dependencias instaladas en nuestra computadora, entonces podemos pasar al siguiente paso.

3. Ahora, ejecutaremos el proyecto con el siguiente comando:

```
    py manage.py runserver
```

4. Listo, ahora en la consola te deberia salir una imagen como las siguiente y deberas hacer ctrl + click en la url que te señalo adelante:

![Imagen de consola](./imagenesReadme/inicio.jpeg)
> P/D: Intentá no romperlo 😅

# Funcionalidades por entidad

## 1. Autores

* Agregar un nuevo autor
    ```
    http://127.0.0.1:8000/autores/nuevo
    ```
* Activar un autor
    ```
    http://127.0.0.1:8000/autores/activar/(id del autor)
    ```
* Desactivar un autor
    ```
    http://127.0.0.1:8000/autores/desactivar/(id del autor)
    ```
* Modificar un autor existente
    ```
    http://127.0.0.1:8000/autores/modificar/(id del autor)
    ```
* Eliminar un autor existente
    ```
    http://127.0.0.1:8000/autores/eliminar/(id del autor)
    ```
* Ver el listado de todos los autores existentes
    ```
    http://127.0.0.1:8000/autores/listado
    ```
![Imagen de web](./imagenesReadme/autores.jpeg)
## 2. Empleados

* Agregar un nuevo empleado
    ```
    http://127.0.0.1:8000/empleados/nuevo
    ```
* Activar un empleado
    ```
    http://127.0.0.1:8000/empleados/activar/(id del empleado)
    ```
* Desactivar un empleado
    ```
    http://127.0.0.1:8000/empleados/desactivar/(id del empleado)
    ```
* Modificar un empleado existente
    ```
    http://127.0.0.1:8000/empleados/modificar/(id del empleado)
    ```
* Eliminar un empleado existente
    ```
    http://127.0.0.1:8000/empleados/eliminar/(id del empleado)
    ```
* Ver el listado de todos los empleados existentes
    ```
    http://127.0.0.1:8000/empleados/listado
    ```
![Imagen de web](./imagenesReadme/empleados.jpeg)
## 3. Libros

* Agregar un nuevo libro
    ```
    http://127.0.0.1:8000/libros/nuevo
    ```
* Activar un libro
    ```
    http://127.0.0.1:8000/libros/activar/(id del libro)
    ```
* Desactivar un libro
    ```
    http://127.0.0.1:8000/libros/desactivar/(id del libro)
    ```
* Modificar un libro existente
    ```
    http://127.0.0.1:8000/libros/modificar/(id del libro)
    ```
* Eliminar un libro existente
    ```
    http://127.0.0.1:8000/libros/eliminar/(id del libro)
    ```
* Ver el listado de todos los libros existentes
    ```
    http://127.0.0.1:8000/libros/listado
    ```
![Imagen de web](./imagenesReadme/libros.jpeg)
## 4. Socios

* Agregar un nuevo socio
    ```
    http://127.0.0.1:8000/socios/nuevo
    ```
* Activar un socio
    ```
    http://127.0.0.1:8000/socios/activar/(id del socio)
    ```
* Desactivar un socio
    ```
    http://127.0.0.1:8000/socios/desactivar/(id del socio)
    ```
* Modificar un socio existente
    ```
    http://127.0.0.1:8000/socios/modificar/(id del socio)
    ```
* Eliminar un socio existente
    ```
    http://127.0.0.1:8000/socios/eliminar/(id del socio)
    ```
* Ver el listado de todos los socios existentes
    ```
    http://127.0.0.1:8000/socios/listado
    ```
![Imagen de web](./imagenesReadme/socios.jpeg)

## 5. Prestamos de Libros

* Agregar un nuevo prestamo
    ```
    http://127.0.0.1:8000/prestamos/nuevo
    ```
* Modificar un prestamo existente
    ```
    http://127.0.0.1:8000/prestamos/modificar/(id del prestamo)
    ```
* Eliminar un prestamo existente
    ```
    http://127.0.0.1:8000/prestamos/eliminar/(id del prestamo)
    ```
* Ver el listado de todos los prestamos existentes
    ```
    http://127.0.0.1:8000/prestamos/listado
    ```
![Imagen de web](./imagenesReadme/prestamos.jpeg)