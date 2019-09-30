message = ['#', 'A', 'T', 'I', 'T', '\n']
buffered_message = [] #store the buffer
full_message = [] #read the message

def message_interpret_binary(read):
    temp_str = str(read[5]) #store first byte as a string
    opener = ''.join(map(bin, bytearray(temp_str, 'ascii')))  # join to an empty string '' and assign to opener
    opener_id = int(opener[2:])
    if opener_id == 1010: #1010 is linefeed in ascii
        print('this is an opening message')
    elif opener_id == 2:
        print('its an arduino')

for i in message:
    buffered_message.append(i)
    if i == '\n': #ASCII character 10, linebreak
        full_message = buffered_message
        buffered_message = [] #clear buffer
        message_interpret_binary(full_message)