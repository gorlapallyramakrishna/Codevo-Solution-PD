# Task_4:File sharing app development using python:
import http.server
import socketserver
import pyqrcode
import png
import os
import socket
import webbrowser

# Function to get the IP address of the user's machine
def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Function to generate a QR code from the IP address and port
def generate_qr_code(url):
    qr = pyqrcode.create(url)
    qr.png("file_share_qr.png", scale=6)
    print(f"QR code saved as 'file_share_qr.png'. You can use it to access the file sharing server.")
    webbrowser.open("file_share_qr.png")  # Open QR code in the default image viewer

# Custom HTTP request handler to serve files in the current directory
class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Override to suppress the console output of HTTP requests
        pass

# Function to start the file-sharing server
def start_file_sharing_server(port, handler_class=CustomHTTPRequestHandler):
    httpd = socketserver.TCPServer(("", port), handler_class)
    print(f"Serving files at port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    # Set the port number and user name
    PORT = 8000
    user_name = "User"

    # Get the IP address of the user's PC
    ip_address = get_ip_address()

    # Generate the file-sharing URL
    file_sharing_url = f"http://{ip_address}:{PORT}/"
    print(f"File sharing URL: {file_sharing_url}")

    # Generate a QR code for easy access
    generate_qr_code(file_sharing_url)
    # Inform the user about the file-sharing server
    print(f"Starting file-sharing server for {user_name} at {file_sharing_url}")

    # Start the file-sharing server
    try:
        start_file_sharing_server(PORT)
    except KeyboardInterrupt:
        print("Server stopped by user.")


