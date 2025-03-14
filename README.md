# POO_python-

- El paradigma de POO esta basado en una abstraccion del mundo real que nos va a permitir desarrollar programas de forma mas cercana a como vemos el mundo, pensando en objetos que tenemos delante y en acciones que podemos hacer con ellos.

### Clase 

- Una clase es un tipo de dato cuyas variables se llaman objetos o instanccias.
- La clase es la definicion del concepto del mundo real y los objetos o instancias son el "propio" objeto del mundo real.
- Las clases están compuestas por dos elementos: atributos y métodos.

### Atributos
- Informacion que almacena la clase.

### Métodos
- Operaciones que pueden realizar las clases.

### Definicion de una clase en Python

```Python
class NombreClase:
    
    def __init__(self, variable1, variable2):
        self.Atributo1 = valor1
        self.Atributo2 = valor2
        
    def nombreMétodo(self):
        bloqueCodigo
```
### Componentes

```clss```: palabra reservada en Python para definir una clase.

```NombreClase```: nombre de la clase que quieres crear.

```def```: palabra reservada en Phyton que se utiliza para definir tanto el constructor de la clase (método que se ejecuta la primera vez que usas en clase)como los diferentes métodos en clase.

```__init__```: palabra reservada en Python para definir el método constructor de la clase. Es lo primero que se ejecuta cuando crear un objeto de una clase.

```(self, variableX)```: parámetro del constructor de la clase. El parámetro self es obligatorio y despues puedes tener tantos parámetro como quieras.La forma de añadir parámetros es la misma que en las funciones.

```self.Atributox```: forma de utilizacion y acceso a los atributos de la clase.

```noombreMétodo```: nombre del método de la clase

```(self)```: parámetro del método.El parámetro self es obligatorio y despues puedes tener tantos parámetro como quieras.La forma de añadir parámetros es la misma que en las funciones.

```bloqueCodigo```: instrucciones que ejecutará el método.

- Cuando defines una clase debes tener en cuenta los siguientes puntos:
   - Puedes definir tantos atributos como necesites.
   - Puedes definir tantos métodos como necesites.
   - Puedes definir tantos parámetros en el constructor y en los métodos como necesites.

##   Composición
 - Consiste en la creacion de nuevas clases apartir de otras clases existentes que actuan como elementos compositores de la nueva
 - Las clases existentes seran atrivitus de la nueva clase.
 - En POO la composicion significa entre las dos clases existe una relacion del tipo  "tiene un".
 - Ejemplo:
    - Una coordenada en dimenensiones está compuesto por dos valores, el valor del eje de las x y el valor en el eje y, ésto podria ser una clase.Un cuadrado está compuesto por cuatro coodernadas que son las cuatro vertices, ésto podria ser una clase que está compuesto por  cuatro clases del objeto coordenado 
