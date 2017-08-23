#!/bin/sh

cd /Fablesoft/InsightView/third/mysql
chmod 777 *
chmod 644 /Fablesoft/InsightView/third/mysql/my.cnf
#./stop.sh


PIDS=`ps -ef|grep mysql|awk '{print $2}'`
kill -9 $PIDS
echo kill mysql the PID = "${PIDS}"
