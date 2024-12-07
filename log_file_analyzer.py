import argparse
import re


def analyze_log(file_path, pattern):

    try:
        with open(file_path, 'r') as log_file:
            print(f"\nAnalizando el archivo: {file_path}")
            regex = re.compile(pattern)
            matches = 0

            for line_number, line in enumerate(log_file, start=1):
                if regex.search(line):
                    matches += 1
                    print(f"Linea {line_number}: {line.strip()}")
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

    args = parser.parse_args()

    analyze_log(args.file, args.pattern)


if __name__ == "__main__":
    main()
