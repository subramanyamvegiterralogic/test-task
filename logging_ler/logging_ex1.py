import logging
# from logging_ler import student
logging.basicConfig(filename='logging_ler1.txt',
                    level=logging.DEBUG,
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    datefmt='%d-%m-%Y %I:%M:%S %p')
# logging.basicConfig(filename='logging_ler1.txt')
def write_test_logs():
    print('logging Demo')
    logging.debug('Debug')
    logging.info('Info')
    logging.warning('Warning')
    logging.error('Error')
    logging.critical('Critical')

def write_exception():
    try:
        print(10/0)
    except Exception as e:
        logging.exception(e)
write_exception()