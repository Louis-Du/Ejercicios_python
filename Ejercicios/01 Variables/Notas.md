## Tipos de Variables 
| Variable    | Descripción                                                                 | Pronunciación |
|-------------|-----------------------------------------------------------------------------|---------------|
| `input()`   | Función que solicita al usuario que introduzca datos por teclado.          | "introduce"   |                                             |               |
| `str`       | Convierte un valor en una cadena de texto.                                 | "cadena"      |
| `float`     | Convierte una cadena o número en un número de punto flotante (decimal).    |               |
| `int`       | Convierte una cadena o número en un entero. Si se proporciona una cadena que representa un número, la convierte en su valor entero. | "entero"      |
| `type`      | Devuelve el tipo de dato del valor o variable proporcionada.               | "tipo"        |

# Ejemplos 

Ejemplo de 'input':
```python
# Solicita al usuario que introduzca su nombre
nombre = input("Introduce tu nombre: ")
print(f"Hola, {nombre}!")
# Salida: Hola, [nombre introducido]!
```

Ejemplo de 'str':
```python
# Convierte un número en una cadena de texto
numero = 123
numero_como_texto = str(numero)
print(f"El número como texto es: {numero_como_texto}")
# Salida: El número como texto es: 123
```

Ejemplo de 'float':
```python
# Convierte una cadena en un número decimal
cadena = "3.14"
numero_decimal = float(cadena)
print(f"El número decimal es: {numero_decimal}")
# Salida: El número decimal es: 3.14
```

Ejemplo de 'int':
```python
# Convierte una cadena en un número entero
cadena = "42"
numero_entero = int(cadena)
print(f"El número entero es: {numero_entero}")
# Salida: El número entero es: 42
```

Ejemplo de 'type':
```python
# Verifica el tipo de dato de una variable
variable = 5.5
print(f"El tipo de dato de la variable es: {type(variable)}")
# Salida: El tipo de dato de la variable es: <class 'float'>
```