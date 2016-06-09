{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf470
{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red64\green11\blue217;\red200\green20\blue201;\red46\green174\blue187;
\red180\green36\blue25;\red193\green101\blue28;}
\margl1440\margr1440\vieww10800\viewh13540\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs22 \cf2 \CocoaLigature0 #!/usr/bin/python\cf0 \
\
\cf2 # MIT License\cf0 \
\cf2 #\cf0 \
\cf2 # Copyright (c) 2016 Todd Klein\cf0 \
\cf2 #\cf0 \
\cf2 # Permission is hereby granted, free of charge, to any person obtaining a copy\cf0 \
\cf2 # of this software and associated documentation files (the "Software"), to deal\cf0 \
\cf2 # in the Software without restriction, including without limitation the rights\cf0 \
\cf2 # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\cf0 \
\cf2 # copies of the Software, and to permit persons to whom the Software is\cf0 \
\cf2 # furnished to do so, subject to the following conditions:\cf0 \
\cf2 #\cf0 \
\cf2 # The above copyright notice and this permission notice shall be included in all\cf0 \
\cf2 # copies or substantial portions of the Software.\cf0 \
\cf2 #\cf0 \
\cf2 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\cf0 \
\cf2 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\cf0 \
\cf2 # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\cf0 \
\cf2 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\cf0 \
\cf2 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\cf0 \
\cf2 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\cf0 \
\cf2 # SOFTWARE.\cf0 \
\
\cf2 # Import modules for CGI handling\cf0 \
\cf3 import\cf0  cgi, cgitb\
\cf3 import\cf0  datetime, time\
\
\cf4 print\cf0  \cf5 'Content-type: text/html\cf3 \\n\\n\cf5 '\cf0 ;\
\cf4 print\cf0  \cf5 'Status: 200 OK'\cf0 \
\
\cf2 # Create instance of FieldStorage\cf0 \
form = cgi.FieldStorage()\
\
\cf2 # Get data from fields\cf0 \
device = form.getvalue(\cf5 'device'\cf0 , \cf4 None\cf0 )\
deviceTime = form.getvalue(\cf5 'deviceTime'\cf0 , \cf4 None\cf0 )\
deviceName = form.getvalue(\cf5 'deviceName'\cf0 , \cf4 None\cf0 )\
system = form.getvalue(\cf5 'systemName'\cf0 , \cf4 None\cf0 )\
version = form.getvalue(\cf5 'systemVersion'\cf0 , \cf4 None\cf0 )\
model = form.getvalue(\cf5 'model'\cf0 , \cf4 None\cf0 )\
uuid = form.getvalue(\cf5 'uuid'\cf0 , \cf4 None\cf0 )\
appVersion = form.getvalue(\cf5 'appVersion'\cf0 , \cf4 None\cf0 )\
batteryLevel = form.getvalue(\cf5 'batteryLevel'\cf0 , \cf4 None\cf0 )\
latitude = form.getvalue(\cf5 'latitude'\cf0 , \cf4 None\cf0 )\
longitude = form.getvalue(\cf5 'longitude'\cf0 , \cf4 None\cf0 )\
autoMessage = form.getvalue(\cf5 'autoMessage'\cf0 , \cf4 None\cf0 )\
\
\cf2 # Open the file to store the data into\cf0 \
fileLog = \cf4 open\cf0 (\cf5 '/tmp/CollectYourData-iPhone'\cf0 , \cf5 'a'\cf0 )\
\
\cf2 # Get the local time on the machine and write to file\cf0 \
localtime = time.time();\
fileLog.write(\cf5 'timeReceived='\cf0  + \cf4 str\cf0 (localtime) + \cf5 '; '\cf0 );\
\
\cf2 # Write the device\cf0 \
\cf6 if\cf0  device != \cf4 None\cf0 :\
  fileLog.write(\cf5 'device='\cf0  + device + \cf5 '; '\cf0 );\
\
\cf2 # Write the device time\cf0 \
\cf6 if\cf0  deviceTime != \cf4 None\cf0 :\
  fileLog.write(\cf5 'deviceTime='\cf0  + deviceTime + \cf5 '; '\cf0 );\
\
\cf2 # Write the device name\cf0 \
\cf6 if\cf0  deviceName != \cf4 None\cf0 :\
  fileLog.write(\cf5 'deviceName='\cf0  + deviceName + \cf5 '; '\cf0 );\
\
\cf2 # Write the system\cf0 \
\cf6 if\cf0  system != \cf4 None\cf0 :\
  fileLog.write(\cf5 'system='\cf0  + system + \cf5 '; '\cf0 );\
\
\cf2 # Write the version\cf0 \
\cf6 if\cf0  version != \cf4 None\cf0 :\
  fileLog.write(\cf5 'version='\cf0  + version + \cf5 '; '\cf0 );\
\
\cf2 # Write the model\cf0 \
\cf6 if\cf0  model != \cf4 None\cf0 :\
  fileLog.write(\cf5 'model='\cf0  + model + \cf5 '; '\cf0 );\
\
\cf2 # Write the UUID\cf0 \
\cf6 if\cf0  uuid != \cf4 None\cf0 :\
  fileLog.write(\cf5 'uuid='\cf0  + uuid + \cf5 '; '\cf0 );\
\
\cf2 # Write the application version\cf0 \
\cf6 if\cf0  appVersion!= \cf4 None\cf0 :\
  fileLog.write(\cf5 'appVersion='\cf0  + appVersion + \cf5 '; '\cf0 );\
\
\cf2 # Write the battery level\cf0 \
\cf6 if\cf0  batteryLevel != \cf4 None\cf0 :\
  fileLog.write(\cf5 'batteryLevel='\cf0  + batteryLevel + \cf5 '; '\cf0 );\
\
\cf2 # Write the latitude coordinate\cf0 \
\cf6 if\cf0  latitude != \cf4 None\cf0 :\
  fileLog.write(\cf5 'latitude='\cf0  + latitude + \cf5 '; '\cf0 );\
\
\cf2 # Write the longitude coordinate\cf0 \
\cf6 if\cf0  longitude != \cf4 None\cf0 :\
  fileLog.write(\cf5 'longitude='\cf0  + longitude + \cf5 ';'\cf0 );\
\
\cf2 # Write the true/false if the message was auto\cf0 \
\cf6 if\cf0  autoMessage!= \cf4 None\cf0 :\
  fileLog.write(\cf5 'autoMessage='\cf0  + autoMessage + \cf5 ';'\cf0 );\
\
fileLog.write(\cf5 '\cf3 \\n\cf5 '\cf0 );\
fileLog.close}