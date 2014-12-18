sudo python /home/pi/MyApp/UploadTempToYeelink/getTmp.py
curl --request POST --data-binary @"/home/pi/MyApp/UploadTempToYeelink/cpuTemp.txt" --header "U-ApiKey:45d551044008252bb4e299e4c34294a3" http://api.yeelink.net/v1.0/device/10401/sensor/16796/datapoints
curl --request POST --data-binary @"/home/pi/MyApp/UploadTempToYeelink/gpuTemp.txt" --header "U-ApiKey:45d551044008252bb4e299e4c34294a3" http://api.yeelink.net/v1.0/device/10401/sensor/16797/datapoints

