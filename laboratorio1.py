# Laboratorio 1
import time
import os

start_time = time.time()
print(f"PID del proceso: {os.getpid()}")
print("Estado: NUEVO")
time.sleep(2) # Simula una espera antes de la ejecución principal
ready_to_running_time = time.time()

print("Estado: EJECUTANDO (bucle intensivo)")
for _ in range(10**7):
    pass
running_to_blocked_time = time.time()

print("Estado: BLOQUEADO (esperando entrada)")
input("Presiona Enter...")
blocked_to_terminated_time = time.time()


print("Estado: TERMINADO")
end_time = time.time()

print(f"\nTiempo de Listo a Ejecutando (aproximado): {ready_to_running_time - start_time:.4f} segundos")
print(f"Tiempo de Ejecutando a Bloqueado (aproximado): {running_to_blocked_time - ready_to_running_time:.4f} segundos")
print(f"Tiempo de Bloqueado a Terminado (aproximado): {blocked_to_terminated_time - running_to_blocked_time:.4f} segundos")
print(f"Tiempo total de ejecución: {end_time - start_time:.4f} segundos")