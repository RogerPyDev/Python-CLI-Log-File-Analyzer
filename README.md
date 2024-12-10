# Python-CLI-Log-File-Analyzer
Una herramienta CLI en Python para filtrar y analizar archivos de log. Permite buscar patrones específicos usando expresiones regulares, mostrando coincidencias con sus números de línea. Ideal para desarrolladores y administradores que necesiten analizar logs de manera rápida y eficiente.


# Log File Analyzer

Una herramienta de línea de comandos (CLI) escrita en Python para filtrar y analizar archivos de log basándose en patrones definidos por el usuario. Utiliza expresiones regulares para encontrar coincidencias y presenta resultados claros y detallados en la consola.

---

## 🚀 Características

- **Filtrado por patrones**: Busca coincidencias en las líneas de un archivo de log usando expresiones regulares.
- **Resultados claros**: Muestra el número de línea y el contenido de las líneas coincidentes.
- **Fácil de usar**: Ejecuta el programa desde la terminal con dos argumentos: archivo de log y patrón a buscar.
- **Ligero**: Sin dependencias externas adicionales, solo bibliotecas estándar de Python.

---

## 🛠️ Requisitos

- Python 3.6 o superior.

---

## 📝 Uso

Ejecuta el programa desde la terminal con la siguiente estructura:

```bash
python log_file_analyzer.py <ruta_del_archivo_de_log> <patrón>
```

### Ejemplo

Dado un archivo `example.log` con este contenido:

```plaintext
2024-11-28 10:00:00 ERROR Failed to connect to database
2024-11-28 10:01:00 INFO Connection established
2024-11-28 10:05:00 WARN Low disk space
2024-11-28 10:10:00 ERROR Timeout during query execution
```

Ejecuta el siguiente comando para buscar errores (`ERROR`):

```bash
python log_file_analyzer.py example.log "ERROR"
```

**Salida esperada:**
```plaintext
Analizando el archivo: example.log
Línea 1: 2024-11-28 10:00:00 ERROR Failed to connect to database
Línea 4: 2024-11-28 10:10:00 ERROR Timeout during query execution

Se encontraron 2 líneas que coinciden con el patrón.
```

---

## 📂 Estructura del Proyecto

```
log-file-file-analyzer/
├── log_file_analyzer.py   # Código fuente principal
├── example.log       # Archivo de log de ejemplo
└── README.md         # Documentación del repositorio
```

---

## 🛡️ Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

## 💬 Contacto

Si tienes alguna pregunta o necesitas ayuda, no dudes en contactarme:

- **GitHub**: [RogerPyDev](https://github.com/RogerPyDev)
- **LinkedIn**: [RogerPyDev](https://www.linkedin.com/in/rogerpydev/)
```

