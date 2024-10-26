import psutil
from datetime import datetime
from time import sleep

#main function where the variables are declared and assigned 
def main():
    date = datetime.now().strftime("%Y-%m-%d")
    log_file = f"{date}-pub.log" 
    memory_threshold_perc = int(input("Enter the thershold percentage without %: "))
    monitoring_period = int(input("Enter the monitoring period in sec: "))
    system_processes(log_file, monitoring_period,memory_threshold_perc)
        

def system_processes(log_file, monitoring_period, memory_threshold_perc):
    date = datetime.now().strftime("%Y-%m-%d")
    #Calculate thershold memory from percentage to actual memory
    used_memory = psutil.virtual_memory().used
    total_memory = psutil.virtual_memory().total
    thershold = (memory_threshold_perc/100)*total_memory
    #data = psutil.cpu_percent(interval = 1, percpu = True).cpu_count(logical=False).virtual_memory().used.disk_usage('/').used.net_connections(kind='inet4')
    #file is created
    create_log_file(log_file)
    #get the data continuously
    while True:
        t = datetime.now().strftime("%H:%M:%S")
        cpu_percent = psutil.cpu_percent()
        logical_cpus = psutil.cpu_count(logical=False)
        used_memory = psutil.virtual_memory().used
        disk_space = psutil.disk_usage('/').used
        current_host_ip = psutil.net_if_addrs()['Wi-Fi'][1].address
        #format log_info
        data = f"{date} {t}, {cpu_percent}, {logical_cpus}, {used_memory}, {disk_space}, {current_host_ip}\n"
        append_log_file(log_file, data)
        #check memory exceeded the threshold
        if(used_memory > thershold):
            notification_file()
        sleep(monitoring_period)
    
def create_log_file(log_file):
    with open(log_file,'w') as file:
        file.write("")

def append_log_file(log_file, log_info):
    with open(log_file,'a') as file:
        file.write(log_info)

def notification_file():
    date = date = datetime.now().strftime("%Y-%m-%d")
    log_file = f"{date}-notification.log"
    with open(log_file,'w') as file:
        file.write("Low memory - system running out of memory.")
    
main()