import logging
import logging.config
import otherMod

def main():
    """
    Based on http://docs.python.org/howto/logging.html#configuring-logging
    """
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger("exampleApp")

    logger.info("Program started")
    result = otherMod.add(3,4)
    logger.info("Done!")


if __name__ == "__main__":
    main()
