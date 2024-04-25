import subprocess
import time
import random

print("1 - Show Ethernet Interfaces\n2 - Change MAC Addressg\n0 - Close Program")

trigger = input("Select an option: ")


def generate_mac_address():
    mac = [random.randint(0x00, 0xFF) for _ in range(6)]
    return ':'.join(map(lambda x: f'{x:02x}', mac))


if trigger == '0':
    print("Closing Program...")
elif trigger == '1':
    print("Showing Ethernet Interfaces")
    time.sleep(1)
    subprocess.call("ifconfig")
elif trigger == '2':
    interface = input("Select your Enternet Interface: ")
    print("Generating your new MAC Address...")
    time.sleep(1)
    subprocess.call("ifconfig " + interface + " down")
    subprocess.call("ifconfig " + interface + " hw ether" + generate_mac_address)
    subprocess.call("ifconfig " + interface + " up")
    print("Your new MAC Address is: " + generate_mac_address)
else: 
    print("Invalid option. Please select a valid option.")