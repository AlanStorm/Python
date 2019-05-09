# 用logging的四大组件来实现日志的功能
# 打印出函数执行的时间，日志的等级，日志的消息
# 用装饰器
# 不同的体质，要记录不同等级的日志消息
import logging

logger = logging.getLogger("my_logger")

logger.setLevel(logging.DEBUG)

# handler
# TimeRotationFileHandler 是用来按照如期区划分日志
# RotationFileHandler 是按照日志文件的大小划分日志
debug_handel = logging.FileHandler("1024debug.log")
debug_handel.setLevel(logging.DEBUG)
debug_handel.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

error_handel = logging.FileHandler("1024error.log")
error_handel.setLevel(logging.ERROR)
error_handel.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

logger.addHandler(debug_handel)
logger.addHandler(error_handel)


# def log(func):
#     def wrapper(*args, **kwargs):
#         logger.debug('this is a debugger info')
#         logger.error('this is a error info')
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
# 按照函数的不同，要在日志中打印出不同的东西
def log_higher(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            logger.debug(text)
            logger.error(text)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log_higher('test done')
def test():
    print('test done')


@log_higher('main done')
def main():
    print('main done')


test()
main()
# 一般情况我们在实际的工作当中，我们经常吧logging封装称一个装饰器，按照我们自己的习惯，
# 我是习惯新建一个loggerTools的文件，在需要保存日志的地方，吧loggerTools给引进进来
