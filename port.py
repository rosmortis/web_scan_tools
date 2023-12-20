"""
Ross Wade
this code checks the port of a website
"""
import socket


def check_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
    except socket.error as e:
        print(f"Error: {e}")
    finally:
        sock.close()


if __name__ == "__main__":
    website_ip = input("Enter the website's IP address: ")
    port_to_check = int(input("Enter the port number to check: "))
    check_port(website_ip, port_to_check)
