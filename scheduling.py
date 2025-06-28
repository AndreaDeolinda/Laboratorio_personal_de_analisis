import time
import os
import sys

def cpu_intensive_task():
    pid = os.getpid()
    print(f"Proceso {pid}: Iniciando tarea intensiva de CPU.")
    
    # Definimos un tiempo de ejecución para que no corra infinitamente.
    # Puedes ajustar este valor. Por ejemplo, 60 segundos.
    execution_time_seconds = 60 
    
    start_time = time.time()
    count = 0
    
    while time.time() - start_time < execution_time_seconds:
        # Realiza una operación que consuma CPU
        count += 1
        _ = count * count * 0.123456789 # Operación flotante para simular más trabajo
        
        # Opcional: Pequeña pausa para que el sistema no se congele si la carga es extrema
        # y necesitas interactuar. Puedes quitarla si quieres carga máxima.
        # time.sleep(0.001) 
        
    print(f"Proceso {pid}: Tarea de CPU completada. Realizó {count} iteraciones.")
    sys.exit(0) # Asegura que el proceso termine después del tiempo

if __name__ == "__main__":
    cpu_intensive_task()