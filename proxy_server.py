import socket
import requests


# Proxy server address and port
proxy_host = '192.168.103.239' # change the ip address accordingly
proxy_port = 8888


# Create a dictionary to store cached web pages
cache = {}


def proxy_server():
    # Create a socket for the proxy server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_socket:
        proxy_socket.bind((proxy_host, proxy_port))
        proxy_socket.listen()


        print(f"Proxy server listening on {proxy_host}:{proxy_port}")


        while True:
            # Accept client connection
            client_socket, client_address = proxy_socket.accept()
            with client_socket:
                print(f"Connected to client: {client_address}")


                # Receive the requested website URL from the client
                url = client_socket.recv(1024).decode('utf-8')
               
                if url in cache:
                    # Website is in the cache, send the URL to the client
                    print(f"Fetching {url} from cache...")
                    client_socket.sendall(url.encode('utf-8'))
                else:
                    # Website not in cache, fetch from the internet
                    print(f"Requesting {url} from the internet...")
                    response = requests.get(url)
                    web_content = response.text


                    # Store the content in the cache
                    cache[url] = web_content


                    # Send the URL to the client
                    client_socket.sendall(url.encode('utf-8'))


                print(f"Sent {url} to the client")


if __name__ == "__main__":
    proxy_server()
