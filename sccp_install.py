# -*- coding: UTF-8 -*-

import commands
import basicLogger
import os
import sh

installDir = "/Fablesoft/InsightView"
log = basicLogger.SelfLog("/logs/install.logs").logger


def install_options():
    msg = "\033[0;32;mPlease input the components which you want to install on this machine:\n" \
          "\033[0;31;m1 Install All with portal\n" \
          "2 Base Package\n" \
          "3 Mysql and Script\n" \
          "4 Tomcat\n" \
          "5 Zookeeper and Kafka\n" \
          "6 SCCP web\n" \
          "7 collect Server 采集\n" \
          "8 Platform Server 控制\n" \
          "9 Install All without portal\n" \
          "0 Quit" \
          "\n"
    print msg
    log.debug(msg)


packageVersion = ["v5.0.0_20170425", "enable"]
f = open('commonConf.ini')
lines = f.readlines()
for line in lines:
    lineArr = line.strip('\n').split("__")
    print "["+lineArr[0]+"]--"+lineArr[1]+" \n "
    lineArr = lineArr[1].split("=")
    if lineArr[0] == "packageVersion":
        packageVersion[0] = lineArr[1]
        packageVersion[1] = lineArr[0]
    print "\n"
f.close()

def chkBaseEnv():
    cmd = "which java"
    out = commands.getoutput(cmd)
    if out == '/Fablesoft/InsightView/third/jdk1.7.0_45/bin/java':
        return 1
    return -1

def install_base():
    flag = chkBaseEnv()
    log.debug("\n chchkBaseEnv=")+flag+" \n"
    if flag == 1:
        basePack = "Fable_insightview_v5.0.0_Linux_X64_env.tgz"
        cmd = "tar -zxvf "+basePack+"-C "+installDir
        commands.getoutput(cmd)


def install_base_mysql():
    basePack = "Fable_insightview_v5.0.0_Linux_X64_env_with_mysql.tgz"
    cmd = "tar -zxvf"+basePack+" -C "+installDir
    commands.getoutput(cmd)


def install_tomcat():
    basePack = "Fable_insightview_v5.0.0_WebappServer_env.tgz "
    cmd =  "tar -zxvf "+basePack+" -C "+installDir
    commands.getoutput(cmd)


def install_zk_kafka():
    basePack = "Fable_insightview_v5.0.0_PlatformServer_env.tgz "
    cmd = "tar -zxvf "+basePack+" -C "+installDir
    commands.getoutput(cmd)

    basePackSuffix = "_release.tgz"
    basePackPrefix4 = "Fable_insightview_SCCP_v5.0.0_FullConf_"
    verArr = packageVersion[0].split("_")
    basePack4 = basePackPrefix4+verArr[1]+basePackSuffix
    cmd = "tar -zxvf "+basePack4+" -C "+installDir
    commands.getoutput(cmd)


def install_biz():
    basePackPrefix1 = "Fable_insightview_SCCP_webapppServer_"
    basePackPrefix2 = "Fable_insightview_SCCP_collectServer_"
    basePackPrefix3 = "Fable_insightview_SCCP_platformServer_"
    basePackSuffix = "_release.tgz"
    basePack1 = basePackPrefix1+packageVersion[0]+basePackSuffix
    basePack2 = basePackPrefix2+packageVersion[0]+basePackSuffix
    basePack3 = basePackPrefix3+packageVersion[0]+basePackSuffix
    cmd = "tar -zxvf "+basePack1+"-C "+installDir
    commands.getoutput(cmd)
    cmd = "tar -zxvf "+basePack2+"-C "+installDir
    commands.getoutput(cmd)
    cmd = "tar -zxvf "+basePack3+"-C "+installDir
    commands.getoutput(cmd)


def install_sccp():
    print "Input sccp upgrade version:"+packageVersion[0]
    basePackPrefix = "Fable_insightview_SCCP_webapppServer_"
    basePackSuffix = "_release.taz"
    basePack = basePackPrefix+packageVersion[0]+basePackSuffix
    cmd = "tar -zxvf "+basePack+"-C "+installDir
    print cmd
    commands.getoutput(cmd)


def install_collectorServer():
    print "Input collectorServer upgrade version:"+packageVersion[0]
    basePackPrefix = "Fable_insightview_SCCP_collectServer_"
    basePackSuffix = "_release.tgz"
    basePack = basePackPrefix+packageVersion[0]+basePackSuffix
    cmd = "tar -zxvf "+basePack+"-C "+installDir
    print cmd+"\n"
    commands.getoutput(cmd)

    basePackPrefix4 = "Fable_insightview_SCCP_v5.0.0_FullConf_"
    verArr = packageVersion[0].split("_")
    basePack4 = basePackPrefix4+verArr[1]+basePackSuffix
    cmd = "tar -zxvf "+basePack4+"-C "+installDir
    commands.getoutput(cmd)

# SCCP Platform
def install_controlData():
    print "Input controlData upgrade version:"+packageVersion[0]
    basePackPrefix = "Fable_insightview_SCCP_platformServer_"
    basePackSuffix = "_release.tgz"
    basePack = basePackPrefix+packageVersion[0]+basePackSuffix
    cmd = "tar -zxvf "+basePack+"-C "+installDir
    commands.getoutput(cmd)

    basePackPrefix4 = "Fable_insightview_SCCP_v5.0.0_FullConf_"
    verArr = packageVersion[0].split("_")
    basePack4 = basePackPrefix4+verArr[1]+basePackSuffix
    cmd = "tar -zxvf"+basePack4+"-C "+installDir
    commands.getoutput(cmd)


def install_all():
    install_base_mysql()
    install_tomcat()
    install_zk_kafka()
    install_biz()


def case_0():
    os._exit(0)
    print '\033[0m'


def case_1():
    install_all()
    commands.getoutput("sh start_mysql.sh")
    commands.getoutput("sh fableOMupgrade.sh")
    commands.getoutput("python sccp_config.py")
    commands.getoutput("python sccp_start.py")
    print '\033[0m'


def case_2():
    install_base()
    install_base_mysql()


def case_3():
    commands.getoutput("sh stop_mysql.sh")
    commands.getoutput("sh start_mysql.sh")
    commands.getoutput("sh fableOMupgrade.sh")


def case_4():
    install_tomcat()


def case_5():
    install_zk_kafka()


def case_6():
    install_sccp()


def case_7():
    install_collectorServer()


def case_8():
    install_controlData()


def case_9():
    commands.getoutput("sh start_mysql.sh")
    commands.getoutput("sh fableOMupgrade.sh")
    commands.getoutput("python sccp_config_without_portal.py")
    commands.getoutput("python sccp_start.py")


def error():
    print "\033[1;31;40m", "Incorrectly content"


# 递归调用，避免输入非法字符
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


def main():
    commands.getoutput("chmod 777 *")
    install_options()
    for x in recursion():
        case_install = {
            0: case_0,
            1: case_1,
            2: case_2,
            3: case_3,
            4: case_4,
            5: case_5,
            6: case_6,
            7: case_7,
            8: case_8,
            9: case_9,
            None: error
        }
        case_install.get(x, case_install[None])()

main()
