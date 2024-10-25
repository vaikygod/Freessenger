from colorama import init, Fore, Style
import socket
import threading
init()
print(Fore.RED + '⠀⠀⠀⠀  ⣀⣠⠤⠶⠶⣖⡛⠛⠿⠿⠯⠭⠍⠉⣉⠛⠚⠛⠲⣄⠀⠀⠀⠀⠀')
print(Fore.RED +'⠀⠀ ⢀⡴⠋⠁⠀⡉⠁⢐⣒⠒⠈⠁⠀⠀⠀⠈⠁⢂⢅⡂⠀⠀⠘⣧⠀⠀⠀⠀')
print(Fore.RED +'⠀  ⠀⣼⠀⠀⠀⠁⠀⠀⠀⠂⠀⠀⠀⠀⢀⣀⣤⣤⣄⡈⠈⠀⠀⠀⠘⣇⠀⠀⠀')
print(Fore.RED +'⢠⡾⠡⠄⠀⠀⠾⠿⠿⣷⣦⣤⠀⠀⣾⣋⡤⠿⠿⠿⠿⠆⠠⢀⣀⡒⠼⢷⣄⠀')
print(Fore.RED +'⣿⠊⠊⠶⠶⢦⣄⡄⠀⢀⣿⠀⠀⠀⠈⠁⠀⠀⠙⠳⠦⠶⠞⢋⣍⠉⢳⡄⠈⣧')
print(Fore.RED +'⢹⣆⡂⢀⣿⠀⠀⡀⢴⣟⠁⠀⢀⣠⣘⢳⡖⠀⠀⣀⣠⡴⠞⠋⣽⠷⢠⠇⠀⣼')
print(Fore.WHITE +'⠀⢻⡀⢸⣿⣷⢦⣄⣀⣈⣳⣆⣀⣀⣤⣭⣴⠚⠛⠉⣹⣧⡴⣾⠋⠀⠀⣘⡼⠃')
print(Fore.WHITE +'⠀⢸⡇⢸⣷⣿⣤⣏⣉⣙⣏⣉⣹⣁⣀⣠⣼⣶⡾⠟⢻⣇⡼⠁⠀⠀⣰⠋⠀⠀')
print(Fore.WHITE +'⠀⢸⡇⠸⣿⡿⣿⢿⡿⢿⣿⠿⠿⣿⠛⠉⠉⢧⠀⣠⡴⠋⠀⠀⠀⣠⠇⠀⠀⠀')
print(Fore.WHITE +' ⢸⠀⠀⠹⢯⣽⣆⣷⣀⣻⣀⣀⣿⣄⣤⣴⠾⢛⡉⢄⡢⢔⣠⠞⠁⠀⠀⠀')
print(Fore.WHITE +' ⢸⠀⠀⠀⠢⣀⠀⠈⠉⠉⠉⠉⣉⣀⠠⣐⠦⠑⣊⡥⠞⠋⠀⠀⠀⠀⠀⠀⠀')
print(Fore.WHITE +' ⢸⡀⠀⠁⠂⠀⠀⠀⠀⠀⠀⠒⠈⠁⣀⡤⠞⠋⠁⠀⠀⠀⠀')
print(Fore.WHITE +'⠀ ⠙⠶⢤⣤⣤⣤⣤⡤⠴⠖⠚⠛⠉⠁⠀⠀⠀⠀')
print(Fore.GREEN +'SERVER ADMIN')
#crear socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345)) #define server
print('esperando conexiones')
server.listen() #server a la escucha
usuarios = {}
def manejar_cliente(usser, ip):
    usser.send(b'BIENVENIDO AL SERVER, porfavor registre su nombre ==>')
    nombre = usser.recv(1024).decode('utf-8')
    usuarios[nombre] = usser
    
    
    while True: 
        mensaje = usser.recv(5000).decode('utf-8')
        print(f'{nombre} --> {mensaje}')
        enviar_a_todos(f'{nombre} --> {mensaje}', usser)
    usser.close()
    del usuarios[usser]
    print(f'{nombre} se ha desconectado')
    
def enviar_a_todos(mensaje, cliente_remitente):
    for usuario_socket in usuarios.values():
        if usuario_socket != cliente_remitente:  # No enviar el mensaje al remitente
            try:
                usuario_socket.send(mensaje.encode('utf-8'))
            except:
                pass  # Si falla el envío, ignorar la excepción


while True:
    usser, ip = server.accept()  # Aceptar conexión
    hilo_cliente = threading.Thread(target=manejar_cliente, args=(usser, ip))
    hilo_cliente.start()  # Iniciar un nuevo hilo para manejar al cliente
print(Style.RESET_ALL)