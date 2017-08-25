import basicLogger
import os
import commands

installDir = "/Fablesoft/InsightView"
log = basicLogger.SelfLog(installDir+"/logs/start.logs").logger


def start_options():
    msg = "\033[0;32;mPlease input the components which you want to install on this machine:\n" \
          "\033[0;31;m1 start All \n" \
          "2 stop Mysql\n" \
          "3 stop SCCP web\n" \
          "4 stop Zookeeper\n" \
          "5 stop Kafka\n" \
          "6 stop monitor\n" \
          "7 stop All\n" \
          "8 restart Mysql\n" \
          "9 restart SCCP web\n" \
          "10 restart Zookeeper" \
          "11 restart Kafka" \
          "12 restart monitor" \
          "13 restart collect server" \
          "14 restart control data" \
          "0 Quit" \
          "\n"
    print msg
    log.debug(msg)


def recursion():
    try:
        msg = "Input your choose number,multiple choose like this 3,4,5 \n "
        reply = raw_input("\033[1;33;40m" + msg)
        log.debug(reply)
        numbers = reply.split(",")
        numbers = [int(x) for x in reply]  # input is int
    except BaseException:
        print "\033[1;31;40m", "Please input the correct content"
        recursion()
    return numbers

def stop_zookeeper():
    commands.getoutput("sh /Fablesoft/InsightView/third/zookeeper-3.4.6/bin/zkServer.sh stop >> start.log")
    print "sh /Fablesoft/InsightView/third/zookeeper-3.4.6/bin/zkServer.sh stop\n"
    print "\033m[1;32;40m","[OK]----stop zkServer----------------------------------------------\n"
    print '\033[0m'


def stop_kafka():
    commands.getoutput("sh stop_kafka.sh >> start.log")
    print "sh stop_kafka.sh \n"
    print "\033m[1;32;40m","[OK]----stop kafka------------------------------------------------\n"


def start_mysql():
    print "sh start_mysql.sh \n";
    commands.getoutput("sh start_mysql.sh  >> start.log")


def start_web():
    print "sh start_web.sh >> start.log \n"
    commands.getoutput("sh start_web.sh >> start.log")
    print "\033m[1;32;40m","[OK]----start web------------------------------------------------\n"





def start():
    commands.getoutput("chmod 777 *")
    commands.getoutput("chmod 777 /Fablesoft/InsightView/bin/*")
    commands.getoutput("chmod 777 /Fablesoft/InsightView/third/apache-tomcat-insightview/bin/*")
