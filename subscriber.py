#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback_function(data):
    #do something with the sent data from the publisher!
    
def publisher(): #Initialize node
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("topic_name", String, callback_function)
    rospy.spin()

if __name__ == '__main__':
    publisher()
