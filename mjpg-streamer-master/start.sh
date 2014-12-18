export LD_LIBRARY_PATH=/home/pi/MyApp/mjpg-streamer-master/mjpg-streamer-experimental
/home/pi/MyApp/mjpg-streamer-master/mjpg-streamer-experimental/mjpg_streamer -i "input_raspicam.so -fps 15" -o "output_http.so -w ./www" 
