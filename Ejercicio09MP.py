from multiprocessing import Process
import time
import random

def consulta_db(nombre):
    tiempo = random.randint(1, 5)
    print(f"{nombre} inició (tarda {tiempo}s)")
    time.sleep(tiempo)
    print(f"{nombre} terminó")

def usaMultiprocesamiento():
    inicio = time.time()

    print("Consulta a base de datos usando Multiprocesamiento.")

    procesos = []
    for i in range(3):
        p = Process(target=consulta_db, args=(f"Consulta {i+1}",))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    fin = time.time()
    print(f"Tiempo total con procesos: {fin - inicio:.2f}s")

if __name__ == "__main__":
    usaMultiprocesamiento()
    