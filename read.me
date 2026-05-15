#  **GamerPower Tracker API - Sistema de Gestión de Giveaways**

##  **Descripción del Proyecto**
Este proyecto consiste en el diseño e implementación de una **API REST estructurada** y una interfaz web funcional para la gestión de videojuegos gratuitos. El sistema transforma datos crudos de una API externa en información jerarquizada mediante lógica de negocio personalizada.

##  **Características Principales**
1. **Arquitectura de Microservicios Modular**: División estricta entre rutas (Routes) y servicios (Services).
2. **Motor de Clasificación**: Algoritmo de "Ranking" que asigna niveles (`NORMAL`, `EPICO`, `LEGENDARIO`) basado en el valor monetario.
3. **Validación en Tiempo Real**: Manejo de excepciones para asegurar la integridad de los datos procesados.

##  **Contrato de la API (Documentación Técnica)**

A continuación se detallan los endpoints, sus parámetros y los objetos de respuesta esperados, conforme a los requerimientos de documentación técnica.

### 1. Obtener Lista de Regalos
*   **Endpoint**: `/regalos`
*   **Método**: `GET`
*   **Respuesta Exitosa (200 OK)**:
    ```json
    [
      {
        "id": 123,
        "title": "Nombre del Juego",
        "worth": "$19.99",
        "platforms": "PC, Steam",
        "open_giveaway_url": "https://..."
      }
    ]
    ```
*   **Posibles Errores**:
    *   `502 Bad Gateway`: Error al conectar con el servidor externo de GamerPower.

### 2. Búsqueda por Calidad
*   **Endpoint**: `/buscar-por-calidad`
*   **Método**: `GET`
*   **Parámetros**: `calidad` (Query String: normal, epico, legendario).
*   **Respuesta Exitosa (200 OK)**:
    ```json
    {
      "calidad_buscada": "epico",
      "cantidad": 5,
      "juegos": [ ... ]
    }
    ```
*   **Lógica de Error**: Si se ingresa una calidad inexistente, el sistema devuelve una lista vacía con `cantidad: 0`.

### 3. Reporte Diario (Newsletter)
*   **Endpoint**: `/reporte-diario`
*   **Método**: `GET`
*   **Parámetros**: `min_val` (Float, opcional - Valor mínimo del juego).
*   **Respuesta Exitosa (200 OK)**: Retorna un objeto con un string formateado (`PlainTextResponse`) para lectura humana.
*   **Posibles Errores**:
    *   `422 Unprocessable Entity`: Si el parámetro `min_val` no es un número válido.

##  **Stack Tecnológico**
* ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) **Lenguaje**: Python 3.8+
* ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi) **Framework**: FastAPI
* ![Uvicorn](https://img.shields.io/badge/Server-Uvicorn-purple?style=flat&logo=gunicorn) **Servidor**: Uvicorn ASGI

##  **Decisiones de Diseño y Reglas de Negocio**
* **Compatibilidad**: Uso de **`NULL`** en lugar de `nullptr` para cumplir con estándares de compatibilidad del proyecto.
* **Integridad de Listas**: Inserción de **Nuevos Nodos al Final** para preservar el orden cronológico de detección.
* **Manejo de Nulos**: Se implementó una lógica de "limpieza" para transformar valores "N/A" de la API original en `0.0` para cálculos matemáticos.

##  **Autor**
* **Edwin Andres Lasso Herazo**
  * **Estudiante de Ingeniería de Sistemas**
