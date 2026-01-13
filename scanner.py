import socket

def scan_ports(target, start_port, end_port):
 try:
     target_ip = socket.gethostbyname(target)
 except socket.gaierror:
     print("Invalid hostname")
     return

 print(f"\nScanning {target_ip} from port {start_port} to {end_port}\n")

 for port in range(start_port, end_port + 1):
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.settimeout(0.5)

     if s.connect_ex((target_ip, port)) == 0:
         print(f"[+] Port {port} is OPEN")

     s.close()

if __name__ == "__main__":
 target = input("Target IP / Hostname: ")
 start = int(input("Start Port: "))
 end = int(input("End Port: "))

 scan_ports(target, start, end)
