#!/usr/bin/env python
"""
SYNOPSIS

    TODO This describes how to run the script via CLI.
    e.g. helloworld [-h,--help] [-v,--verbose] [--version]

DESCRIPTION

    TODO This describes how to use this script.

EXAMPLES

    TODO: Show some examples of how to use this script.

AUTHOR

    30148167@tafe.wa.edu.au

LICENSE

    This script is the exclusive and proprietary property of
    TiO2 Minerals Consultants Pty Ltd. It is only for use and
    distribution within the stated organisation and its
    undertakings.

VERSION

    $Id$

Scenario 1: Network Scanner Script
Create a script that follows the pseudocode you created in Scenario 1.
File Name: basic_network_scanner.py
Requirements:
Include completed headers at the top of the script using the TMC_Header template.
Add comments above each major block of code to explain its purpose.
If you make changes to the pseudocode that were not originally planned, include a version 2 of your pseudocode (from Task 1b).

Requirements:

Command-line Input:
The script should be executed from the command line (CLI).
The user will input the target IP address or a range of IP addresses in CIDR notation (e.g., 192.168.1.0/24).

Ports to Scan:
The script should scan for the following ports:
22 (SSH)
80 (HTTP)
443 (HTTPS)
3389 (RDP)
8080 (HTTP Alt)

Scanning Mechanism:
The script should attempt to open a TCP connection to each port in the list for each IP address in the range.
The status of each port should be reported as one of the following:
Open – The connection was successful.
Closed – The connection was refused or no service is running on the port.
Filtered – The port is unreachable due to a firewall or network filter.

Output:
The script should output the IP address and the status of each port in a human-readable format.
All results should be saved to a log file called scan_results.txt.

Error Handling:
If the user provides an invalid IP or CIDR range, the script should display an error message and terminate.
The script should gracefully handle network-related errors (e.g., connection timeouts).

BEGIN

INPUT targetIP
IF targetIP IS VALID
    CONTINUE
ELSE IF
    OUTPUT "Invalid IP"
END

FOR EACH targetIP
    FOR EACH port
        TRY connecting to port
        IF connected
            OUTPUT port, open
        ELSE IF refused OR no service
            OUTPUT port, closed
        ELSE
            OUTPUT port, filtered
    OUTPUT result
    SAVE scan_results.txt
END


https://pythontic.com/modules/socket/create_connection

"""
import ipaddress
import socket
import scapy.all as scapy

#initialize ports that needs to be scanned
ports = [22,80,443, 3389, 8080]
#initialize results list to keep the results of the scans
results = []

while True:
    #ask the user the IP addresses
    targetIP = input("Please enter the target IP address or CIDR range: ")

    #check if the IP address is valid using try-except block
    try:
        #turns the input to IPaddress object. If strict=TRUE then it can accept CIDR prefixes
        network = ipaddress.ip_network(targetIP, strict=False)

        #checks if the network version is IPv4 and not IPv6
        if network.version != 4:
            #error message for the user
            print("Invalid IP address: IP address is not IPv4. Please try again.")
        break

    #any other value error
    except ValueError:
        print("Invalid IP address: Please enter a valid IP address or CIDR range. Please try again.")

#looping through the network hosts addresses
for ip in network.hosts():
    print(f"Scanning IP address: {ip}")
    #setting up the scan result in the result list
    results.append(f"IP Scanned: {ip}")

    #looping for every port that is in the ports list
    for port in ports:
        try:
            with socket.create_connection((ip, port), timeout=1):







#check if the IP address is IPv4
