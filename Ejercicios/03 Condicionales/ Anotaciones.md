| Condicional | Descripción                                              | Pronunciación |
|-------------|----------------------------------------------------------|---------------|
| `if`        | Evalúa una condición; si es verdadera (True), ejecuta el bloque de código asociado. | "si"          |
| `else`      | Se ejecuta si la condición en el if es falsa (False).    | "sino"        |
| `elif`      | Combina else e if; evalúa otra condición si la anterior fue falsa. | "sino si"     |


Ejemplos if:

```python
# Verifica si un número es positivo
numero = 5
if numero > 0:
    print("El número es positivo.")
# Salida: El número es positivo.

Ejemplos if y else:
 
# Verifica si un número es positivo o negativo
numero = -3
if numero > 0:
    print("El número es positivo.")
else:
    print("El número es negativo o cero.")
# Salida: El número es negativo o cero.

Ejemplos if, elif y else:

# Verifica si un número es positivo, negativo o cero
numero = 0
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
# Salida: El número es cero.
