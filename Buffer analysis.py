# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

#create a buffer of a desired feature
def buffer_analysis():
    #objct to buffer
    buffered_object = "River"
    #output feature where the buffer will be stored 
    buffered_output_class = "buffer"
    #the distance you want the buffer to come out 
    buffered_distance = "10 Meters"
    #the side type of the buffer
    buffered_sideType = "FULL"
    #the end type of the buffer 
    buffered_endType = "ROUND"
    #buffer stlyle
    buffered_dissolve_type = "LIST"
    #buffered_dissolve_field = "usually distance field"
    arcpy.Buffer_analysis(buffered_object, buffered_output_class, buffered_distance, buffered_sideType, buffered_endType, buffered_dissolve_type)

# Set environment settings
env.workspace = "C:/Practice map/YOURGDB.gdb"

buffer_analysis()
