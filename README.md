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

Click on the “Next” button on the bottom right corner of the “Create Device Type” dialog to move through the steps. All the subsequent steps are optional and can be skipped. Finally, the device type will be created and listed under the “Device Types” tab panel.

Step 6: Create device profile for the mobile app

Now we can follow the same steps to create another device type in “IBM IoT Platform” for the mobile app.
At last, we will have the two device types listed as per our project requirement.

Step 7: Create device instances

We now have the device types defined in the service. The next thing is to define the actual device itself which acts as a virtual identifier (device id) for every device instance that is going to access the service. In our case, we have the raspberry pi and the mobile app as our two device instances.
So lets go ahead and add them by clicking on the “Add Device” button under the “Browse” tab of “Devices” section in the dashboard.

Lets create the device,by selecting a device type
