"""scan_network.py"""
import nmap

print("WLAN_Network_Scanner")
nm = nmap.PortScanner()
count = 1
while count < 125:
    ip = "192.168.1." + str(count)
    print(ip + " Scanning ...")
    count = count + 1
    nm.scan(hosts=ip, arguments="-n -sP -PE -PA21,23,80,3389")
    hosts_list = [(x, nm[x]["status"]["state"]) for x in nm.all_hosts()]
    for host, status in hosts_list:
        print(host, status)
        if status == "up":
            report = open("active_devices.txt", "a")
            report.writelines(host + "\n")
            report.close()
