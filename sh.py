import commands
import basicLogger


def src_env():
    cmd = "source /Fablesoft/InsightView/Fablesoft/InsightView/.insightview_profile"
    commands.getstatusoutput(cmd)
    cmd = "source /root/.bashrc"
    commands.getstatusoutput(cmd)
    cmd = "source /etc/profile"
    commands.getstatusoutput(cmd)
    cmd = "source /root/.bash_profile"
    commands.getstatusoutput(cmd)
    cmd = "env"
    output = commands.getoutput(cmd)
    basicLogger.logger.info("environment:\n"+output)