#!/usr/bin/env python
"""
SYNOPSIS

    python basic_network_scanner.py <targetIP or CIDR> <additional targetIP or CIDR> [additional targets ...]

DESCRIPTION

    The Basic Network Scanner is a command-line tool designed to scan
    single or multiple IPv4 addresses and CIDR ranges.

    The program attempts to establish TCP connections to the following
    network ports:

        22   - SSH
        80   - HTTP
        443  - HTTPS
        3389 - RDP
        8080 - Alternative HTTP

    The status of each port is reported as Open, Closed, or Filtered
    based on the connection result.

    The program validates user input, handles invalid IP addresses
    and network errors, and displays the scan results in the terminal.
    The results are also saved to a text file named scan_results.txt.

    This tool should only be used on authorized networks.

EXAMPLES

    Scan a single IP address:
        python basic_network_scanner.py 192.168.9.1

    Scan multiple IP addresses separated by [space]:
        python basic_network_scanner.py 192.168.9.1 192.168.9.2

    Scan a CIDR range:
        python basic_network_scanner.py 192.168.9.0/29

    Scan an individual IP address and a CIDR range separated by [space]:
        python basic_network_scanner.py 192.168.9.1 192.168.9.8/29

AUTHOR

    30148167@tafe.wa.edu.au

LICENSE

    This script is the exclusive and proprietary property of
    TiO2 Minerals Consultants Pty Ltd. It is only for use and
    distribution within the stated organisation and its
    undertakings.

VERSION

    $Id$

"""

import ipaddress
import socket
import sys

# get user input for IP address and input validation function
def get_input_ip():

    # checks if there are command line arguments
    if len(sys.argv) > 1:
        # FIX: stores all command-line arguments as a list
        targetips = sys.argv[1:]
    else:
        # if no IP address was provided
        print("Missing IP address or CIDR range.")
        # exit the program
        sys.exit(1)

    # FIX: initialize a list to store validated networks
    networks = []

    # FIX: loop through each IP address provided by the user
    for targetip in targetips:

        # check if the IP address is valid using a try-except block
        try:
            # converts the input into an IP network object
            network = ipaddress.ip_network(targetip, strict=False)

            # checks whether the address is IPv4
            if network.version != 4:
                # error message for the user
                print("Invalid IP address: IP address is not IPv4.")
                # exit the program
                sys.exit(1)

            # FIX: add the validated network to the list
            networks.append(network)

        # catches invalid IP addresses and CIDR ranges
        except ValueError:
            # error message for the user
            print("Invalid IP address or CIDR range.")
            # exit the program
            sys.exit(1)

    # FIX: return the list of validated network objects
    return networks

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

# scanning the IP addresses in a network function
def scan_network(networks):

    # initialize ports that need to be scanned
    portlist = [22, 80, 443, 3389, 8080]

    # attempts to scan the network and save the results
    try:
        # open the text file in write mode using UTF-8 encoding
        with open("scan_results.txt", "w", encoding="utf-8") as logFile:

            # FIX: loop through each validated network in the list
            for network in networks:

                # FIX: loop through each usable IP address in the network
                for ipAddress in network.hosts():

                    # convert the IP address into a string and format the output
                    line = "IP Address: " + str(ipAddress)
                    # prints the IP address in the terminal for the user to see
                    print(line)
                    # write the IP address in the text file on a new line
                    logFile.write(line + "\n")
                    # looping through each port in the port list
                    for port in portlist:
                        # getting the status of each port in the network
                        status = scan_port(ipAddress, port)
                        # convert the status into a string and format the output
                        line = "  Port " + str(port) + ": " + status
                        # prints the status of the port in the terminal
                        print(line)
                        # write the status of the port in the text file
                        logFile.write(line + "\n")

        # prints to let the user know that the function has finished executing
        print("Scan finished. Results saved to scan_results.txt")

    # catches if the program returns a system-related error
    except OSError:
        print("Error: Could not save scan_results.txt")

    # catches if the user stops the scanning using the keyboard
    except KeyboardInterrupt:
        print("\nScan stopped by the user.")

# executes the main functions to control the program execution
def main():

    #getting the input for ip address
    network = get_input_ip()

    # passing the network list to the scanning function
    scan_network(network)

    print(f"\nID: 30148167, Initials:  NABMY")

# check if the script is being executed directly
if __name__ == "__main__":

    #calls the main function to start the program
    main()
