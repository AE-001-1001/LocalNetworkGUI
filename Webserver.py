from http.server import BaseHTTPRequestHandler, HTTPServer
from App import *
import logging
import json

hostName = "localhost"
serverPort = 8080

class MyServerCums(BaseHTTPRequestHandler):
    
    def _set_response(self):
        try:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
        except Exception as e:
            print(e)

    def do_GET(self):
        logging.info(f"GET request,\nPath: {str(self.path)}\nHeaders:\n{str(self.headers)}\n")
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))
        try:
            # Send the html message
            f = open(self.path[1:])
            self.wfile.write(f.read().encode('utf-8'))
            f.close()
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)
            logging.info('File Not Found: %s' % self.path)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))
        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))
        try:
            json_data = json.loads(post_data.decode('utf-8'))
        except ValueError as e:
            logging.error("Could not parse JSON: {}".format(e))
            return
        print(json_data)
        if 'username' in json_data:
            print(json_data['username'])
        if 'password' in json_data:
            print(json_data['password'])


def run(server_class=HTTPServer, handler_class=MyServerCums, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    # log the incoming request
    logging.info('Incoming request: %s', httpd)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')
    return 0

def main():
    run(port=serverPort, handler_class=MyServerCums)

if __name__ == "__main__":
    main()