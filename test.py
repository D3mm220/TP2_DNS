import dns.resolver

ip_address = '172.217.173.238'

try:
    reversed_dns = dns.reversename.from_address(ip_address)
    answers = dns.resolver.resolve(reversed_dns, 'PTR')
    for answer in answers:
        print(answer.target)
except dns.resolver.NXDOMAIN:
    print('No se encontró el registro PTR')
