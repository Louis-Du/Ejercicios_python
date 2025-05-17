print("CALCULADORA PARA DOS CANTIDADES")

print('+ = suma \n- = menos \n× = multiplicar \n÷ = dividir') # Impresión en pantalla que muestra las opciones que tiene el usuario para realizar operaciones matematicas.
print("  ")

while True:
  try: # Bloque try: Intenta ejecutar este código. Si ocurre algún error conocido, salta a los bloques except.
    numero1 = float(input("Primer número: "))
    simbolo = input("Operación: ").lower()
    numero2 = float(input("Segundo número: ")) 
  
    if simbolo in ("+", "mas", "suma"):
      print(f"{numero1} + {numero2} = {numero1 + numero2}") # Realiza operaciones de suma.

    elif simbolo in ("-", "menos", "resta"):
      print(f"{numero1} - {numero2} = {numero1 - numero2}") # Realiza operaciones de resta.

    elif simbolo in ("×", "*", "x", "por", "multiplicar"):
      print(f"{numero1} × {numero2} = {numero1 * numero2}") # Realiza operaciones de multiplicación.

    elif simbolo in ("÷", "/", "dividir"):
      if numero2 == 0:
        print("ERROR: No puedes dividir entre cero")
      else:
        print(f"{numero1} ÷ {numero2} = {numero1 / numero2}")# Realiza operaciones de división y muestra error si uno de los números es un 0.

    else:
      print("Ingresa un simbolo o operador arimetico valido")

    salir_continuar = input("¿Quieres realizar otra Operación? \n(s/n):\n ").lower()
    if salir_continuar not in ("s", "y", "si", "yes"):
      break # Pregunta si quiere hacer otra operación, si no quiere entonces rompe el bucle.

  except ValueError:
    print("ERROR: Debes de ingresa un número \nIntenta de nuevo") # Muestra error si el usuario ingresa una cadena en lugar de un número.
  except ZeroDivisionError:
    print("Error: No puedes dividir entre 0\nIntenta de nuevo") # Muestra error si el usuario ingresa un 0 en el momento de ralizar una división
