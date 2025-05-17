| Bucles      | Descripción                                              | Pronunciación |
|-------------|----------------------------------------------------------|---------------|
| `While`     | Ejecuta un bloque de código mientras una condición sea verdadera (`True`). | "mientras"      |
| `For`       | Itera secuencialmente sobre cada elemento de un iterable (listas, cadenas, rangos, etc.). | "para cada"   |

| Keywords    | Descripción                   | Pronunciación            |
|-------------|----------------------------------------------------------|---------------|
| `in`        | Especifica el iterable a recorrer en un bucle `for`.        | "en"            |
| `break`     | Interrumpe inmediatamente la ejecución del bucle donde se encuentra.     | "interrumpir"  |
| `range()`   | Genera una secuencia de números: `range(10)` Establece un rango númerico del 0 al 9. `range(1, 10)` Establece un rango númerico del 1 al 9. `range(1, 10, 2)` Establece un rango númerico del 1 al 9 saltando de dos en dos. | "rango"


# Ejemplo `while`:
```python
# imprime todos los números hasta llegar al 5

número = 5
contador = (0)

while número >= contador:
  print(contador)
  contador += 1
  
# Salida: 1
          2
          3
          4
          5
```


# Ejemplo `for` e `in`:
```python
# Imprime cada letra de una palabra.

palabra = "Hola"

for letra in palabra:
  print(letra)
  
# Salida: H
          o
          l
          a
```

# Ejemplo `for` y `.range()`:
```python
# Imprime los números del 1 hasta el 10 contando de 2 en 2.

for número in range(1, 10 + 1, 2):
  print(número)
  
# Salida: 1 
          3
          5
          7
          9
```