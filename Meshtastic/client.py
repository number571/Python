import time
from pubsub import pub
import meshtastic
import meshtastic.serial_interface

def on_receive_message(packet, interface):
    try:
        if 'decoded' in packet and packet['decoded']['portnum'] == 'TEXT_MESSAGE_APP':
            message_text = packet['decoded']['text']
            sender_id = packet['fromId']
            
            print(f"\n[{sender_id}]: {message_text}")
            print("> ", end="", flush=True)
    except Exception as e:
        print(f"Read error: {e}")

pub.subscribe(on_receive_message, "meshtastic.receive")

print("Connecting to Meshtastic...")

# interface = meshtastic.serial_interface.SerialInterface(devPath='/dev/ttyACM0')
interface = meshtastic.serial_interface.SerialInterface()

print("Stream listening...")

try:
    while True:
        user_input = input("> ")
        if user_input.strip():
            print(f"Sending...")

            # interface.sendText(text=user_input, channelIndex=1)
            # interface.sendText(text=user_input, destinationId="!2345678a")
            interface.sendText(text=user_input)
            
            print("The message was sent successfully!")
            
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nClosing...")
    interface.close()
