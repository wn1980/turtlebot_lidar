#!/usr/bin/env python

import rospy

from dialogflow_ros.srv import DialogflowService

def cmd():
	rospy.wait_for_service('voice_cmd')
		
	try:
		voice_cmd = rospy.ServiceProxy('voice_cmd', DialogflowService, persistent=True)
		results = voice_cmd()
		
		if results.success:
			return results.result.action, results.result.query_text, results.result.fulfillment_text
			
	except rospy.ServiceException, e:
		print "Service call failed: %s"%e
		return None
	
	return None

def say(s):
	rospy.wait_for_service('speak')
		
	try:
		speak = rospy.ServiceProxy('speak', DialogflowService, persistent=True)
		results = speak(True, s)
		
		if results.success:
			return True
			
	except rospy.ServiceException, e:
		print "Service call failed: %s"%e
		return False
	
	return False

if __name__ == "__main__":
	r = cmd()
	
	if r is not None:
		#print(r)
		a, q, f = r[0], r[1], r[2]
		print(f)
		say(f)
