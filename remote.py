from __future__ import print_function
import time
import pychromecast

def forward(time_diff):
    print("Forward " + time_diff)
    time = mc.status.current_time
    mc.seek(time + float(time_diff))

def backward(time_diff):
    print("Back " + time_diff)
    time = mc.status.current_time
    mc.seek(time - float(time_diff))

def print_help():
    print("h:\thelp")
    print("f x:\tforward x seconds")
    print("b x:\tbackstep x seconds")
    print("pause:\tpause")
    print("play:\tplay")
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
        elif command.startswith("b"):
            time = command.split()
            backward(time[1])
        elif command == "pause":
            mc.pause()
        elif command == "play":
            mc.play()
