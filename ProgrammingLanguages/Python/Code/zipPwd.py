import zipfile

zFile = zipfile.ZipFile('code.zip')

zFile.extractall(pwd='Welcome#123')
