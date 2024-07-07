from storage.sqlite import SQLiteDatabase

from http.server import HTTPServer
from currencies.dao import CurrenciesDAO


port = 8000

# Create HTTP-server with specified address and handler
server_address = ('0.0.0.0', port)
with HTTPServer(server_address, CurrenciesDAO) as server:
    print(f'Сервер начал работу {port}...')
    server.serve_forever()

if __name__ == '__main__':
    db = SQLiteDatabase()

    db.connect()
    db.init()
    db.disconnect()