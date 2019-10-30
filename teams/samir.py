
"""
Demo the direct flying for the python interface
Author: Amy McGovern
"""
import os
from pyparrot.Minidrone import Mambo

# you will need to change this to the address of YOUR mambo
mamboAddr = os.environ.get(DRONE_ADDRESS)

# make my mambo object
# remember to set True/False for the wifi depending on if you are using the wifi or the BLE to connect
mambo = Mambo(mamboAddr, use_wifi=False)

print("trying to connect")
success = mambo.connect(num_retries=3)
print("connected: %s" % success)

if (success):
    # get the state information
    print("sleeping")
    mambo.smart_sleep(2)
    mambo.ask_for_state_update()
    mambo.smart_sleep(2)

    print("taking off!")
    mambo.safe_takeoff(5)

    print("Flying direct: going forward (positive pitch)")
    mambo.fly_direct(roll=0, pitch=100, yaw=0, vertical_movement=0, duration=2)

    print("Flying direct: going backwards (negative pitch)")
    mambo.fly_direct(roll=0, pitch=-200, yaw=0, vertical_movement=0, duration=2)

    print("Flying direct: going forward (positive pitch)")
    mambo.fly_direct(roll=0, pitch=100, yaw=0, vertical_movement=0, duration=2)

    print("Showing turning (in place) using turn_degrees")
    mambo.turn_degrees(180)
    mambo.smart_sleep(2)
    mambo.turn_degrees(-180)
    mambo.smart_sleep(2)

    print("Flying direct: going forward (positive pitch)")
    mambo.fly_direct(roll=0, pitch=100, yaw=0, vertical_movement=0, duration=2)

    print("Flying direct: going backwards (negative pitch)")
    mambo.fly_direct(roll=0, pitch=-200, yaw=0, vertical_movement=0, duration=2)

    print("Flying direct: going forward (positive pitch)")
    mambo.fly_direct(roll=0, pitch=100, yaw=0, vertical_movement=0, duration=2)

    print("flip back")
    print("flying state is %s" % mambo.sensors.flying_state)
    success = mambo.flip(direction="back")
    print("mambo flip result %s" % success)
    mambo.smart_sleep(5)

    #next

    print("Flying direct: going forward (positive pitch)")
    mambo.fly_direct(roll=0, pitch=100, yaw=0, vertical_movement=0, duration=2)

    print("Flying direct: going backwards (negative pitch)")
    mambo.fly_direct(roll=0, pitch=-200, yaw=0, vertical_movement=0, duration=2)

    print("Flying direct: going forward (positive pitch)")
    mambo.fly_direct(roll=0, pitch=100, yaw=0, vertical_movement=0, duration=2)

    print("Showing turning (in place) using turn_degrees")
    mambo.turn_degrees(-90)
    mambo.smart_sleep(2)
    mambo.turn_degrees(90)
    mambo.smart_sleep(2)

    print("Flying direct: going forward (positive pitch)")
    mambo.fly_direct(roll=0, pitch=100, yaw=0, vertical_movement=0, duration=2)

    print("Flying direct: going backwards (negative pitch)")
    mambo.fly_direct(roll=0, pitch=-200, yaw=0, vertical_movement=0, duration=2)

    print("Flying direct: going forward (positive pitch)")
    mambo.fly_direct(roll=0, pitch=100, yaw=0, vertical_movement=0, duration=2)

    print("flip back")
    print("flying state is %s" % bebop.sensors.flying_state)
    success = bebop.flip(direction="back")
    print("mambo flip result %s" % success)
    bebop.smart_sleep(5)

    #next

    print("Flying direct: going around in a circle (yes you can mix roll, pitch, yaw in one command!)")
    mambo.fly_direct(roll=100, pitch=0, yaw=200, vertical_movement=0, duration=5)

    print("landing")
    mambo.safe_land(5)
    mambo.smart_sleep(5)

    print("disconnect")
    mambo.disconnect()
