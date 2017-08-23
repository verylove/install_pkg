import os



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
    # print ip_address
    # print lineArr
    ip_address[0] = lineArr1[1]
    ip_address[1] = lineArr1[0]


f = open('commonConf.ini')
lines = f.readlines()
for line in lines:
    lineArr = line.strip('\n').split("__")
    #print "["+lineArr[0]+"]--"+lineArr[1]+" \n"
    lineArr = lineArr[1].split("=")
    # print lineArr[0]
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

    # {
    #      address
    #
    # }.get(lineArr[0], None)(
    #     {
    #         "zookeeperIp": zookeeperIp,
    #         None: lineArr
    #                         }.get(lineArr[0], None), lineArr)

print zookeeperIp

