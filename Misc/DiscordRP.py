from pypresence import Presence # This simple rich presence client in pypresence
import time
import random

wait_time = 120

Maybe = ['Confusion 100',
         'Becoming Mad',
         'Thinking Of A New Colour For A Username']
Doing = ['place holder1',
         'place holder2']
ThinkingAbout = ['place holder3',
                 'place holder4']
Is = ['place holder5']

client_id = "838857015844929576"  # Put your Client ID in here
RPC = Presence(client_id)  # Initialize the Presence client

RPC.connect() # Start the handshake loop

while True:  # The presence will stay on as long as the program is running
    RanVal = random.randrange(1, 3)
    if RanVal == 1:
        RPC.update(details="Maybe...",
        state=random.choice(Maybe),
        large_image="galatic_getaway",
        large_text="Test",
        start = int(time.time()),
        end = int(time.time()+wait_time),
        buttons = [{"label": "Press This If You Dare", "url": "https://tiny.one/doyoudare"}])

    elif RanVal == 2:
        RPC.update(details="Doing...",
        state=random.choice(Doing),
        large_image="galatic_getaway",
        large_text="Test",
        start = int(time.time()),
        end = int(time.time()+wait_time),
        buttons = [{"label": "Discord Web App", "url": "https://discord.com/app"}])

    time.sleep(wait_time) # Can only update rich presence every 2min seconds
