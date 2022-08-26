import os

class Config:

    def __init__(self):

        # environment variables
        self.env = 'dev'
        # directories
        self.project_path = os.path.join(os.getcwd())
        self.data_dir = 'data'
        self.download_dir = 'download'
        self.sample_dir = 'sample'

config = Config()
