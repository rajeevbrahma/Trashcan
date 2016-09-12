# MQTT
import ibmiotf.application
import time
import json

# External module imports                                                                                                        
import RPi.GPIO as GPIO

#logging module
import logging 

# twilio module
from twilio.rest import TwilioRestClient
from twilio import TwilioRestException

# datetime module
import datetime

LOG_FILENAME = 'Trashcanlogs.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG,format='%(asctime)s, %(levelname)s, %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


account_sid = "AC161d5213dce9632db6d2b6febdad21eb" # Enter your account sid 
auth_token  = "9ee4b0327f1e3d09b7a8928bb602ac9b"   # Enter your auth token


twilioClient = TwilioRestClient(account_sid, auth_token)

twilionumber = "+12512724152" # Your Twilio phone Number you will get it while registration
receivernumber = "+919738300498" #Your verified phone number


# Pin Definitons:                                                                                                                
TRIG = 24 # Broadcom pin 18 (P1 pin 12)                                                                                     
ECHO = 23 # Broadcom pin 23 (P1 pin 16)                                                                                   



'''****************************************************************************************
Function Name 	:	ultrasonicSensorInit()
Description		:	Function which initilizes the GPIO pins
Parameters 		:	-
****************************************************************************************'''

def ultrasonicSensorInit():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)
	GPIO.output(TRIG, False)

'''****************************************************************************************
Function Name 	:	distanceMeasurement()
Description		:	Function calculates the amount of waste in the trashcan and send it to the client
					and sends an alert message when trash can reaches the threshold
Parameters 		:	-
****************************************************************************************'''
currentCriticalLevelFlag = False
criticalLevelChangeOverFlag = False
distanceRecordedTime = 0
criticalLevelReachedTime = 0
currentDistance = 0
notificationSentTime = 0

LOOP_SAMPLING_TIME = 2
CRITICAL_DISTANCE = 50
NOTIFICATION_TIME_DELAY = 15



def distanceMeasurement():
	try:
		global client,deviceType,LOOP_SAMPLING_TIME,NOTIFICATION_TIME_DELAY,CRITICAL_DISTANCE,currentCriticalLevelFlag,criticalLevelChangeOverFlag,twilionumber,receivernumber
		l_prev_distance = 0
		ultrasonicSensorInit()

		deviceId = "App"
		deviceType = "Trashcan_app"
		messageBody = "Trashcan at xyz filled please come to pickup"
			
			
		while 1:

			time.sleep(LOOP_SAMPLING_TIME)		
			GPIO.output(TRIG, True)
			time.sleep(0.00001)
			GPIO.output(TRIG, False)
			#Starts the timer 
			while GPIO.input(ECHO)==0:
				pulse_start = time.time()
			#Waits for the timer to end once the pin is high
			while GPIO.input(ECHO)==1:
				pulse_end = time.time()

			pulse_duration = pulse_end - pulse_start

			l_distance = pulse_duration * 17150

			l_distance = round(l_distance, 2)
			
			currentDistance = l_distance
			distanceRecordedTime = datetime.datetime.now()

			message = {"ID":1,"distance":l_distance}
			print message
			try:
				# publishing the message to the Device called APP
				pubReturn = client.publishEvent(deviceType, deviceId, "status", "json", message)
				if pubReturn ==True:
					logging.info("The message successfully sent")
			except Exception  as e:
					logging.info("The sent message Failed")
					logging.error("The publishEvent exception httpcode :%s,message:%s,response:%s"(e.httpcode,e.message,e.response))
			

			if currentDistance < CRITICAL_DISTANCE:#6.1
				if currentCriticalLevelFlag == False:#6.1.1
					currentCriticalLevelFlag = True#6.1.1.2
					criticalLevelChangeOverFlag = True#6.1.1.3
					criticalLevelReachedTime = datetime.datetime.now()
				else:
					criticalLevelChangeOverFlag = False

			else:
				currentCriticalLevelFlag = False
				criticalLevelChangeOverFlag = False


			#This means that in this measurement loop , the changeover has happend 
			if criticalLevelChangeOverFlag == True:
				try:
					message = twilioClient.messages.create(body=messageBody,to=receivernumber,from_=twilionumber)	
				except TwilioRestException as e:
					logging.error("The exception in twilio %s,%s"(e,type(e)))	
				
				notificationSentTime = datetime.datetime.now()
			

			# This means that in this measurement loop the level stays at the critical level
			
			elif (currentCriticalLevelFlag == True):
				#calculate timedifference
				diff = distanceRecordedTime - notificationSentTime 

				day  = diff.days
				hour = (day*24 + diff.seconds/3600)
				diff_minutes = (diff.days *24*60)+(diff.seconds/60)			

				if diff_minutes > NOTIFICATION_TIME_DELAY:
					try:								
						message = twilioClient.messages.create(body=messageBody,to=receivernumber,from_=twilionumber)	
					except TwilioRestException as e:
						logging.error("The exception in twilio %s,%s"(e,type(e)))	
					

					notificationSentTime = datetime.datetime.now()
		
						
	except KeyboardInterrupt: 
		GPIO.cleanup()
	except Exception as e:
		logging.error("The distanceMeasurement exception is %s,%s"%(e,type(e)))	

	

'''****************************************************************************************
Function Name 	:	init()
Description		:	Function which connects to the ibmiotf service
Parameters 		:	-
****************************************************************************************'''

def init():
	global client,deviceType
	organization = "5q764p" #Your organization ID
	
	appId = "Device"   # The Device you've created and wants to connect with
	authMethod = "token" #Method of authentication (the only value currently supported is apikey)
	
	authKey = "a-5q764p-ps671tu3kb" #API key (required if auth-method is apikey).
	authToken = "CPW58F)?&gwsxeDBIn"#API key token (required if auth-method is apikey).
	
	deviceType = "Trashcan" # The Type of the device created in your organization 
	deviceId = "Device" # The Device you've created and wants to connect with                                                                                                       
	try:
		# options require for the connection
		options = {"org": organization, "id":deviceType, "auth-method": authMethod, "auth-key": authKey, "auth-token": authToken}
		client = ibmiotf.application.Client(options)
		client.connect()		
	except ibmiotf.connectionException as e:
		logging.error("The iotfconnection Exception is %s,%s"%(e,type(e)))	


if __name__ == '__main__':
	init()
	distanceMeasurement()		 