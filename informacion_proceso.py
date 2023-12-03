import os
import sys
import psutil

def get_process_info(process_id):
    try:
        # Obtener información del proceso usando psutil
        process = psutil.Process(process_id)

        # Obtener información específica del proceso
        process_name = process.name()
        process_pid = process.pid
        parent_pid = process.ppid()
        username = process.username()
        cpu_percent = process.cpu_percent()
        memory_info = process.memory_info()
        status = process.status()
        executable_path = process.exe()

        # mostrar la información
        print(f"Nombre del proceso: {process_name}")
        print(f"ID del proceso: {process_pid}")
        print(f"Parent process ID: {parent_pid}")
        print(f"Usuario propietario: {username}")
        print(f"Porcentaje de uso de CPU: {cpu_percent}%")
        print(f"Consumo de memoria: {memory_info.rss / (1024 * 1024):.2f} MB")
        print(f"Estado: {status}")
        print(f"Path del ejecutable: {executable_path}")

    except psutil.NoSuchProcess as e:
        print(f"Error: No existe el proceso con ID {process_id}")
    except Exception as e:
        print(f"Error inesperado: {e}")

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 informacion_proceso.py <ID_del_proceso>")
        sys.exit(1)


    process_id = int(sys.argv[1])
    get_process_info(process_id)


if __name__ == "__main__":
    main()