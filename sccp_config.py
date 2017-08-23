import commands
import basicLogger
import os

basePath = "/Fablesoft/InsightView"
zkmyPath = "/conf/zookeeper.properties"
dataPath = "/conf/transferData.properties"
cmPath = "/conf/collectorMaster.properties"
zkotherPath = "/third/kafka_2.9.2-0.8.1.1/config/server.properties"
fdbPath = "/third/apache-tomcat-insightview/webapps/insightview/WEB-INF/classes/jdbc.properties"
fparamPath = "/third/apache-tomcat-insightview/webapps/insightview/WEB-INF/classes/systemParam.properties"
fzkmyPath = "/third/apache-tomcat-insightview/webapps/insightview/WEB-INF/classes/zookeeper.properties"
pmyPath = "/third/apache-tomcat-insightview/webapps/insightview/WEB-INF/classes/cas-server.properties"
log = basicLogger.SelfLog("/logs/install.logs").logger

zookeeperIp=['192.168.20.199','enable']
zookeeperPort=['2181','enable']
zookeeperDataDir=['./data','enable']
databaseIp=['192.168.20.199','enable']
databasePort=['3306','enable']
databaseUsername=['root','enable']
databasePassword=['root123','enable']
databaseSchema=['sccp','enable']
itilIp=['192.168.20.199','enable']
itilPort=['8080','enable']
portalIp=['192.168.20.199','enable']
portalPort=['8083','enable']
sccpIp=['192.168.20.199','enable']
sccpPort=['8088','enable']
kafkaIp=['192.168.20.199','enable']
kafkaPort=['2181','enable']


def address(ip_address, lineArr1):
    ip_address[0] = lineArr1[1]
    ip_address[1] = lineArr1[0]


f = open ('commonConf.ini')
lines = f.readlines()
f.close()
for line in lines:
    lineArr = line.strip('\n').split("__")
    print "["+lineArr[0]+"]--"+lineArr[1]+" \n"
    lineArr = lineArr[1].split("=")
    try:
        address(
            {
                "zookeeperIp": zookeeperIp,
                "zookeeperPort": zookeeperPort,
                "zookeeperDataDir": zookeeperDataDir,
                "databaseIp": databaseIp,
                "databasePort": databasePort,
                "databaseUsername": databaseUsername,
                "databasePassword": databasePassword,
                "databaseSchema": databaseSchema,
                "itilIp": itilIp,
                "itilPort": itilPort,
                "portalIp": portalIp,
                "portalPort": portalPort,
                "sccpIp": sccpIp,
                "sccpPort": sccpPort,
                "kafkaIp": kafkaIp,
                "kafkaPort": kafkaPort
                        }.get(lineArr[0]), lineArr)
    except TypeError:
        print "not match"


def config_zookeeper():
    path = basePath+zkmyPath
    print path+"\n"
    print "configuration of zookeeper \n"
    msg = "configuration of zookeeper \n"
    log.debug(msg)
    log.debug(path)

    if os.path.exists(path):
        cmd = "sed -i s/^zk.connect.*/zk.connect="+zookeeperIp[0]+":"+zookeeperPort[0]+"/g "+path
        commands.getoutput(cmd)
        cmd = "cat "+path
        output = commands.getoutput(cmd)
        log.debug(output)

    path = basePath+zkotherPath
    log.debug(path)
    if os.path.exists(path):
        cmd = "sed -i s/^zookeeper.connect=.*/zookeeper.connect="+zookeeperIp[0]+":"+zookeeperPort[0]+"/g "+path
        commands.getoutput(cmd)
        cmd = "sed -i s/^host.name.*/host.name="+zookeeperIp[0]+"/g "+path
        commands.getoutput(cmd)
        cmd = "sed -i s#^log.dirs.*#log.dirs="+zookeeperDataDir[0]+"/#g "+path
        commands.getoutput(cmd)
        cmd = "cat "+path
        output = commands.getoutput(cmd)
        log.debug(output)

    path = basePath + fzkmyPath
    log.debug(path)
    if os.path.exists(path):
        cmd = "sed -i s/^zk.connect.*/zk.connect=" + zookeeperIp[0] + ":" + zookeeperPort[0] + "/g " + path
        commands.getoutput(cmd)
        cmd = "cat " + path
        output = commands.getoutput(cmd)
        log.debug(output)


def config_collectMaster():
    path = basePath+cmPath
    print path+"\n"
    msg = "configuration of database\n"
    print msg
    log.debug(msg)
    if os.path.exists(path):
        cmd = "sed -i s/^jdbc.userName.*/jdbc.userName="+databaseUsername[0]+"/g "+path
        commands.getoutput(cmd)
        cmd = "sed -i s/^jdbc.password.*/jdbc.password="+databasePassword[0]+"/g "+path
        commands.getoutput(cmd)
        cmd = "sed -i s#//.*\?#//"+databaseIp[0]+":"+databasePort+"/"+databaseSchema[0]+"\?#g "+path
        commands.getoutput(cmd)
        cmd = "cat "+path
        output = commands.getoutput(cmd)
        log.debug(output)


def config_web():
    path = basePath+fparamPath
    print path+"\n"
    msg = "configuration of web\n"
    log.debug(msg)
    if os.path.exists(path):
        cmd = "sed -i s#^fileServerURL.*#fileServerURL=http://"+sccpIp[0]+":"+sccpPort[0]+"/FileBank/FileDir/#g "+path
        commands.getoutput(cmd)
        cmd = "sed -i s#^fileServerPath.*#fileServerPath=http://"+sccpIp[0]+":"+sccpPort[0]+"/FileBank/FileUpload\?fileDir=#g "+path
        commands.getoutput(cmd)
        cmd = "sed -i s#^mobileSoftwareLatestURL.*#mobileSoftwareLatestURL=http://"+sccpIp[0]+":"+sccpPort[0]+"/FileBank/FileDir=#g "+path
        commands.getoutput(cmd)
        cmd = "sed -i s#^rest.room3d.url.*#rest.room3d.url=http://"+sccpIp[0]+":"+sccpPort[0]+"/insightview#g "+path
        commands.getoutput(cmd)
        cmd = "sed -i s#^cmdb.host.*#cmdb.host=http://"+sccpIp[0]+":"+sccpPort[0]+"/insightview/rest/cmdb/monitor/SyncResAndOMapping#g "+path
        commands.getoutput(cmd)
        cmd = "sed -i s#^rest.resSychron.url.*#rest.resSychron.url=http://"+sccpIp[0]+":"+sccpPort[0]+"/insightview#g "+path
        commands.getoutput(cmd)
        cmd = "sed -i s#^rest.machineRoom.alarms.*#rest.machineRoom.alarms=http://"+sccpIp[0]+":"+sccpPort[0]+"/insightview/rest/monitor/alarm/alarmsOfRoom#g "+path
        commands.getoutput(cmd)
        cmd = "sed -i s#^rest.monitor.types.*#rest.monitor.types=http://"+sccpIp[0]+":"+sccpPort[0]+"/insightview/rest/monitor/alarm/monitorTypes#g "+path
        commands.getoutput(cmd)
        cmd = "sed -i s#^rest.backlog.url.*#rest.backlog.url=http://"+portalIp[0]+":"+portalPort[0]+"/insightviewPortal/rest/backlog#g "+path
        commands.getoutput(cmd)
        cmd = "sed -i s#^rest.bpmConsole.machingAlarm.*#rest.bpmConsole.machingAlarm=http://"+sccpIp[0]+":"+sccpPort[0]+"/insightview#g "+path
        commands.getoutput(cmd)
        cmd = "sed -i s#^fileDeleteServerPath.*#fileDeleteServerPath=http://"+sccpIp[0]+":"+sccpPort[0]+"/FileBank/FileDelete?fileDir=#g "+path
        commands.getoutput(cmd)
        cmd = "sed -i s#^rest.workflow.Alarm.*#rest.workflow.Alarm=http://"+itilIp[0]+":"+itilPort[0]+"/itil-app/workflow#g "+path
        commands.getoutput(cmd)
        cmd = "cat "+path
        output = commands.getoutput(cmd)
        log.debug(output)

    path = basePath+fdbPath
    log.debug(path)
    if os.path.exists(path):
        cmd = "sed -i s/^jdbc.username.*/jdbc.username="+databaseUsername[0]+"/g "+path
        commands.getoutput(cmd)
        cmd = "sed -i s/^jdbc.password.*/jdbc.password="+databasePassword[0]+"/g "+path
        commands.getoutput(cmd)
        cmd = "sed -i s#//.*\?#//"+databaseIp[0]+":"+databasePort[0]+"/"+databaseSchema[0]+"\?#g "+path
        commands.getoutput(cmd)
        cmd = "cat "+path
        output = commands.getoutput(cmd)
        log.debug(output)


def get_install_dir():
    path = "/root/.bashrc"
    f = open(path)
    lines = f.readlines()
    f.close()
    for line in lines:
        if "FBIV_HOME" in line :
            words = line.split("=")
            return words[1]


def main():
    commands.getoutput("chmod 777 *")
    temp = get_install_dir()
    print temp
    if temp:
        config_zookeeper()