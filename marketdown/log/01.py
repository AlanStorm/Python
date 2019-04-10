import logging

LOG_FORMAT = "%(asctime)s=====%(levelname)s=+++++%(message)s"

logging.basicConfig(level=logging.DEBUG, filename='text.log', format=LOG_FORMAT)

logging.debug('This is a debug log.')
logging.info('This is a debug info.')
logging.warning('This is a debug warning.')
logging.error('This is a debug error.')
logging.critical('This is a debug critical.')

# 另一种写法
logging.log(logging.DEBUG, 'This is a debug log.')
logging.log(logging.INFO, 'This is a debug info.')
logging.log(logging.WARNING, 'This is a debug warning.')
logging.log(logging.ERROR, 'This is a debug error.')
logging.log(logging.CRITICAL, 'This is a debug critical.')
