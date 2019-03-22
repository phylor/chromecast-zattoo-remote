from __future__ import print_function
import datetime
import time
import pychromecast

def forward(time_diff):
    print("Forward " + time_diff)

    if time_diff.endswith("m"):
        time_diff = float(time_diff.replace("m", "")) * 60

    time = mc.status.current_time
    mc.seek(time + float(time_diff))

def backward(time_diff):
    print("Back " + time_diff)

    if time_diff.endswith("m"):
        time_diff = float(time_diff.replace("m", "")) * 60

    time = mc.status.current_time
    mc.seek(time - float(time_diff))

def status():
    print(str(datetime.timedelta(seconds=mc.status.current_time)))

def print_help():
    print("h:\thelp")
    print("f x:\tforward x seconds")
    print("b x:\tbackstep x seconds")
    print("pause:\tpause")
    print("play:\tplay")
    print("status:\tshows current time")
    print("q:\tquit")

chromecasts = pychromecast.get_chromecasts()

if len(chromecasts) == 1:
    cast = chromecasts[0]
    cast.wait()
    print(cast.device.friendly_name)

    mc = cast.media_controller
    mc.block_until_active()

    while True:
        command = input("> ")

        if command == "q":
            break
        elif command == "h":
            print_help()
        elif command.startswith("f"):
            time = command.split()
            forward(time[1])
            status()
        elif command.startswith("b"):
            time = command.split()
            backward(time[1])
            status()
        elif command == "pause":
            mc.pause()
        elif command == "play":
            mc.play()
        elif command == "status":
            status()
