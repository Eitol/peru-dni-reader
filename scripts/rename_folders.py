import os


def rename_folders(path):
    # Obtener una lista de todas las carpetas en el directorio especificado
    folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    # Ordenar las carpetas por nombre
    folders.sort()
    # Recorrer las carpetas y cambiarlas por un nuevo nombre
    for i, folder in enumerate(folders):
        new_name = str(i + 1)
        new_path = os.path.join(path, new_name)
        if os.path.exists(new_path):
            continue
        os.rename(os.path.join(path, folder), new_path)


if __name__ == '__main__':
    # Ejemplo de uso del código
    rename_folders("/Users/hloliveros/PycharmProjects/peru-dni-reader/test/data/1997")
