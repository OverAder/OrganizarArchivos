from distutils import extension
import os
import shutil

extensiones_dict = {'.txt': 'documentos',
                    '.docx': 'documentos',
                    '.pdf': 'documentos',
                    '.jpg': 'imagenes',
                    '.png': 'imagenes',
                    '.exe': 'ejecutable'
                    }

predeterminada = 'otros'
carpeta_organizar_ruta = r'C:\Users\Tropi\Downloads'

archivos = os.listdir(carpeta_organizar_ruta)

for archivo in archivos:
    archivo_origen_ruta = os.path.join(carpeta_organizar_ruta, archivo)

    if os.path.isfile(archivo_origen_ruta):
        _, extension_archivo = os.path.splitext(archivo)
        nombre_carpeta = extensiones_dict.get(extension_archivo.lower(), predeterminada)

        carpeta_destino_ruta = os.path.join(carpeta_organizar_ruta, nombre_carpeta)

        # Si la carpeta destino no existe, la creamos
        if not os.path.exists(carpeta_destino_ruta):
            os.makedirs(carpeta_destino_ruta)

        archivo_destino_ruta = os.path.join(carpeta_destino_ruta, archivo)

        # Movemos el archivo a la carpeta destino
        shutil.move(archivo_origen_ruta, archivo_destino_ruta)

print("Organización de archivos completada.")
