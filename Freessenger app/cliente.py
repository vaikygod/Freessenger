import socket
import threading

def recibir_mensajes(cliente):
    while True:
        try: 
            mensaje = cliente.recv(5000).decode('utf-8')
            if mensaje:
                print(f'\n{mensaje}')
            else:
                break
        except Exception as e:
            print(f'ocurrio un error : {e}')
            break 

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(('localhost', 12345))

server_confirmation =  cliente.recv(5000).decode('utf-8')
print(f'--> {server_confirmation}')

nombre = input('por favor ingrese su nombre ===>')
cliente.send(nombre.encode('utf-8'))
hilo_recibir = threading.Thread(target=recibir_mensajes, args=(cliente,))
hilo_recibir.start()

try:
    while True:
        mensaje = input('mensaje -->  ')
        cliente.send(mensaje.encode('utf-8'))
except Exception as e:
    print(f'error : {e}')
finally :
    cliente.close()