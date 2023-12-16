import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# )

# 创建一个文件处理器，用于将日志写入文件
file_handler = logging.FileHandler("log")
file_handler.setLevel(logging.INFO)

# 创建一个控制台处理器，用于将日志输出到控制台
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 创建一个日志记录器
logger = logging.getLogger('route_table')
logger.setLevel(logging.DEBUG)

# 创建日志格式化器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 将处理器添加到日志记录器
logger.addHandler(file_handler)
logger.addHandler(console_handler)