#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys

import roslib
roslib.load_manifest('ultraspeech')
import rospy

from ultraspeech.msg import Control, CurrentStim, SaveFile
from sensor_msgs.msg import CameraInfo

class Logger:
    def __init__(self):
        self.logfile = None
        self.runstatus = 0
        rospy.init_node("logger", anonymous=True)
        rospy.Subscriber("control", Control, self.control_cb)
        rospy.Subscriber("current_stimulus", CurrentStim, self.currentstim_cb)
        rospy.Subscriber("monocam/camera_info", CameraInfo, self.monocaminfo_cb)
        rospy.Subscriber("monocam/monocam_capture/save_name", SaveFile, self.monocamsave_cb)
        rospy.spin()
        
    def control_cb(self, data):
	timestamp = self.getTime(str(data.header.stamp.secs), str(data.header.stamp.nsecs))	
        self.runstatus = data.run
        directory = data.directory
        if self.logfile == None:
            logfilename = directory + '/logfile.txt'
            self.logfile = open(logfilename, 'w')
        self.logfile.write('topic:control,time:%s,run:%d,directory:%s\n' %(timestamp, self.runstatus, directory))    

    def currentstim_cb(self, data):
	timestamp = self.getTime(str(data.header.stamp.secs), str(data.header.stamp.nsecs))	
	stim = data.stimulus
	rep = data.rep
	batch = data.batch
	self.logfile.write('topic:currentstim,time:%s,stimulus:%s,rep:%d,batch:%d\n' %(timestamp, stim, rep, batch))
       
    def monocaminfo_cb(self, data):
        if self.runstatus == 1:
	    timestamp = self.getTime(str(data.header.stamp.secs), str(data.header.stamp.nsecs))
	    frame = data.header.seq
	    self.logfile.write('topic:monocaminfo,time:%s,frame:%d\n' %(timestamp, frame))
	else:
	  pass

    def monocamsave_cb(self, data):
	timestamp = self.getTime(str(data.header.stamp.secs), str(data.header.stamp.nsecs))
	filename = data.filepath
	self.logfile.write('topic:monocamsave,time:%s,filepath:%s\n' %(timestamp, filename))
	  
    def getTime(self, secs, nsecs):
	if len(nsecs) < 9:
	    while (len(nsecs) != 9):
		nsecs = '0' + nsecs
	return secs + '.' + nsecs
        
        
if __name__ == "__main__":
    Logger()
