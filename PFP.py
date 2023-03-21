#!/usr/bin/python
#Eddie/S10/cfc2407/James

# Importing the required modules
import psutil
import os
import requests
import platform

# Displaying The Basic System Infomation
print("\n\t\t\t Basic System Information\n")

# Printing the Architecture of the OS
print("[+] Architecture :", platform.architecture())

# Displaying the machine
print("[+] Machine :", platform.machine())

# Printing the Operating System release information
print("[+] Operating System Release :", platform.release())

# Prints the currently using system name
print("[+] System Name :",platform.system())

# This line will print the version of your Operating System
print("[+] Operating System Version :", platform.version())


# Displaying The Network Information
print("\n\t\t\t Network Information\n")

# Storing the arguments that filter out the internal IP address in a variable "ip"
ip="(ifconfig | grep broadcast | awk '{print $2}')"

# Using the OS module to print out the internal IP address with the variable "ip"
print("[+] Internal IP address :",os.system(ip))

# Using the request module to retrieve public IP 'https://api.ipify.org' and storing in variable "pubip"
pubip = requests.get('https://api.ipify.org').text

# Print out the  Public IP Address with the variable "pubip" 
print("[+] Public IP address :", pubip)

# Storing the arguments that filter out the default gateway in a variable "gateway"
gateway="(route | grep UG| awk '{print$ 2}')"

# Using the OS module to print out the default gateway with the variable "gateway"
print("[+] Default Gateway :" ,os.system(gateway))


# Displaying Disk Details
print("\n\t\t\t Disk Details\n")

# Storing the arguments that retrieve the system disk details
disk_details='(df -h)'

# Using the OS module to print out the disk details with the variable "disk_details"
print(os.system(disk_details))


# Displaying The CPU Usage
print("\n\t\t\t CPU Usage\n")

# Using the psutil module to print out the current CPU usage
cpu_frequency = psutil.cpu_freq()
print("[+]Current Frequency :", cpu_frequency,"GHz")


# Displaying The Current Directory
print("\n\t\t\t Current Directories\n")

# Using forloop to print out the only the diretories with its size

# Listing out the contents in the directory and saving it in a variable
dir_items=os.listdir()

# Running forloop
for eachitem in dir_items:

# Saving the items size in the list in a variable
	filesize=os.path.getsize(eachitem)

# Checking for the the list for directories only
	if os.path.isdir(eachitem)==True:

# Printing the directory name and size
		print(eachitem," ",os.path.getsize(eachitem),"bytes")