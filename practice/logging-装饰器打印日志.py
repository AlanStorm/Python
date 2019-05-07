# import logging
#
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, filename='my.log')
#
# logging.debug('this is bug')
# logging.info('this is info')
# logging.warning('this is warning')
# logging.error('this is error')
# logging.critical('this is critical')
#
#
# # 装饰器
# # 使用装饰器，打印函数执行的时间
# import logging
#
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# logging.basicConfig(format=LOG_FORMAT)
#
#
# def log(func):
#     def wrapper(*args, **kwargs):
#         logging.error('this is error message')
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @log
# def test():
#     print('test done')
#
#
# test()
#
#
# 使用装饰器，根据不同的函数，传入的日志不相同
import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(format=LOG_FORMAT)

def log(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            logging.error(text)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log("test done")
def test():
    print('test done')


@log("main done")
def main():
    print('main done')


test()
main()
