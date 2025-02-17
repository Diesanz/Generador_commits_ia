# Gemini API Git Commit Generator

Este proyecto contiene dos scripts que utilizan la API generativa de Gemini para generar mensajes de commit en Git automáticamente. Los scripts utilizan la API para generar resúmenes sobre los cambios en los archivos de un repositorio de Git y realizar el commit con un mensaje generado automáticamente.

## Requisitos

- Python 3.6 o superior.
- Paquete `google-generativeai` para interactuar con la API de Gemini.
- Paquete `GitPython` para interactuar con el repositorio Git.
- Una clave API de Gemini (`GEMINI_API_KEY`).
- Un repositorio de Git local.

## Instalación

1. **Instalar las dependencias:**

   Instala las dependencias necesarias utilizando `pip`:

   ```bash
   pip install google-generativeai GitPython
  bash```
2.  **Configurar la clave API de Gemini:**

  Asegúrate de configurar tu clave API de Gemini como una variable de entorno antes de ejecutar los scripts. En Linux o macOS:

  ```bash
  export GEMINI_API_KEY="tu_clave_api_aqui"
  ```

  En windows
  ```bash
  set GEMINI_API_KEY=tu_clave_api_aqui
```
## Uso

### Script 1: Generar un mensaje de commit con Gemini

Este script genera un mensaje de commit utilizando la API de Gemini basado en los cambios realizados en un repositorio de Git.

**Cómo ejecutar el script:**

```bash
python script1.py <pregunta> [--modo <modo>]
```

*   `<pregunta>`: La pregunta que deseas hacer al modelo para generar la respuesta.
*   `--modo`: Opcional, especifica el modo de respuesta. Puede ser `text` (por defecto) o `json`.


### Script 2: Generar un mensaje de commit basado en diferencias en Git

Este script detecta diferencias en los archivos de un repositorio local, formula una pregunta con las diferencias, genera un mensaje de commit utilizando la API de Gemini y realiza el commit automáticamente.

**Cómo ejecutar el script:**

```bash
python script2.py <ruta_del_repositorio>
```

*   `<ruta_del_repositorio>`: La ruta al repositorio de Git donde se desea realizar el commit.


### Detalles de los scripts

#### `script1.py`

*   `configurar_api()`: Configura la API de Gemini utilizando una clave API desde una variable de entorno.
*   `obtener_respuesta()`: Envía una pregunta al modelo de Gemini y obtiene una respuesta en formato texto o JSON.
*   `main()`: Punto de entrada principal donde se manejan los argumentos y se obtiene la respuesta del modelo.

#### `script2.py`

*   `configurar_api()`: Configura la API de Gemini utilizando una clave API desde una variable de entorno.
*   `obtener_respuesta()`: Envía una pregunta al modelo de Gemini para generar una respuesta.
*   `make_commit()`: Realiza un commit en el repositorio con el mensaje generado.
*   `main()`: Obtiene las diferencias en el repositorio, genera una pregunta basada en ellas y realiza el commit con el mensaje generado.


### Notas

*   Asegúrate de que la clave API de Gemini esté correctamente configurada como variable de entorno antes de ejecutar los scripts.
*   Ambos scripts pueden generar mensajes detallados de commit en formato `text` o `json`, y pueden ser configurados para ajustarse a tus necesidades de automatización de Git.


### Contribuciones

Si deseas contribuir a este proyecto, por favor abre un issue o envía un pull request.


### Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

  
