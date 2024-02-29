import os

dir_path = r'Q:\cmatv-dxotu-sxu--planeamento\IET_DOG_BOP_PLANEAMENTO\WEB\PROCESADO_SIOTUGA\28592 - PXOM ABEGONDO'

def rename_files_in_dir(dir_path):
    import os
    for dirpath, dirs, files in os.walk(dir_path):
        for filename in files:
            os.rename(
                os.path.join(dirpath, filename),
                os.path.join(dirpath, filename.replace(' ',''))
            )

rename_files_in_dir(dir_path)