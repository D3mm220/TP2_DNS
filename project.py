#pip install dnspython

import dns.resolver

def option1():
    tiposRegistro = ['A', 'AAAA', 'NS', 'MX', 'SOA', 'TXT']

    try:
        dominio = input("Ingrese dominio: ")
    except IndexError:
        print('Syntax Error')
    for registro in tiposRegistro:
        try:
            respuesta = dns.resolver.resolve(dominio, registro)
            print(f'\n{registro} Registros')
            print('-' * 30)
            for server in respuesta:
                print(server.to_text())
        except dns.resolver.NoAnswer:
            print ("No se encontro nada")
        except dns.resolver.NXDOMAIN:
            print(f'El dominio {dominio} no existe')
        except KeyboardInterrupt:
            print("No apretes cualquier cosa")

def option2():
    try:
        direccionIP = input("Ingrese direccion IP: ")
    except IndexError:
        print('Syntax Error')
    try:
        dnsReserved = dns.reversename.from_address(direccionIP)
        answs = dns.resolver.resolve(dnsReserved, 'PTR')
        print(f'\nPTR Registros')
        print('-' * 30)
        for answ in answs:
            print(answ.target)
    except dns.resolver.NoAnswer:
        print("No se encontro el registro CNAME para")
    except dns.resolver.NXDOMAIN:
        print(f'la direccion {direccionIP} no existe')
    except KeyboardInterrupt:
        print("No apretes cualquier cosa")

def option3():
    try:
        dominio = input("Ingrese dominio: ")
    except IndexError:
        print('Syntax Error')
    try:
        answers = dns.resolver.resolve(dominio, 'CNAME')
        for rdata in answers:
            print(f'Registro CNAME encontrado para {dominio}: {rdata.target}')
    except dns.resolver.NoAnswer:
        print(f'No se encontró el registro CNAME para {dominio}')
    except dns.resolver.NXDOMAIN:
        print(f'El dominio {dominio} no existe')
    except dns.exception.DNSException as e:
        print(f'Ocurrió un error: {str(e)}')
    except KeyboardInterrupt:
        print("No apretes cualquier cosa")

def chooser(option):
    if option == "1":
        option1()
    elif option == "2":
        option2()
    elif option == "3":
        option3()

option = input("Elija la configuración:\n1. 'A', 'AAAA', 'NS', 'MX', 'SOA', 'TXT'\n2. 'PTR'\n3. 'CNAME'\nElija la configuración: ")
resultado = chooser(option)
print(resultado)

#No comprendo porque returnea none algunas veces en algunas option()