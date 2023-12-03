import os
import sys
import psutil
import time
import matplotlib.pyplot as plt

def monitor_process(ejecutable, log_file, interval=1, duration=None):

    process = psutil.Popen(ejecutable, shell=True)

    cpu_percent_list = []
    memory_percent_list = []
    start_time = time.time()

    while True:
        time_elapsed = time.time() - start_time

        if duration and time_elapsed >= duration:
            break

        cpu_percent = process.cpu_percent(interval=interval)
        memory_percent = process.memory_percent()

        cpu_percent_list.append(cpu_percent)
        memory_percent_list.append(memory_percent)

        log_entry = f"Time: {time_elapsed:.2f}s, CPU: {cpu_percent}%, Memory: {memory_percent}%"
        # print(log_entry)
        with open(log_file, 'a') as f:
            f.write(log_entry + '\n')

    return cpu_percent_list, memory_percent_list

def plot_graph(cpu_percent_list, memory_percent_list):
    time_values = [i for i in range(len(cpu_percent_list))]

    plt.plot(time_values, cpu_percent_list, label='CPU %')
    plt.plot(time_values, memory_percent_list, label='Memoria %')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Porcentaje %')
    plt.legend()
    plt.title('Uso de memoria y CPU en el tiempo')
    plt.show()

def main():
    # Verificar si se proporcionó el ejecutable como argumento
    if len(sys.argv) != 2:
        print("Uso: python3 consumo_proceso.py <ejecutable>")
        sys.exit()

    executable_path = sys.argv[1]

    # Monitorear y registrar el consumo de CPU y memoria
    log_file = 'registro.log'
    cpu_percent_list, memory_percent_list = monitor_process(executable_path, log_file, interval=1, duration=60)

    # Graficar los valores
    plot_graph(cpu_percent_list, memory_percent_list)
    sys.exit()


if __name__ == "__main__":
    main()