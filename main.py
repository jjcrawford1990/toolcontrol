import serial
import rfid
import gpiozero

#lock = gpiozero.LED(17) #lock is GPIO GP17, LED class must be used
#rfid_permission_led = gpiozero.LED(18) #LED to flash if not authenticated

#ser = serial.Serial(
#    port='/dev/serial0',
#    baudrate=9600,
#    parity=serial.PARITY_NONE,
#    stopbits=serial.STOPBITS_ONE,
#    bytesize=serial.EIGHTBITS,
#    timeout=1
#)

#while 1:
#    raw_data = ser.readline() #read serial port until a '\n' termination byte is recieved
raw_data = ['2', '02', '6B', '19', '5D', '1', '\n']
rfid_message = rfid.RFID(raw_data) #pass raw_data to new instance object 'rfid_message'
print(type(rfid_message))
if rfid_message.authenticate_access == 1:
    #lock.on()
    sleep(5) #lock will unlock for 5 seconds
    print('AUTHENTICATED')
else:
   # rfid_permission_led.blink(0.6, 0.4, 4) #blink on for 0.6seconds, off, for 0.4 seconds, blink 4 times
    print('No Access')

