#!/usr/bin/python
#-*- coding: utf-8 -*-
from ftplib import FTP
import time
import tarfile
import os
import sys


from ftplib import FTP

def ftpconnect(host, port, username, password):
    ftp = FTP()
    # ftp.set_debuglevel(2)
    ftp.connect(host, int(port))
    ftp.login(username, password)
    return ftp

#从ftp下载文件
def downloadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

#从本地上传文件到ftp
def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

if __name__ == "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    # username = sys.argv[3]
    # password = sys.argv[4]
    localfilepath = sys.argv[3]
    remotefilename = sys.argv[4]
    ftp = ftpconnect(ip, port, "", "")
    uploadfile(ftp, localfilepath, remotefilename)
    ftp.quit()

