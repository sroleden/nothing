
import zipfile
import os
import sys
import logging
import subprocess
from config.config import config
import pandas as pd

# def unzip(source,destination):
#     with zipfile.ZipFile(source, 'r') as zip_ref:
#         zip_ref.extractall(destination)
# kaggle competitions download -c us-patent-phrase-to-phrase-matching
def download(name):
    # subprocess.check_call([sys.executable,"-m",'pip','install',package])
    subprocess.check_call(['kaggle','competitions','download','-c',name,'-p',os.path.join(config.project_path,config.data_dir,config.download_dir,name)])

def unzip(name):
    with zipfile.ZipFile(os.path.join(config.project_path,config.data_dir,config.download_dir,name,'{0}.zip'.format(name)), 'r') as zip_ref:
        zip_ref.extractall(os.path.join(config.project_path,config.data_dir,config.sample_dir
                                        ,name))


def read_csv(name):
    train_data = pd.read_csv(os.path.join(config.project_path,config.data_dir,config.sample_dir,name,'train.csv'))
    test_data = pd.read_csv(os.path.join(config.project_path,config.data_dir,config.sample_dir,name,'test.csv'))
    print('TRAIN SIZE \t: {}\nTEST SIZE \t: {}'.format(train_data.shape,test_data.shape))
    return train_data, test_data

if __name__ == '__main__':
    source = 'data/us-patent-phrase-to-phrase-matching.zip'
    destination = 'data'
    name = 'us-patent-phrase-to-phrase-matching'
    # download(name)

    # source = r'C:\projects\Kaggle_Projects\data\downloads\us-patent-phrase-to-phrase-matching\us-patent-phrase-to-phrase-matching.zip'
    # unzip(name)

    train, test = read_csv(name)
    print(train.shape)
    print(test.shape)

# kaggle competitions download -c us-patent-phrase-to-phrase-matching