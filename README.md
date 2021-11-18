# priceisright

This is the companion micropython code to the public Edge Impulse project for Digits Recognition: https://studio.edgeimpulse.com/public/18079/latest, which can be deployed using the OpenMV library deployment option in Edge Impulse. 

This can be run on the Arduino Portenta H7 with Vision Shield (https://docs.edgeimpulse.com/docs/arduino-portenta-h7), or the OpenMV Cam H7 Plus (https://docs.edgeimpulse.com/docs/openmv-cam-h7-plus) using the OpenMV IDE. Copy the labels.txt and trained.tflite files to the mass storage drive that shows up when the device is connected to your host machine. 

The program prints out the number detected in the top most left hand corner, and there is a rolling tally for the price at the bottom. The top right number that is drawn is the index of the price, and it goes through each index for a few seconds at a time to trap the number that is detected. 
