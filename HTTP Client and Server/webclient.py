import socket
import sys

def get_http_response(host, port=28333, path="/"):
    
    with socket.socket() as skt:
        skt.connect((host, port))
        
        request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
        
        skt.sendall(request.encode("UTF-8"))
        
        # Receive response in chunks
        response = b""
        
        while True:
            chunk = skt.recv(4096)
            if len(chunk) == 0:
                break
            response += chunk
            
        
    return response.decode("utf-8", errors="replace")


if __name__ == "__main__":
    if len(sys.argv)< 2:
        print("Usage: python webclient.py <hostname> [path]")
        sys.exit(1)
        
    host = sys.argv[1]
    path = sys.argv[2] if len(sys.argv) > 2 else "/"
    
    response = get_http_response(host, path=path)
    
    print(response)
