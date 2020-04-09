import socket
import pyautogui

size = pyautogui.size()
# prevMousePos = pyautogui.position()[0] / size[0], pyautogui.position()[1] / size[1]
# mousePos = pyautogui.position()[0] / size[0], pyautogui.position()[1] / size[1]

UDP_IP  = '255.255.255.255'

# UDP_IP = '127.0.0.1'
UDP_PORT = 5005
# MESSAGE = "Hello, World!".encode('utf-8')

# print ("UDP target IP:", UDP_IP)
# print ("UDP target port:", UDP_PORT)
# print ("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

i = 0
while True:
    if i % 10 == 0:
        continue

    mousePos = pyautogui.position()[0] / size[0], pyautogui.position()[1] / size[1]
    mouseStr = 'pos' + ' ' + str(mousePos[0]) + ' ' + str(mousePos[1])
    data = mouseStr.encode('utf-8')

    # if mousePos != prevMousePos:
    sock.sendto(data, (UDP_IP, UDP_PORT))
        # prevMousePos = mousePos
    # print (mouseStr.split(" ")[1]

    # # Exit condition
    # if mousePos[0] < 0.05 and mousePos[1] < 0.05:
    #     break

    i += 1

