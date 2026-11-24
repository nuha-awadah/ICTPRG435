#!/usr/bin/env python
"""
SYNOPSIS

    TODO This describes how to run the script via CLI.
    e.g. helloworld [-h,--help] [-v,--verbose] [--version]
    Run the script by entering the command [python basic_network_scanner.py]

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

#get user input for IP address and input validation function
def get_input_ip():

    #looping until the user input valid IP address
    while True:
        #ask the user the IP addresses
        targetip = input("Please enter the target IP address or CIDR range: ")

        #check if the IP address is valid using try-except block
        try:
            #turns the input to IPaddress object. If strict=TRUE then it can accept CIDR prefixes
            network = ipaddress.ip_network(targetip, strict=False)

            #checks if the network version not IPv4
            if network.version != 4:
                #error message for the user
                print("Invalid IP address: IP address is not IPv4. Please try again.")
                continue
            break

        #any other value error
        except ValueError:
            #error message for the user
            print("Invalid IP address: Please enter a valid IP address or CIDR range. Please try again.")

    return network

#checking the port either open, closed, or filtered function
def scan_port(scanIPAddress,port):

    #try except block to catch what type of error was put out when connecting to the network's ports
    try:
        #trying to connect to the network ports
        with socket.create_connection((str(scanIPAddress), port), timeout=1):
            return "Open"
    #executes if the network port refused to connect first
    except ConnectionRefusedError:
        # return the port status as Closed
        return "Closed"
    #executes if the network port timed out or system function returns a system-related error
    except (socket.timeout, OSError):
        # return the port status as Filtered
        return "Filtered"

#scanning the ip address in a network function
def scan_network(network):



    # initialize ports that needs to be scanned
    portlist = [22, 80, 443, 3389, 8080]

    # attempts to scan the network and save the results
    try:
        # open the text file in write more using UTF-8 encoding
        with open("scan_results.txt", "w", encoding="utf-8") as logFile:
            # loop through each usable IP address in the network
            for ipAddress in network.hosts():
                # convert the IP address into a string and format the output
                line = "IP Address: " + str(ipAddress)

                # prints the ip address in the terminal for the user to see
                print(line)
                # write the ip address in the text file on a new line
                logFile.write(line + "\n")

                # looping again through each port in the port list
                for port in portlist:
                    # getting the status of each of the ports in the network
                    status = scan_port(ipAddress, port)
                    # convert the statis into a string and format the output
                    line = "  Port " + str(port) + ": " + status
                    # prints the status of the port in the terminal for the user to see
                    print(line)
                    # write the status of the port in the text file on a new line
                    logFile.write(line + "\n")

        # prints to let the user know that the function has finish executing
        print("Scan finished. Results saved to scan_results.txt")

    # catches if the program returns a system-related error
    except OSError:
        print("Error: Could not save scan_results.txt")

    # catches if the user
    except KeyboardInterrupt:
        print("\nScan stopped by the user.")

# executes the main functions to control the program execution
def main():
    #getting the input for ip address
    network = get_input_ip()

    if network is not None:
        scan_network(network)

# check if the script is being executed directly
if __name__ == "__main__":

    #calls the main function to start the program
    main()
