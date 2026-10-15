#FACT 1 (RFC 9293) In the TCP header, Source Port and Destination Port are 16 bits each.
#FACT 2 (RFC 791) "Addresses are fixed length of four octets (32 bits)."

PORT__BITS=16
ADDRESS_BIT=32
number_of_possible_port_number=2**16
highest_port_number=(2**16-1)
number_of_possible_ipv4=2**32
print(f"number of possible port {number_of_possible_port_number}")
print(f"highest port number {highest_port_number}")
print(f"number of possible ipv4 {number_of_possible_ipv4}")