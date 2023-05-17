#pip install dnspython

import dns.resolver

tiposRegistro = ['A','AAAA','NS','CNAME','MX','PTR','SOA','TXT']

try:
    dominio = input("Ingrese dominio: ")
except IndexError:
    print('Syntax Error')
    quit()
for registro in tiposRegistro:
    try:
        respuesta = dns.resolver.resolve(dominio, registro)
        print(f'\n{registro} Registros')
        print('-'*30)
        for server in respuesta:
            print(server.to_text())
    except dns.resolver.NoAnswer:
        pass
    except dns.resolver.NXDOMAIN:
        print(f'{dominio} no existe')
        quit()
    except KeyboardInterrupt:
        print('no apretes cualquier cosa')
        quit()