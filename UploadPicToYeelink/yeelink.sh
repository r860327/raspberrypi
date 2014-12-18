raspistill -w 320 -h 240 -o /home/pi/MyApp/UploadPicToYeelink/image.jpg
curl --request POST --data-binary @/home/pi/MyApp/UploadPicToYeelink/image.jpg --header "U-ApiKey: 45d551044008252bb4e299e4c34294a3" http://api.yeelink.net/v1.0/device/10401/sensor/16910/photos
