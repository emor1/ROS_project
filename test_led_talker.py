#!/usr/bin/env python
import rospy
from std_msgs.msg import String
#import pigpio
rospy.init_node('keyctl')
pub=rospy.Publisher('ledswitch',String, queue_size=10)

while not rospy.is_shutdown():
	ctl=String()
	order=raw_input('o:on, f:off ')
	if 'o' in order:
		ctl='o'
	if 'f' in order:
		ctl='f'
	if 'q' in order:
		break


	print ctl
	pub.publish(ctl)

