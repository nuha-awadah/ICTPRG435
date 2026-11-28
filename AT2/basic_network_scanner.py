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

    # catches if the user had typed in something on the keyboard to stop the scanning
    # useful to quickly test the program when scanning for a network range
    except KeyboardInterrupt:
        print("\nScan stopped by the user.")

# executes the main functions to control the program execution
def main():

    #getting the input for ip address
    network = get_input_ip()

    # checking if there are ip addresses before executing the function
    if network is not None:
        # passing the network list to the scanning function
        scan_network(network)

    print(f"\nID: 30148167, Initials:  NABMY")

# check if the script is being executed directly
if __name__ == "__main__":

    #calls the main function to start the program
    main()
