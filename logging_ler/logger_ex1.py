import logging


class LoggerConsoleDemo:
    def test_log(self):
        # logger = logging.getLogger("demo_logger")
        logger = logging.getLogger(LoggerConsoleDemo.__name__)
        # logger.setLevel(logging.INFO)
        logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        # console_handler.setLevel(logging.INFO)
        console_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s',
                                      datefmt='%d/%m/%Y %I:%M:%S %p')
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # logger.debug('Debug Message')
        # logger.info('Info Message')
        # logger.warning('Warning Message')
        # logger.error('Error Message')
        # logger.critical('Critical Message')
        try:
            print(10/0)
        except Exception as e:
            logger.exception(e)


class LoggerFileDemo:
    def test_log(self):
        # logger = logging.getLogger('File_logger')
        logger = logging.getLogger(LoggerFileDemo.__name__)
        logger.setLevel(logging.DEBUG)
        # logger.setLevel(logging.ERROR)

        file_handler= logging.FileHandler('custom_logeer.log', mode='a')
        file_handler.setLevel(logging.DEBUG)
        # file_handler.setLevel(logging.CRITICAL)

        formatter = logging.Formatter('%(asctime)s - %(name)s : %(message)s', datefmt='%d-%m-%Y %I:%M:%S %p')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # logger.debug('Debug Message')
        # logger.info('Info Message')
        # logger.warning('Warning Message')
        # logger.error('Error Message')
        # logger.critical('Critical Message')

        try:
            # print(10/0)
            # print(int('ten'))
            # print(complex('ten+10'))
            # raise FileNotFoundError
            # raise FileExistsError
            raise NotImplementedError
        except Exception as e:
            logger.exception(e)


# demo = LoggerConsoleDemo()
demo = LoggerFileDemo()
demo.test_log()