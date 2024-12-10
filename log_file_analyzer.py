import argparse  # Para gestionar argumentos en la línea de comandos
import re  # Para trabajar con expresiones regulares


def analyze_log(file_path, pattern):

    """
    Analiza un archivo de log y filtra líneas que coincidan
    con el patrón dado.add()

    Args:
    file_path (str): Ruta del archivo de log a analizar.
    pattern (str): Expresión regular para filtrar líneas.
    """

    try:
        with open(file_path, 'r') as log_file:  # Abre el archivo en modo lectura
            print(f"\nAnalizando el archivo: {file_path}")
            regex = re.compile(pattern)  # Cmpila la expresión regular
            matches = 0  # Contador de líneas coincidentes

            for line_number, line in enumerate(log_file, start=1):
                if regex.search(line):  # verifica si la línea coincide con el patrón
                    print(f"Línea {line_number}: {line.strip()}")
                    matches += 1

            if matches == 0:
                print("No se encontraron coincidencias con el patrón.")
            else:
                print(f"\nSe encontraron {matches} lineas que coinciden con el patrón.")
    except FileNotFoundError:
        print(f"\nError: El archivo '{file_path}' no se encontro.")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")


def main():

    """
    Punto de entrada principal para la aplicación.
    """

    parser = argparse.ArgumentParser(
        description="Log File Analyzer - Filtra y analiza archivos de log con patrones específicos."
    )
    parser.add_argument(
        "file",
        type=str,
        help="Ruta del archivo de log a analizar."
        )
    parser.add_argument(
        "pattern",
        type=str,
        help="Expresión regular para filtrar líneas."
        )

    args = parser.parse_args()  # Procesa los argumentos de la línea de comandos

    # Llama a la función de análisis con los argumentos proporcionados
    analyze_log(args.file, args.pattern)


if __name__ == "__main__":
    main()
