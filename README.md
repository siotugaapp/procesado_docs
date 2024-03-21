# PROCESADO DOCUMENTOS SIOTUGA
Utilidades de procesado


## 1. BULK FILE RENAMER

Este script de Python, `bulk_file_renamer.py`, está diseñado para renombrar archivos basándose en la información proporcionada en una hoja de cálculo de Excel.

## Requisitos

- Python 3.6 o superior
- Biblioteca pandas
- Bibliotecas os y shutil (estándar en Python)

## Cómo funciona

El script lee un archivo de Excel, itera sobre sus filas y renombra los archivos de acuerdo a las rutas y nombres especificados en el DataFrame. Se espera que las rutas originales de los archivos estén en la columna 'A' y los nuevos nombres para los archivos estén en la columna 'B'.

![image](https://github.com/siotugaapp/procesado_docs/assets/161585865/85151836-baca-4f34-ae65-e732116b98bb)


Los archivos renombrados se guardan en un directorio de destino especificado.

## Uso

Para usar este script, llama a la función `bulk_rename_files` con los siguientes parámetros:

- `excel_path`: La ruta al archivo de Excel.
- `sheet_name`: El nombre de la hoja en el archivo de Excel.
- `destination_directory`: El directorio donde se guardarán los archivos renombrados.

Este script asume que los nuevos nombres de archivo en  Excel no incluyen la extensión del archivo. El script añade la extensión '.pdf' a los nuevos nombres de archivo. Si los nuevos nombres de archivo incluyen la extensión del archivo, o si tus archivos no son PDFs, necesitarás modificar el script añadiendo la extensión adecuada (pdf, jpg, etc.)

Aquí tienes un ejemplo de cómo llamar a la función:

```python
bulk_rename_files("C:/ruta/al/tu/archivo/excel.xlsx", 'Hoja1', "C:/ruta/al/directorio/destino")
