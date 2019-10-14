import logging

def logging_operation(message):
    try:
        logging.basicConfig(filename='exception.log', format='%(asctime)s %(message)s', filemode='a')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.error(message)
    except Exception as e:
        print(e)
