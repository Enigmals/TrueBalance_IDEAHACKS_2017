import socket
import sys
import pickle
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('192.168.43.189', 80)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)

lineBuffer = ""
count = 0

startTime = 0 

timeData = []
vectorData = []

try: 
    while True:
        # Wait for a connection
        print('waiting for a connection...')
        connection, client_address = sock.accept()
        print('connection from %s:%d' % client_address)
        startTime = time.mktime(time.localtime())
        try:
            while True:
                # Receive the data one byte at a time          
                data = connection.recv(1)

                if data == '\n':
                    parsedData = lineBuffer.split()
                    print(parsedData)
                    vectorData.append(float(parsedData[1]))
                    timeData.append(float(parsedData[3])) 
                    lineBuffer = ""
                    count = count + 1
                else:
                    lineBuffer = lineBuffer + data              
                
                    #print "sizes:", len(timeData), len(vectorData)
                    
                    #parsedData.remove(parsedData[0])
                    #vectorData = vectorData[1:]
                    #timeData.remove(timeData[0])
                    #timeData = timeData[1:]
                    #count = count - 1

                if data:
                    continue
                    # Send back in uppercase
                    #connection.sendall(data.upper())
                else:
                    print('no more data, closing connection.')
                    break
        finally:
            # Clean up the connection
            connection.close()
except Exception as e:
    print('exiting: ' + e.message)
finally:
    with open('vectorDataL.txt', 'w') as f:
        f.write(str(startTime) + '\n')
        for s in vectorData:
            f.write(str(s) + '\n')
    with open('timeDataL.txt', 'w') as f:
        for s in timeData:
            f.write(str(s) + '\n')

    sock.shutdown(socket.SHUT_RDWR)
    sock.close()



