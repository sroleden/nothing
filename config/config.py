import os
import datetime
import time
class Config:

    def __init__(self):

        _now = datetime.datetime.now()

        # environment variables
        self.env = 'dev'
        # directories
        self.project_path = os.path.join(os.getcwd())
        self.data_dir = 'data'
        self.download_dir = 'download'
        self.sample_dir = 'sample'
        self.log_dir = 'logs'
        self.log_name = "log_{0}.log".format(_now.strftime("%Y-%m-%d"))

        # logging formatter
        self.stream_fomatter = '%(asctime)-15s %(levelname)-8s %(filename)s:%(lineno)s %(message)s'
        self.file_fomatter = "{'time':'%(asctime)s', 'name': '%(name)s', 'level': '%(levelname)s', 'message': '%(message)s'}"



config = Config()
