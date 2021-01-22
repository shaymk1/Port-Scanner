import socket
import termcolor


def scan(target, ports):
    print('\n' + 'Starting Scan For' + str(target))
    for port in range(1, ports):
        scan_port(target, port)


def scan_port(ipaddress, port):

    # initiate object socket inside a try/except
    try:

        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+]  port open " + str(port))
        sock.close()

    except:
        pass
        # print(" [-1]  port closed" + str(port))

    # asking the user to input some IP's and ports to scan
targets = input("[*] Enter Targets To Scan (split them by ,) : ")
ports = int(input("[*] Enter How Many Ports That You Want To Scan : "))
if' , ' in targets:
    print(termcolor.colored(("[*] Scanning multiple targets"), 'Red'))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)

else:
    scan(targets, ports)
