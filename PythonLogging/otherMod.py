import logging

module_logger = logging.getLogger("exampleApp.otherMod")

def add(x,y):
    """"""
    logger = logging.getLogger("exampleApp.otherMod.add")
    logger.info("added %s and %s to get %s" %(x, y, x+y))
    return x+y
