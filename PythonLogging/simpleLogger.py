import logging

# level : DEBUG -> INFO -> WARNING -> ERROR -> CRITICAL
# add filemode="w" to overwrite
logging.basicConfig(filename="sample.log", level=logging.INFO)

logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happeneed!")


# getLogger() method : used to dealing with multiple loggers in on application
# return a logger object(name : ex)
log = logging.getLogger("ex")

try:
    raise RuntimeError
except RuntimeError:
    log.exception("Error!")
