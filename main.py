import subprocess

print("1 - Show Ethernet Interfaces\n2 - Change MAC Addressg\n0 - Close Program")

trigger = input("Select an option: ")

if trigger == '0':
    print("Closing Program...")
elif trigger == '1':
    print("Showing Ethernet Interfaces")
    subprocess.call("ifconfig")