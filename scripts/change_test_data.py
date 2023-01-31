import os


def rename_pdf_files(directory):
    # Recorrer los directorios y archivos de forma recursiva
    for root, dirs, files in os.walk(directory):
        # Recorrer la lista de archivos
        for file in files:
            new_name = ''
            # Obtener el path completo del archivo
            file_path = os.path.join(root, file)
            # Comprobar si el archivo es un PDF
            if file.endswith("img.png"):
                # Construir el nuevo nombre del archivo
                new_name = "IMG.png"
            if file.endswith("img_1.png"):
                # Construir el nuevo nombre del archivo
                new_name = "PDF417.png"
            if new_name == '':
                continue
            # Construir el path completo del nuevo archivo
            new_file_path = os.path.join(root, new_name)
            # Renombrar el archivo
            os.rename(file_path, new_file_path)


if __name__ == '__main__':
    # Ejemplo de uso del código
    rename_pdf_files("/Users/hloliveros/PycharmProjects/peru-dni-reader/test/data/1997")
