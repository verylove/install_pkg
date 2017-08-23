import logging


class SelfLog:
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logfile = ""

    def __init__(self, file1):
        self.logfile = file1
        fh = logging.FileHandler(file1, mode='w')
        fh.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)



