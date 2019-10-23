# Back-end code - DNS simple subset
# Developer: Henrique da Silva Deziderio
# This program records a DNS name in a list that acknowledge A, AAAA, CNAME and TXT and add the new register in the list.
# It can delete a DNS already registered, except the originals, and check all DNS registered

# Opening file and creating list with DNS already registered: 
DNS = []
registered = 'registered_DNS'

with open(registered) as file_object:
    for line in file_object:
        DNS.append(line.rstrip())
        
fixDNS = ('A', 'AAAA', 'CNAME', 'TXT') # Tuple to define original DNS that cannot be deleted

# If the original DNS was deleted from the source file:
for fix in fixDNS:
    if fix not in DNS:
        DNS.insert(0, fix)

# First menu - user's options
print("DNS Subset\nDeveloper: Henrique da Silva Deziderio\n")
flag = input("Choose your option:\n1 - Register new DNS;\n2 - Check DNS already registrated;\n3 - Delete DNS;\n\nType 0 to exit.\n\n")
flag = int(flag)

while flag != 0:
# Registering a new DNS:
    if flag == 1:
        new = input("Type your new DNS: ")
        new = new.upper()
        if new in DNS:
            print('"' + new + '" already registrated. Please register a new domain.')
        else:
            DNS.append(new)
            print('"' + new + '" successfully registrated.')
        flag = input("\n\nChoose your option:\n1 - Register new DNS;\n2 - Check DNS already registrated;\n3 - Delete DNS;\n\nType 0 to exit.\n\n")
        flag = int(flag)

# Checking DNS already registrated:
    if flag == 2:
        print("DNS Already registrated:")
        for x in DNS:
            print(x)
        flag = input("\n\nChoose your option:\n1 - Register new DNS;\n2 - Check DNS already registrated;\n3 - Delete DNS;\n\nType 0 to exit.\n\n")
        flag = int(flag)

# Deleting DNS registrated:
    if flag == 3:
        purge = input("Type DNS to delete: ")
        purge = purge.upper()
        if purge in DNS:
            if purge in fixDNS:
                print('Sorry, "' + purge + '" cannot be deleted.\n')
            else:
                DNS.remove(purge)
                print(purge + " successfully deleted.")
        else:
            print(purge + " is not a registered DNS.")
        flag = input("\n\nChoose your option\n1 - Register new DNS\n2 - Check DNS already registrated\n3 - Delete DNS\n\nType 0 to exit\n\n")
        flag = int(flag)
    
# If a not valid option is typed
    if flag not in range(0,4):
        print("Wrong option, choose a value among 0 to 3.")
        flag = input("\n\nChoose your option\n1 - Register new DNS\n2 - Check DNS already registrated\n3 - Delete DNS\n\nType 0 to exit\n\n")
        flag = int(flag)

# Writing registered DNS on the source file:
print("Writing registered DNS on registered_DNS...\n\n")
with open(registered, 'w') as file_object:
    for x in DNS:
        file_object.write(x + '\n')
