# Requiere la instalación de gswin64.exe
# e incluir en el Path la carpeta C:\Program Files\gs\gs10.02.1\bin
# Ejemplo de llamada desde Powershell:
# gswin64.exe -sDEVICE=jpeg -r200 -dJPEGQ=100 -o "c:\tmp\SIOTUGA\docs\document-%02d.jpg" "c:\tmp\SIOTUGA\docs\PORD.pdf" -dBATCH
# 

from multiprocessing import Pool
import os
import subprocess
import time


# ================================
# CONFIG
# ================================

# directorio con los PDF
pdf_directory = r"C:\tmp\SIOTUGA\docs"
# directorio donde guardar los JPG de salida
output_dir = os.path.join(pdf_directory,"output_jpg")
# resolución JPG salida
res = 400


file_list = []

start_time = time.time()
os.makedirs(output_dir, exist_ok=True)

# get list of files in pdf_directory directory
for root, dirs, files in os.walk(pdf_directory):
    for file in (files):
        if file.endswith(".pdf"):
            file_path = os.path.join(root, file)
            file_list.append(file_path)

def convert_pdf(file_path, output_dir, resolution=res):
    file_name = os.path.basename(file_path)
    file_name = file_name.split(".")[0]
    # execute Ghostscript command, print results
    subprocess.run(["gswin64.exe", "-dNOPAUSE", "-sDEVICE=jpeg", "-dJPEGQ=100", f"-r{resolution}", f"-o{output_dir}/{file_name}-%02d.jpg", f"{file_path}", "-dBATCH"], stdout=subprocess.PIPE)


def process_pdf(args):
    file_path, i = args
    convert_pdf(file_path, output_dir, resolution=res)


if __name__ == "__main__":
    # create pool of threads to process each pdf in parrallel
    num_processes = 30
    pool = Pool(processes=(num_processes))
    pool.map(process_pdf, zip(file_list, range(len(file_list))))
    pool.close()
    print(f"Last file completed in {time.time() - start_time} seconds")

