"""Calcular el conjunto resultante, de la interseccion de los conjuntos
 que estan conformados por los conjuntos A y B"""
  # Conjunto A
import datetime
mes_actual = datetime.datetime.now().strftime("%B")
conjunto_a = set("septiembre")
# Conjunto B
conjunto_b = set("abcdefghij")
# Intersección de conjuntos A y B
conjunto_resultante = conjunto_a & conjunto_b

print(conjunto_resultante)
print("resultado")
