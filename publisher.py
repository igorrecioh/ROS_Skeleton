#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def function():
    pub = rospy.Publisher('topic_name', String, queue_size=10)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        #do something
        
        pub.publish(#publish a variable)
        rate.sleep()

if __name__ == '__main__':
    try:
        function()
    except rospy.ROSInterruptException:
        pass
