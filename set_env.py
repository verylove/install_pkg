import commands
import basicLogger
import os
import sh


installDir = "/Fablesoft/InsightView"
log = basicLogger.SelfLog(installDir+"/logs/environment.log").logger

# set the environment variable
print "make the dir"
cmd = "mkdir -p /Fablesoft/InsightView"
(com, output) = commands.getstatusoutput(cmd)
if com != 0:
    log.error(output)


def set_env():
    cmd = "cp -rf ./.insightview_profile /Fablesoft/InsightView/"
    (com, output) = commands.getstatusoutput(cmd)
    path = installDir+"/.insightview_profile"
    if com != 0:
        log.error(output)
    log.debug("configuration of install environment\n"+path+"\n")

    if os.path.exists(path):
        cmd = "sed -i s#^FBIV_HOME.*#FBIV_HOME="+installDir+"#g "+path
        (com, output) = commands.getstatusoutput(cmd)
        if com != 0:
            log.error(output)
        cmd = "cat "+path
        (com, output) = commands.getstatusoutput(cmd)
        if com != 0:
            log.error(output)

    path = "/root/.bashrc"
    log.debug(path)
    if os.path.exists(path):
        cmd = "cat "+path
        (com, out) = commands.getstatusoutput(cmd)
        if out.find("instightview_profile") == -1:
            cmd = "sed -i '$aFBIV_HOME=/Fablesoft/InsightView' "+path
            commands.getstatusoutput(cmd)
            cmd = "sed -i '$aexport FBIV_HOME' "+path
            commands.getstatusoutput(cmd)
            cmd = "sed -i '$aif [ -f ${FBIV_HOME}/.insightview_profile ]; then' "+path
            commands.getstatusoutput(cmd)
            cmd = "sed -i '$afi' "+path
            commands.getstatusoutput(cmd)
            cmd = "cat "+path
            commands.getstatusoutput(cmd)
            sh.src_env()        # shell method
        else:
            log.debug(path+"The file no changes are required\n")
            cmd = "cat "+path
            commands.getoutput(cmd)
        print "\n source ", path, " \n"

        path = "/root/.bash_profile"
        log.debug(path)
        if os.path.exists(path):
            cmd = "cat "+path
            output = commands.getoutput(cmd)
            if output.find("LANG=en_US.utf8") == -1:
                cmd = "sed -i '$aexport LANG=en_US.utf8' "+path
                commands.getoutput(cmd)

            print "\033[1;32;m", "modify file "+path
            cmd = "cat "+path
            commands.getoutput(cmd)
            print "\n"
            print "\n source ", path, "\n"

        print "\033[1;32;m", "[OK]----set environment-----------------------------------------------\n"
        log.debug("[OK]----set environment-----------------------------------------------\n")

set_env()
sh.src_env()