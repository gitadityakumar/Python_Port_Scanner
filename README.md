# python_port_scanner
A tool for port scan
The code uses the socket module to perform a port scan on a given host. It defines a function called scan_port that takes in a host and a port number and attempts to connect to the specified port on the host. If the connection is successful, it returns True, otherwise it returns False.

The main function prompts the user to enter the host to scan, the start port and the end port. It then calls the scan_port function for each port in the given range and prints whether the port is open or closed.

This port scan tool can be useful for checking which ports are open on a given host, for example to see which services are running on the host or to identify potential security vulnerabilities.
