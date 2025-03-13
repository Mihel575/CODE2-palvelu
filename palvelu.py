from wsgiref.simple_server import make_server
import time as t

def app(environ, respond):
    respond('200 OK', [('Content-type', 'text/plain; charset=utf-8')])
    for i in range(100):
        t.sleep(1)
        if i%2 == 0:
            yield "Hello w€rld😞!".encode('utf-8')
        else:
            yield "Badbye w€rld😞!".encode('utf-8')
            
if __name__ == '__main__':
    with make_server("172.18.1.1", 8000, app) as server: 
        server.serve_forever()