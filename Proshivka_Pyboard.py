
import bluetooth,time
import sys,struct
bd_addr = "20:16:05:12:05:13" #itade address

port = 1
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))
print('Connected')
sock.settimeout(2.0)

messeg=False
while True:
    sock.send(b'$')
    data = sock.recv(1)
    data=data.decode("utf-8")
    print(data)
    if data=='~':
        messeg = True
        break
data=None

if messeg :
    #mas=""

    # with open("main_py.py") as file:
    #     array = [row.strip('\n') for row in file]

    # with open('main_py.py') as f:
    #     for line in f:
    #sock.send(struct.pack('!I', len(line)))

    #sock.send(str(len(array)))
    sock.send(str(1))
    while sock.recv(1).decode("utf-8") !='~':pass
        # data = sock.recv(1)
        # data = data.decode("utf-8")
        # print(data)
        # if data == '~':break
            #print(line)
    print('LETS GO')
    # for line in array:
    #       line+="\n "
    #       sock.send(line)
    with open('main_py.py') as f:
        for line in f:
          sock.send(line)
          time.sleep(0.01)
          #while sock.recv(1).decode("utf-8") != '~': pass
    sock.send('$')





print('Firmware complete')
time.sleep(1)
try:
    print('____________________')
    dr="NONE"
    print("COMPLETE")
    sock.settimeout(3.0)
    while True:
            data = sock.recv(1)
            data=data.decode("utf-8")
            if data =='|' :break
            dr+=data
    print(dr)
except Exception as e:
    print(e)
sock.close()