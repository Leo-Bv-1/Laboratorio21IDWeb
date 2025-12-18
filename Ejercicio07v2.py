def copiar_archivo_binario(origen, destino):
    try:
        with open(origen, "rb") as f_origen:
            with open(destino, "wb") as f_destino:
                while True:
                    bloque = f_origen.read(1024)
                    if not bloque:
                        break
                    f_destino.write(bloque)

        print("Archivo binario copiado correctamente.")

    except FileNotFoundError:
        print("El archivo origen no existe.")
    except IOError as e:
        print("Error de entrada/salida:", e)

copiar_archivo_binario("imagen.jpg", "imagen_copia.jpg")
