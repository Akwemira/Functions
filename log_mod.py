import logging

logging.basicConfig(level = logging.WARNING)# we set the level at debug
logger = logging.getLogger()# logger variable will retrieve all the debug message

logger.warning('This is a warning message')# don't name a file logging.py in this folder else this code will throw AttributeError