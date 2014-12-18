#!/bin/bash

# check network availability
HOME='/home/pi'
while true
do
    TIMEOUT=5
    SITE_TO_CHECK="www.163.com"
    RET_CODE=`curl -I -s --connect-timeout $TIMEOUT $SITE_TO_CHECK -w %{http_code} | tail -n1`
    if [ "x$RET_CODE" = "x200" ]; then
  echo "Network OK, will send mail..."
  break
    else
  echo "Network not ready, wait..."
  sleep 1s
    fi
done

# get the IP address of wlan0, e.g. "192.168.16.5"
ETH0_IP_ADDR=`ifconfig wlan0 | sed -n "2,2p" | awk '{print substr($2,1)}'`

# send the Email
echo "Current time: `date '+%F %T'`. Enjoy it" | mutt -s "IP Address of Raspberry Pi: $ETH0_IP_ADDR" fenghuayin860327@163.com
