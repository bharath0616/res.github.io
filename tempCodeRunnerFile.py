import ipaddress

ip_network = ipaddress.ip_network('172.16.0.0/25')
num_subnets = 2 ** (32 - ip_network.prefixlen)
num_hosts_per_subnet = 2 ** (ip_network.max_prefixlen - ip_network.prefixlen) - 2

subnet_id = ip_network.network_address
broadcast_address = ip_network.broadcast_address
subnet_mask = ip_network.netmask

# Calculate the first subnet block
first_subnet_id = subnet_id
first_subnet_broadcast = ipaddress.ip_address(int(subnet_id) + num_hosts_per_subnet + 1)
first_subnet_first_host = ipaddress.ip_address(int(subnet_id) + 1)
first_subnet_last_host = ipaddress.ip_address(int(first_subnet_broadcast) - 1)

print("Number of subnets:", num_subnets)
print("Number of hosts per subnet:", num_hosts_per_subnet)
print("Subnet ID:", subnet_id)
print("Broadcast address:", broadcast_address)
print("Subnet mask:", subnet_mask)
print("First subnet ID:", first_subnet_id)
print("First subnet broadcast address:", first_subnet_broadcast)
print("First subnet first host ID:", first_subnet_first_host)
print("First subnet last host ID:", first_subnet_last_host)
