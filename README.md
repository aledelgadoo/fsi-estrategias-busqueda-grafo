# 🗺️ Estrategias de Búsqueda en Grafos: Mapa de Rumanía
**Autores:** Alejandro Delgado y Tomás Santana  
**Asignatura:** Fundamentos de los Sistemas Inteligentes *(Práctica 2)*  
**Universidad de Las Palmas de Gran Canaria - Curso 25/26**

---

Este repositorio contiene la solución a la **Práctica 2** de la asignatura **Fundamentos de los Sistemas Inteligentes (FSI)** de la ULPGC (Curso 25/26). El objetivo principal es ampliar un código base de búsqueda en grafos para implementar estrategias informadas y no informadas, analizando su rendimiento en el problema del mapa de Rumanía.

## 📂 Contenido del Repositorio

* **`search.py`**: Módulo principal con la lógica de los algoritmos de búsqueda y definición del problema.
* **`utils.py`**: Estructuras de datos auxiliares.
* **`run.py`**: Script de ejecución principal con menús de pruebas y experimentos.
* **`Tabla_Resultados.pdf`**: Documento con la comparativa de métricas (Nodos generados, visitados, coste, tiempo).
* **`Traza_Ramificacion_Acotacion.pdf`**: Resolución manual del algoritmo (Apartado Opcional 1).

## 🛠️ Implementación y Modificaciones

Se ha partido del código base proporcionado, respetando las interfaces existentes y ampliando la funcionalidad según los requisitos obligatorios y opcionales .

### 1. Modificaciones en `utils.py`

* **Nueva Estructura de Datos**: Se ha implementado la clase `PriorityQueue` (Cola de Prioridad). Esto es fundamental para ordenar la *lista abierta* basándose en el coste del camino, requisito indispensable para los algoritmos de Ramificación y Acotación.

### 2. Modificaciones en `search.py`

* **Documentación**: Se han añadido *docstrings* detallados para facilitar la comprensión del flujo de las funciones base.
* **Instrumentación de `graph_search`:** Se ha modificado la función genérica de búsqueda para contabilizar métricas de rendimiento:
  * **Nodos Generados**: Total de nodos creados al expandir.
  * **Nodos Visitados**: Total de nodos analizados (extraídos de la frontera).
  * **Coste**: Coste acumulado de la ruta `path_cost`.
* **Nuevos Algoritmos**:
  *  `ramificacion_acotacion(problem)`: Implementación de la estrategia de Coste Uniforme, utilizando una cola de prioridad ordenada por `path_cost`.
  * `ramificacion_acotacion_subestimacion(problem)`: Implementación de **A*** (A Estrella), utilizando una cola de prioridad ordenada por f(n) = g(n) + h(n), donde h(n) es la distancia euclídea (subestimación).
* **Clase para Experimentos**: Se ha añadido la clase `GPSProblemOverestimated`, que hereda de `GPSProblem`. Esta clase sobrescribe la función heurística `h(n)` para introducir deliberadamente un valor sobreestimado en un nodo específico, permitiendo demostrar la pérdida de optimalidad.

### 3. Modificaciones en `run.py`

* **Automatización de Pruebas**: Se ha incluido código para ejecutar secuencialmente todos los algoritmos (Anchura, Profundidad, Ramificación y Acotación, A*) sobre los casos de prueba definidos.
* **Medición de Tiempo**: Se ha añadido el cálculo del tiempo de ejecución (en segundos con notación científica) para cada algoritmo.
* **Menú Interactivo**: Se ha estructurado el fichero para permitir al usuario elegir entre ejecutar la batería de pruebas estándar o la demostración de heurística sobreestimada.


## 📊 Apartados Opcionales Realizados

Además de los requisitos obligatorios, se han completado los siguientes apartados opcionales descritos en el enunciado:

1. Traza Manual de Ramificación y Acotación 

Se ha realizado una ejecución manual paso a paso del algoritmo sobre el grafo de Rumanía (mínimo 5 iteraciones).

* 📄 **Ver:** `Traza_Ramificacion_Acotacion.pdf`

2. Heurística Sobreestimada y Optimalidad 

Se ha implementado una demostración empírica para probar que **una heurística que sobreestima no garantiza alcanzar un camino óptimo**.

* **Experimento:** Se modificó la heurística para el nodo 'Sibiu' asignándole un valor artificialmente alto.
* **Resultado:** El algoritmo A* evita pasar por Sibiu debido a la penalización en f(n), encontrando un camino alternativo con un coste real superior al óptimo. Esto se puede verificar seleccionando la **opción 2** en `run.py`.

3. Medición de Tiempos 

Se ha añadido la medición del tiempo de CPU para cada ejecución, permitiendo comparar la eficiencia temporal de las estrategias ciegas frente a las informadas.

## 📝 Conclusiones y Resultados

Los resultados obtenidos (disponibles en `Tabla_Resultados.pdf`) demuestran que:

* **Ramificación y Acotación** garantiza el coste óptimo pero explora un gran número de nodos.
* **A\* (con subestimación)** mantiene la optimalidad del coste reduciendo drásticamente el número de nodos visitados y generados gracias a la heurística de distancia euclídea.
* Las búsquedas ciegas (Anchura/Profundidad) no garantizan optimalidad en costes (en grafos ponderados) o eficiencia en memoria.


<br>

<p align="center">
  <img width="50%" alt="image" src="https://github.com/user-attachments/assets/b4c47d04-6ee6-4bc7-af93-7d05c473e2d6" />
</p>
