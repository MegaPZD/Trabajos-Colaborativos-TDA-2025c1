# Trabajo Practico numero 3
## Problema 1
Se desarrollo un algoritmo de aproximación que encuentra un subconjunto factible con la garantía de que su suma total sea al menos la mitad de la suma total de cualquier subconjunto factible de A,
obteniendo una solucion aproximada al "Problema del subconjunto factible"

## Problema 2

Este algoritmo utiliza programación lineal para maximizar el beneficio total eligiendo las ofertas convenientes para lograr ese beneficio máximo pero respetando una serie de restricciones. El resultado final y sus especificaciones será guardado en el archivo ```resultado_concesiones.txt```. 

## Problema 3

Este algoritmo utiliza redes de flujo para determinar si es posible asignar backups a un conjunto de antenas respetando restricciones de distancia máxima, número de backups y reutilización máxima de cada antena como backup.

## Lenguaje de programación

- **Python** 3.8 o superior

## 📦 Bibliotecas requeridas

Para ejecutar los algoritmos se debe contar con las siguientes bibliotecas:

- `time` , `sys` y `random` (incluidas por defecto en Python)

## Intrucciones de compilado

# subConjuntotp3.py

Es el codigo fuente del problema 1. Su compilado retornará el subConjunto S encontrado para una instancia particular de A y B.
Para instancias aleatorias del problema utilizar subConjuntotp3Aleatorio.py.

Para su compilado se debe ejecutar el siguiente comando:

Windows:
```bash Windows
Python3 subConjuntotp3.py
```
Lynux
```bash Lynux
python3 subConjuntotp3.py
```

# subConjuntotp3Aleatorio.py

Es el generador de instancias aleatorias del problema 3.
Utiliza el codigo fuente para la resolución de instancias.
Tiene 2 maneras de compilarse:


1- De este modo se utilizara una seed aleatoria para generar A, B aleatorios y resolver los Sopt y S correspondientes.


Windows:
```bash Windows
Python3 subConjuntotp3Aleatorio.py
```
Lynux
```bash Lynux
python3 subConjuntotp3Aleatorio.py
```

2- Donde seed es una seed determinada (int). De este modo se puede usar una seed ya usada para repitir las condicciones de experimentación.

Windows:
```bash Windows
Python3 subConjuntotp3Aleatorio.py <seed>
```
Lynux
```bash Lynux
python3 subConjuntotp3Aleatorio.py <seed>
```


## Set de datos

# Problema 1

subConjuntotp3Aleatorio.py se encarga crear un set de datos aleatoriamente y mostrar A, B, Sopt, S, si se cumplio la cota y la seed usada por pantalla.

# Problema 2


