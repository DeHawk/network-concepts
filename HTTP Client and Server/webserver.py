import socket
import sys


def recv_until_blank(skt):
    buffer = b""
    while b"\r\n\r\n" not in buffer:
        data = skt.recv(1024)
        if not data: # connection closed
            break
        buffer += data
    return buffer

def send_http_response(host="localhost", port=80, path="/"):
    
    with socket.socket() as skt:
             
        # Allow the socket to bind to the same local IP, port pair rapidly
        skt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Bind the socket to our port
        skt.bind(('', 28333))
        
        # Set the socket to listen
        skt.listen()
        

        
  
        # Start receiving data from the client
        
        while True:
            
            # Accept new connections
            new_conn = skt.accept()
            new_skt = new_conn[0] # accept() creates this new socket on which we send/receive data 
             
            with new_skt:
                request_data = recv_until_blank(new_skt)
                
                print("request data = ",request_data.decode())
                
                response = """HTTP/1.1 200 OK
                        Age: 586480
                        Cache-Control: max-age=604800
                        Content-Type: text/html; charset=UTF-8
                        Date: Thu, 22 Sep 2022 22:20:41 GMT
                        Etag: "3147526947+ident"
                        Expires: Thu, 29 Sep 2022 22:20:41 GMT
                        Last-Modified: Thu, 17 Oct 2019 07:18:26 GMT
                        Server: ECS (sec/96EE)
                        Vary: Accept-Encoding
                        X-Cache: HIT
                        Content-Length: 1256
                        Connection: close

                        <!doctype html>
                        <html>
                        <head>
                            <title>Example Domain</title>
                            <meta charset="utf-8" />
                            <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
                            <meta name="viewport" content="width=device-width, initial-scale=1" />
                            <style type="text/css">
                                body {
                                    background-color: #f0f0f2;
                                    margin: 0;
                                    padding: 0;
                                    font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
                                }
                                div {
                                    width: 600px;
                                    margin: 5em auto;
                                    padding: 2em;
                                    background-color: #fdfdff;
                                    border-radius: 0.5em;
                                    box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
                                }
                                a:link, a:visited {
                                    color: #38488f;
                                    text-decoration: none;
                                }
                                @media (max-width: 700px) {
                                    div {
                                        margin: 0 auto;
                                        width: auto;
                                    }
                                }
                            </style>    
                        </head>
                        <body>
                            <div>
                                <h1>Example Domain</h1>
                                <p>This domain is for use in illustrative examples in documents. You may use this
                                domain in literature without prior coordination or asking for permission.</p>
                                <p><a href="https://www.iana.org/domains/example">More information...</a></p>
                            </div>
                        </body>
                        </html>
                        """
                
                new_skt.sendall(response.encode())      
        
            
            

if __name__ == "__main__":
    if len(sys.argv)< 2:
        print("Usage: python webserver.py <host> [port]")
        sys.exit(1)
        
    host = sys.argv[1]
    port = sys.argv[2] if len(sys.argv) > 2 else 28333
    
    send_http_response(host, port=port)
    
