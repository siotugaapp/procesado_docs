import os

dir_path = r'C:\tmp\my_dir_with_files_to_rename'

def rename_files_in_dir(dir_path):
    import os
    for dirpath, dirs, files in os.walk(dir_path):
        for filename in files:
            os.rename(
                os.path.join(dirpath, filename),
                os.path.join(dirpath, filename.replace(' ',''))
            )

rename_files_in_dir(dir_path)
