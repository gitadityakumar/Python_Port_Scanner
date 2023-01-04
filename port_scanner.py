import socket

def scan_port(host, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(1)
  try:
    s.connect((host, port))
    return True
  except:
    return False
  finally:
    s.close()

def main():
  host = input("Enter the host to scan: ")
  start_port = int(input("Enter the start port: "))
  end_port = int(input("Enter the end port: "))

  for port in range(start_port, end_port+1):
    if scan_port(host, port):
      print("Port {} is open".format(port))
    else:
      print("Port {} is closed".format(port))

if __name__ == "__main__":
  main()
