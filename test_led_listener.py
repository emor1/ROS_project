#!/usr/bin/env python
import rospy
from std_msgs.msg import String

import pigpio

pi = pigpio.pi()
pi.set_mode(16, pigpio.OUTPUT)#LED

def order(ctl):
	#rospy.loginfo(ctl)
	if 'o' == ctl.data:
		pi.write(16,1)
		rospy.loginfo('on')
	if 'f'== ctl.data:
		pi.write(16,0)
		rospy.loginfo('off')
#	else:
#		pi.write(16,1)
#		rospy.loginfo('fail')
rospy.init_node('listner')
sub=rospy.Subscriber('ledswitch',String,order)
rospy.spin()
