import os
import sys
import psutil
import time

def run_process(process_name, command):
    try:
        # Ejecutar el proceso
        process = psutil.Popen(command, shell=True)
        print(f"Proceso {process_name} iniciado con ID: {process.pid}")

        # Monitorear el estado del proceso
        while True:
            time.sleep(1)  # Esperar un segundo antes de verificar el estado nuevamente
            process_status = process.status()

            if process_status == psutil.STATUS_ZOMBIE:
                print(f"El proceso {process_name} ha terminado. Reiniciando...")
                process = psutil.Popen(command, shell=True)
                print(f"Proceso {process_name} reiniciado con ID: {process.pid}")

    except Exception as e:
        print(f"Error inesperado: {e}")

def main():
    if len(sys.argv) != 3:
        print("Uso: python3 monitoreo.py <nombre_del_proceso> <comando>")
        sys.exit(1)

    process_name = sys.argv[1]
    command = sys.argv[2]

    run_process(process_name, command)


if __name__ == "__main__":
    main()