from time import sleep

import bluetooth
from Menu import Menu

target_address = '00:21:13:03:E9:53'

# Create a Bluetooth socket
connect = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

try:
    # Attempt to connect (use port 1 by default)
    connect.connect((target_address, 1))
    print("Connected successfully!")
    menu = Menu(connect)
    menu.main()
except bluetooth.BluetoothError as e:
    print(f"Bluetooth connection failed: {e}")

finally:
    # Close the connection
    connect.close()
    print("Connection closed.")
