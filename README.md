# Trabajo Practico numero 2
## Problema 1

## Problema 2

## Problema 3

Este algoritmo utiliza redes de flujo para determinar si es posible asignar backups a un conjunto de antenas respetando restricciones de distancia máxima, número de backups y reutilización máxima de cada antena como backup.

## Lenguaje de programación

- **Python** 3.8 o superior

## 📦 Bibliotecas requeridas

Para ejecutar el algoritmo se debe contar con las siguientes bibliotecas instaladas:

- `networkx` (para trabajar con grafos y flujos)
- `time` y `random` (incluidas por defecto en Python)

### Instalación de dependencias

Puedes instalar `networkx` usando `pip`:

```bash
pip install networkx
```
## Intrucciones de compilado

# antenas.py

Es el codigo fuente, para su compilado se debe ejecutar el siguiente comando:

Windows:
```bash Windows
Python3 antenas.py
```
Lynux
```bash Lynux
python3 antenas.py
```
# antenasAleatorias.py

Es el generador de instancias aleatorias del problema 3.
Utiliza el codigo fuente para la resolución de instancias.
Tiene 2 maneras de compilarse:

Windows
```bash Windows
Python3 antenasAleatorias.py
```
Lynux
```bash Lynux
python3 antenasAleatorias.py
```
De este modo se utilizara una seed aleatoria para generar n, k, b, D y la matriz de distancia correspondiente.
Windows
```bash Windows
Python3 antenasAleatorias.py <seed>
```
Lynux
```bash Lynux
python3 antenasAleatorias.py <seed>
```
Donde <seed> es una set determinada (int). De este modo se puede usar una seed ya usada para repitir las condicciones de experimentación.
