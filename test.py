print('Hell World')

import zipfile

def unzip(source,destination):
    with zipfile.ZipFile(source, 'r') as zip_ref:
        zip_ref.extractall(destination)

if __name__ == '__main__':
    source = 'data/us-patent-phrase-to-phrase-matching.zip'
    destination = 'data'
    unzip(source,destination)
