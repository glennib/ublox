import message

OLDBAUD = 9600
NEWBAUD = 4800

print "Setting NAV5 config to airborne mode..."
navconfig = message.UBXMessage('CFG-NAV5', "\x01\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
(ack, null) = message.send(navconfig, baudrate=OLDBAUD)
if ack:
    print "ACK: ", ack.emit()
else:
    print "Didn't get ACK."

print "\nSaving settings to flash..."
(ack, null) = message.send(message.UBXSaveConfig(), OLDBAUD)
if ack:
    print "ACK: ", ack.emit()
else:
    print "Didn't get ACK."
    
print "Verifying NAV settings..."
(settings, ack) = message.send(message.UBXPollNav5(), NEWBAUD)
print "New settings: ", settings.payload
