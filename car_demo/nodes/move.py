#!/usr/bin/env python3
import rospy
import time
from prius_msgs.msg import Control
from std_msgs.msg import String

rospy.init_node('navigate_ugv')
pub = rospy.Publisher('prius', Control, queue_size=20)

# def initialize(str):
# 		global str_msg
# 		str_msg = "" + str

# def callback(msg):
# 	initialize(msg)

# sub = rospy.Subscriber('prius', String , callback )

command = Control()
rospy.loginfo('start')
print("w : Forward\n a : Left \n s : Reverse \n d : Right")
for i in range(100) :
    
    current_key = str(input("Enter Letter: "))

    if(current_key == 'w'):
        command.shift_gears = Control.FORWARD
        command.throttle = 0.5
        command.brake =0.0
        command.steer= 0.0
        pub.publish(command)
    if(current_key == 's'):
        command.shift_gears = Control.REVERSE
        command.throttle = 1.0
        command.brake =0.0
        command.steer= 0.0
        pub.publish(command)
    if(current_key == 'a'):
        command.shift_gears = Control.FORWARD
        command.throttle = 0.5
        command.brake =0.0
        command.steer= 0.8
        pub.publish(command)
    if(current_key == 'd'):
        command.shift_gears = Control.FORWARD
        command.throttle = 0.5
        command.brake =0.0
        command.steer= -0.8
        pub.publish(command)
    if(current_key == 'f'):
        command.shift_gears = Control.NO_COMMAND
        command.throttle = 0.0
        command.brake =1.0
        command.steer= 0.0
        pub.publish(command)