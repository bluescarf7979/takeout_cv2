#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id()+ "\t" + "I heard blue")

def listener():
    rospy.init_node('study_sub')
    rospy.Subscriber("cv_detection", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

