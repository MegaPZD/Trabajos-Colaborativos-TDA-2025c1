# Trabajo Practico numero 2
## Problema 1
Para probar este algoritmo hay que utilizar la función prueba_palindromo({path del set de datos})
Se ofrece un set de palabras para probar el algoritmo, cada una con su respectivo resultado. Dicho set es el que se llama "set_palindromos.txt". De querer probar un set de datos propio revisar el formato del archivo anteriormente mencionado para el correcto funcionamiento del algoritmo de prueba.

## Problema 2

Este algoritmo utiliza programación lineal para maximizar el beneficio total eligiendo las ofertas convenientes para lograr ese beneficio máximo pero respetando una serie de restricciones. El resultado final y sus especificaciones será guardado en el archivo ```resultado_concesiones.txt```. 

## Problema 3

Este algoritmo utiliza redes de flujo para determinar si es posible asignar backups a un conjunto de antenas respetando restricciones de distancia máxima, número de backups y reutilización máxima de cada antena como backup.

## Lenguaje de programación

- **Python** 3.8 o superior

## 📦 Bibliotecas requeridas

Para ejecutar los algoritmos se debe contar con las siguientes bibliotecas instaladas:

- `networkx` (para trabajar con grafos y flujos)
- `time` y `random` (incluidas por defecto en Python)
- `pulp` (para trabajar con programación lineal)

### Instalación de dependencias

Puedes instalar `networkx` usando `pip`:

```bash
pip install networkx
```

Puedes instalar `pulp` usando `pip`:

```bash
pip install pulp
```

## Intrucciones de compilado

# palindromo.py

Es el codigo fuente del problema 2. Su compilado no retornará nada, utilizar prueba_palindromos.py para la ejecucion de varios palindromos.

Para su compilado se debe ejecutar el siguiente comando:

Windows:
```bash Windows
Python3 palindromo.py
```
Lynux
```bash Lynux
python3 palindromo.py
```

# prueba_palindromo.py

Ejecuta los set de datos de set_palindromos.txt.

Para su compilado se debe ejecutar el siguiente comando:

Windows:
```bash Windows
Python3 prueba_palindromo.py
```
Lynux
```bash Lynux
python3 prueba_palindromo.py
```

# concesiones.py

Es el código fuente del Problema 2, para su compilado se debe ejecutar el siguiente comando:

Windows:
```bash Windows
Python3 concesiones.py
```
Lynux
```bash Lynux
python3 concesiones.py
```

# antenas.py

Es el código fuente del Problema 3. Su compilado no retornará nada, utilizar antenasAleatorias.py para la ejecucion de instacias aleatorias del problema de las antenas.
Para su compilado se debe ejecutar el siguiente comando:

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


1- De este modo se utilizara una seed aleatoria para generar n, k, b, D y la matriz de distancia correspondiente.


Windows
```bash Windows
Python3 antenasAleatorias.py
```
Lynux
```bash Lynux
python3 antenasAleatorias.py
```


2- Donde seed es una seed determinada (int). De este modo se puede usar una seed ya usada para repitir las condicciones de experimentación.


Windows
```bash Windows
Python3 antenasAleatorias.py <seed>
```
Lynux
```bash Lynux
python3 antenasAleatorias.py <seed>
```

## Set de datos

# Problema 1

set_palindromos.txt: tiene 50 palabras adjuntas con sus palindromos minimos. Este archivo se utiliza prueba_palindromos.py, el cual resuelve las palabras planteadas.

# ¿Como crear un set de datos propio para testeo?

El archivo.txt debera tener el nombre de set_palindromos.txt, deberá estar contenido en la misma carpeta que prueba_palindromos.py.


Su formato deberá ser el siguiente:

<palabra> <numero de palindromos esperado> \n

# Problema 2

Se plantea el modelo solo para resolver el problema planteado en el enunciado.

# Problema 3

antenasAleatorias.py se encarga crear un set de datos aleatoriamente y mostrarlo por pantalla. La variación de n, k, b y D esta hecha para que se generen n backup de k longitud o en su defecto que indique que no existe una solución posible (y porque no es posible).
