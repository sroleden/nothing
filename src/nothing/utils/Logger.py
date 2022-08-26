
# -*- coding: utf-8 -*-
import logging
import os

from config.config import config

class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]



# python 3 style
class Logger(object, metaclass=SingletonType):
    # __metaclass__ = SingletonType   # python 2 Style
    _logger = None

    def __init__(self,name):
        self._logger = logging.getLogger(name)
        self._logger.setLevel(logging.INFO)

        streamHandler=logging.StreamHandler()

        streamFormatter=logging.Formatter(config.stream_fomatter)

        fileFormatter=logging.Formatter(config.file_fomatter)

        self.create_log_dir()

        fileHandler = logging.FileHandler(os.path.join(config.project_path,config.log_dir,config.log_name))


        fileHandler.setFormatter(fileFormatter)
        streamHandler.setFormatter(streamFormatter)

        self._logger.addHandler(fileHandler)
        self._logger.addHandler(streamHandler)

        print("Generate new instance")

    @property
    def logger(self):
        return self._logger

    @logger.setter
    def logger(self,name):
        self._logger = logging.getLogger(name)

    # TODO : complete this function
    @property
    def level(self):
        pass

    # TODO : handle this function with enumerate
    @level.setter
    def level(self,level):

        if level == 'info':
            self._logger.setLevel(logging.INFO)
        if level == 'debug':
            self._logger.setLevel(logging.DEBUG)

    def create_log_dir(self):
        path = os.path.join(config.project_path,config.log_dir)

        if not os.path.isdir(path):
            os.mkdir(path)