#!/bin/sh
echo "Content-Type: text/plain"
echo "Cache-Control: no-cache, must-revalidate"
echo "Expires: Sat, 26 Jul 1997 05:00:00 GMT"
echo

RELAY_CTRL=/sys/class/leds/tp-link:blue:relay/brightness
if [ -f '/sys/class/leds/i-konke:red:relay/brightness' ] ; then 
	RELAY_CTRL=/sys/class/leds/i-konke:red:relay/brightness
fi

case "$QUERY_STRING" in
 state) 
   case "`cat $RELAY_CTRL`" in
      0) echo "OFF"
         ;;
            1) echo "ON"
               ;;
                 esac
                  ;;
                   on) 
                     echo 1 > $RELAY_CTRL
                       echo OK
                        ;;
                         off) 
                           echo 0 > $RELAY_CTRL
                             echo OK
                              ;;
                              esac
                              
                              
