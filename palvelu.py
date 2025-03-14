from wsgiref.simple_server import make_server
import time as t

def app(environ, respond):
    respond('200 OK', [('Content-type', 'text/html; charset=utf-8')])
    nimi = environ['PATH_INFO'].strip('/')
    salanimi = nimi.replace('a', 'apa').replace('i', 'ipi').replace('n', 'non').replace('na', 'nana')
    yield ("salainen nimesi on: %s\n" % salanimi).encode('utf-8')
    yield "<form method=GET><input type=button value=paina></form>".encode("utf-8")

if __name__ == '__main__':
    with make_server("localhost", 8000, app) as server: 
        server.serve_forever()