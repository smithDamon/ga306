import maya.cmds as cmds

def createTurntable(rotDegrees):

    #Select the object you want rotated
    selected = cmds.ls(sl=1, sn = True, type ='transform')

    #how many degrees to rotate the object. change to any desired value
    #rotDegrees = 360

    #start and end time will be read from the timeline
    startTime = cmds.playbackOptions(query=True, minTime=True)
    endTime = cmds.playbackOptions(query=True, maxTime=True)
    
    for objectName in selected:
        cmds.cutKey( selected, time =(startTime, endTime), attribute='rotateY')
        cmds.setKeyframe(selected, time=startTime, attribute='rotateY', value=0)
        cmds.setKeyframe(selected, time=endTime, attribute='rotateY', value=rotDegrees)
        
createTurntable(360)