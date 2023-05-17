#pip install dnspython

import dns.resolver


option = input("Elija la configuración:\n1. 'A', 'AAAA', 'NS', 'MX', 'SOA', 'TXT'\n2. 'PTR'\n3. 'CNAME'\nElija la configuración: ")

def chooser(option):
    if option == "1":
        option1()
    elif option == "2":
        return "gay2"
    elif option == "3":
        return "gay3"

resultado = chooser(option)
print(resultado)

def option1():
    tiposRegistro = ['A','AAAA','NS','MX','SOA','TXT']

    try:
        dominio = input("Ingrese dominio: ")
    except IndexError:
        return'Syntax Error'
        quit()
    for registro in tiposRegistro:
        try:
            respuesta = dns.resolver.resolve(dominio, registro)
            return f'\n{registro} Registros'
            return '-'*30
            for server in respuesta:
                return server.to_text()
        except dns.resolver.NoAnswer:
            pass
        except dns.resolver.NXDOMAIN:
            print(f'{dominio} no existe')
            quit()
        except KeyboardInterrupt:
            print('no apretes cualquier cosa')
            quit()
