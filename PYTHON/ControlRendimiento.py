import psutil
import time

def monitor_system(thresholds):
    while True:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        
        if cpu > thresholds['cpu']:
            print(f'ADVERTENCIA! uso de CPU al {cpu}%')
        if memory > thresholds['memory']:
            print(f'ADVERTENCIA! uso de Memoria al {memory}%')
        if disk > thresholds['disk']:
            print(f'ADVERTENCIA! uso del disco al {disk}%')
            
            
        time.sleep(10)
        
    
systemDta = {'cpu': 20, 'memory': 15, 'disk': 15}


monitor_system(systemDta)