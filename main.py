import serial
import rfid
import gpiozero

lock = gpiozero.LED(17) #lock is GPIO GP17, LED class must be used
rfid_permission_led = gpiozero.LED(18) #LED to flash if not authenticated

ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

while True:
    raw_data = ser.readline() #read serial port until a '\n' termination byte is recieved
    rfid_message = rfid.RFID(raw_data) #pass raw_data to new instance object 'rfid_message'
    if rfid_message.authentication_level == 1:
        #lock.on()
        #lock will unlock for 5 seconds
        print(raw_data)
        print('RFID: ' +str(rfid_message.l_to_st))
        print('Access Level ' + str(rfid_message.authentication_level) + ' granted!')
    elif len(raw_data) == 0: #if no data is present(timeout reached), do nothing.
        pass
    else:
        rfid_permission_led.blink(0.6, 0.4, 4) #blink on for 0.6seconds, off, for 0.4 seconds, blink 4 times
        print('No Access')
