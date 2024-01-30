from socket import *
import webbrowser


server_ip = input("Enter the server's IP address: ") #192.168.103.239
server_address = (server_ip, 8888) #8888 is the port number of the proxy server


# TCP connection
# Client socket
client_socket = socket(AF_INET, SOCK_STREAM)




def client():
    # Create a socket for the client
    client_socket.connect(server_address)


    # Request a website from the proxy server
    website_url = input("Enter the website URL: ")
    client_socket.send(website_url.encode('utf-8'))
    print("Waiting for the URL")


    # Receive the website content from the proxy server
    web_content = client_socket.recv(4096).decode('utf-8')


    # Display the received content
    webbrowser.open(web_content)
    print("Received from Proxy Server:")
    print("Done done")
    print(web_content)


if __name__ == "__main__":
    client()
