"""
Ross Wade
Reads a web page and prints the ssl certificate
"""

import ssl
import socket


def get_certificate(hostname):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as sslsock:
            cert = sslsock.getpeercert()
            return cert


def print_certificate(cert):
    print("SSL Certificate Information:")
    for key, value in cert.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    website = input("Enter the website URL (e.g., example.com): ")
    try:
        certificate = get_certificate(website)
        print_certificate(certificate)
    except Exception as e:
        print(f"Error: {e}")
