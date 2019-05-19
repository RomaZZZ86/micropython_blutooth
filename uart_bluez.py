import pyb, time ,machine
from thread import Thread

class Bluez(object):
    def __init__(self, com):
        #self.repl = pyb.USB_VCP()

        self.uart = pyb.UART(com, 9600,bits=8, parity=None, stop=1,read_buf_len=15024,timeout=10)  # ,bits=8, parity=None, stop=1,read_buf_len=64
        #self.pin = pyb.Pin('X18', pyb.Pin.OUT_PP, pyb.Pin.PULL_NONE)
        #self.pin.low()
        self.data=None
        self.read_n='DATA'
        self.msgss=None
        #self.word=''
        tr1 = Thread(target=self.download)#, args=(self.data)
        tr1.start()


        # for c in str:
        #     self.uart.writechar(ord(c))
    def download(self):
      while True:
        #print(self.read_n)
        if self.uart.any():
            self.data = self.uart.read(self.uart.any())
            self.data=self.data.decode("utf-8")
            print(self.data)
            if self.data=="~dowload":
                print("DOWNLOAD")
                self.uart.write(b'~')

                if self.uart.any():
                    # start = pyb.millis()
                    # while pyb.elapsed_millis(start)<1000:
                    with open('main_i.py', 'wb') as file:
                        file.write("")


                while True:
                    if self.uart.any():
                        check = self.uart.read(self.uart.any())
                        check=int(check)
                        if check>0:
                            print(check)
                            self.uart.write(b'~')


                        # while True:
                        #     if self.uart.any():
                        #         df = self.uart.read(self.uart.any())
                        #         df = df.decode("utf-8")
                        #         self.word+=df
                        #         if self.word[len(self.word)-1]=='|':
                        #             self.word=self.word[:-1]
                        #             break
                        #
                        # print(self.word)
                        word = ''
                        count = 0
                        #index = 0

                        while True:
                          if self.uart.any():
                            df = self.uart.read(self.uart.any())
                            df = df.decode("utf-8")
                            word+=df
                            print(df)
                            if word[len(word) - 1] == '$':
                                word = word[:-1]
                                with open("main_i.py", "a") as file:
                                    file.write(word)
                                break
                            if count > 10:
                                # print(word)
                                with open("main_i.py", "a") as file:
                                    # file.write("%s\n" % word)
                                    file.write(word)
                                word = ''
                                count = 0
                            count += 1
                            #index += 1
                        print('THE END')






                        # start1 = pyb.millis()
                        # while pyb.elapsed_millis(start1) < 1000:
                        # if self.word :
                        #         with open("main_i.py", "w") as file:
                        #             file.write("%s\n" % self.word)


                        time.sleep(2)

                            #pin.low()
                            #self.pin.high()
                        machine.reset()
            if self.data == "Data":
                #print("Data")
                for st in self.read_n:
                    st = str(st)
                    byte = bytes(st + '|', 'utf-8')
                    self.uart.write(byte)

            else:
                return self.data


    def bluez_pp(self,*args):
        self.read_n=args

