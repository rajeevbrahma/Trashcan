# Trashcan
In order to make the communication work between the Trashcan Hardware and mobile app, we will need to setup and configure the IBM IoT service as per our application needs. Follow along the steps given below to launch your IBM IoT service instance. If you do not yet have an IBM Id, this is the time to create one and get started.

Step 1: Locate the “IBM Internet of Things Platform” Service

Login to your IBM Bluemix account and locate the “IBM Internet of Things Platform” under catalog.

Step 2: Launch the Service

Click on the “IBM Internet of Things Platform” service icon to launch the service. Specify the service parameters for Space, App, Service Name and Selected Plan as shown below (on the right side panel), and click on “CREATE” button.
![alt-tag](https://github.com/rajeevbrahma/Trashcan/blob/master/screenshots/step2.png)
Note: The Space for the service refers to an IBM Bluemix space that you have to create separately from your Bluemix dashboard.

Once created, a welcome screen will be displayed for your newly launched service.
![alt-tag](https://github.com/rajeevbrahma/Trashcan/blob/master/screenshots/step2.1.png)

Step 3: Launch the service dashboard

Scroll down on the welcome page and you will be able to locate a button “Launch Dashboard” under the “Connect your devices” section.
![alt-tag](https://github.com/rajeevbrahma/Trashcan/blob/master/screenshots/step3.png)

Step 4: Access the device profiles page on the service dashboard

To use this service with IOT devices, we must create the device profiles first. As described in the “Overview” section, we have two devices, the virtual raspberry pi that interfaces with the IOTIFY trashcan simulator and the mobile app. So to facilitate communication between the two devices, we will create a device profile for each.
In the dashboard page, hover your mouse to left side menu to expand and bring it up.
![alt-tag](https://github.com/rajeevbrahma/Trashcan/blob/master/screenshots/step3.1.png)

Click on the “DEVICES” sub-menu to bring up the Device list page
![alt-tag](https://github.com/rajeevbrahma/Trashcan/blob/master/screenshots/step3.2.png)

And on the same page, click on “Device Types” tab to bring up the device types panel.
![alt-tag](https://github.com/rajeevbrahma/Trashcan/blob/master/screenshots/step3.3.png)

Step 5 : Create device profile for the trash can 

Click on the “Create Type” button on the top right corner of the page to add a new device profile. Follow the sequence of screenshots below to add a device type for the hardware underneath trash can.
![alt-tag](https://github.com/rajeevbrahma/Trashcan/blob/master/screenshots/step3.4.png)

Note: Make sure to select “Create device type” in the above step
![alt-tag](https://github.com/rajeevbrahma/Trashcan/blob/master/screenshots/step3.5.png)

Click on the “Next” button on the bottom right corner of the “Create Device Type” dialog to move through the steps. All the subsequent steps are optional and can be skipped. Finally, the device type will be created and listed under the “Device Types” tab panel.
![alt-tag](https://github.com/rajeevbrahma/Trashcan/blob/master/screenshots/step3.6.png)

Step 6: Create device profile for the mobile app

Now we can follow the same steps to create another device type in “IBM IoT Platform” for the mobile app.
![alt-tag](https://github.com/rajeevbrahma/Trashcan/blob/master/screenshots/step3.7.png)

At last, we will have the two device types listed as per our project requirement.
![alt-tag](https://github.com/rajeevbrahma/Trashcan/blob/master/screenshots/step3.8.png)

Step 7: Create device instances

We now have the device types defined in the service. The next thing is to define the actual device itself which acts as a virtual identifier (device id) for every device instance that is going to access the service. In our case, we have the raspberry pi and the mobile app as our two device instances.

So lets go ahead and add them by clicking on the “Add Device” button under the “Browse” tab of “Devices” section in the dashboard.
![alt-tag](https://github.com/rajeevbrahma/Trashcan/blob/master/screenshots/step3.9.png)
Lets create the device,by selecting a device type "Trashcan"
![alt-tag](https://github.com/rajeevbrahma/Trashcan/blob/master/screenshots/step3.10.png)
And,assign a unique name to the device,Device in this case.
![alt-tag](https://github.com/rajeevbrahma/Trashcan/blob/master/screenshots/step3.11.png)
Note: Just like in the case of adding device types, we can ignore the other steps in creating device and hit Next until we reach the end of “Add Device” dialog.

As part of the final step, we will be presented with the device credentials of this newly added device.
![alt-tag](https://github.com/rajeevbrahma/Trashcan/blob/master/screenshots/step3.12.png)
Similarly,let also create another device instance for the mobile app
![alt-tag](https://github.com/rajeevbrahma/Trashcan/blob/master/screenshots/step3.13.png)

![alt-tag](https://github.com/rajeevbrahma/Trashcan/blob/master/screenshots/step3.14.png)

![alt-tag](https://github.com/rajeevbrahma/Trashcan/blob/master/screenshots/step3.15.png)

We now have the devices also listed in the IBM IoT Platform service, and that concludes the device provisioning.
![alt-tag](https://github.com/rajeevbrahma/Trashcan/blob/master/screenshots/step3.16.png)

Note: Make a note of the Organization ID displayed in the "Your Device Credentials" Section of "Add Device" dialog.This will be required for programming the device SDKS

Step 8: Generate API Key and Auth Token

Now that all the devices are created , we need to generate the API key and auth token to access the IBM IOT service from our end point devices.

For this, go to the “APPS” sub-menu

![alt-tag](https://github.com/rajeevbrahma/Trashcan/blob/master/screenshots/step7.1.png)

Now,click on the "Generate API Key" button.
![alt-tag](https://github.com/rajeevbrahma/Trashcan/blob/master/screenshots/step7.2.png)

You will see the API key and Auth token being displayed on a dialog. Make a note of these parameters.

![alt-tag](https://github.com/rajeevbrahma/Trashcan/blob/master/screenshots/step7.4.png)

Click “Finish” on the lower right corner of the dalog to return back to the “API Keys” tab and you can now see your newly generated API credentials listed over there.

Note:Make sure that you make a note of the API key & authentication token displayed on the screen for your device instance. This token will be used to program the application software later

DEVICE SETUP
step 1: Power On the raspberry.
step 2: Clone this repository Trashcan

[Trashcan](https://github.com/rajeevbrahma/Trashcan.git)

step 3 : Install Dependency modules ibmiotf and twilio by doing

sudo pip install ibmiotf

sudo pip install twilio

Python Script Configuration

You will have to add some configuration settings to make the application work with IBM IoT platform service and Twilio messaging. These configurations are to be done as variables, which are already defined in the trash can's application code under[Trashcan.py](https://github.com/rajeevbrahma/Trashcan/blob/master/Trashcan.py)

Edit the variables in the following lines as follows
Variable name       Line no.           Description

      account_sid         23                 Twilio account SID

      auth_token          24                 Twilio account authToken

      twilionumber        28                 Twilio Number ( Your Twilio subscribed number)

      receivernumber      29                 Twilio verified number (where you want to receive the SMS notifications). 
                                             Should have country code, for example +18458892405

      organization        182                IBM account organization ID

      authKey             189                Generated API key

      authToken           190                Generated Authentication token
    
Mobile App Configuration

The IBM IoT platform configurations has to be done in the mobile app as well, since the mobile app is also registered as a device instance for receiving the readings published by the trash can.

Edit the line numbers in[index.js](https://github.com/rajeevbrahma/Trashcan/blob/master/TrashCanApp/www/js/index.js)

Variable Name        Line no.            Description

      org                  55                  IBM account organization ID

      auth-key             60                  Generated API key    

      auth-token           61                  Generated authentication token  
      
      
Steps to Build the Mobile App

For building the mobile app, please refer to the official Cordova & Android documentation to setup the build dependencies. You will have to setup a build system with the dependencies, primarily the NodeJS, Java and Ant among others.

Follow the steps below to build the APK file for the mobile app. All these steps are to be performed on the build system. These steps have been verified on a build system with Ubuntu mate OS along with Android version 23 & Cordova 6.3.0

Step 1: Clone this repository and run the following commands from within the repository to pull the submodules from https://github.com/ibm-watson-iot/iot-nodejs to get the nodejs sdk for the IBM IoT platform.

git submodule init
git submodule update

Step 2: Add the android platform by executing this command in the terminal under the app root folder ( TrashCanApp)

    cordova platform add android
Step 3: In the config.xml file in the root folder change the name of the app to the name you want. This is optional step. By default the app name is "Trash Can"

Step 4: Build the app by executing the following command in the terminal in the root folder of the cordova app

      cordova build android
Step 5: Once build is successful, you can find the generated apk file in the following path relative to the cordova project root directory.

    /platforms/android/build/outputs/apk
