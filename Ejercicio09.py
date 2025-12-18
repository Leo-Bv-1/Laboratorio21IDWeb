import threading
import time
import random

def consulta_db(nombre):
    tiempo = random.randint(1, 5)
    print(f"{nombre} inició (tarda {tiempo}s)")
    time.sleep(tiempo)
    print(f"{nombre} terminó")

def usaHilos():
    inicio = time.time()
    print("Consulta a base de datos usando hilos.")
    hilos = []
    for i in range(3):
        t = threading.Thread(target=consulta_db, args=(f"Consulta {i+1}",))
        hilos.append(t)
        t.start()

    for t in hilos:
        t.join()

    fin = time.time()
    print(f"Tiempo total con hilos: {fin - inicio:.2f} s\n")

usaHilos()

