#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Date   : 16/05/2017
# @User   : W.b
# @File   : change_package_name.py
# @Declare: 更改 Android 项目包名，也可以用于更改某些特定的字符串

import os
import time
from datetime import datetime


def main():
    print('开始更改---', datetime.fromtimestamp(time.time()))

    # 旧包名
    oldStr = 'xxxxxx'
    # 新包名
    newStr = 'xxxxxx'
    # 项目根目录
    dirPath = 'xxxxxx'
    # dirPath = '/Users/wb/Desktop/untitled folder/untitled folder 2'
    # 目录下的所有文件
    fileList = listFile(dirPath)
    # 以下文件不修改
    keywordList = ['.git', '.jks', '.class', 'libs', 'assets', '.apk', 'drawable', 'mipmap', '.gradle', 'gradlew']
    print('正在更改---')
    for file in fileList:
        if filter(file, keywordList):
            # print('修改... %s' % file)
            with open(file, 'r+', errors='ignore') as f:
                lines = f.readlines()
                # 不要让 python 记住执行到这里，从文件头开始
                f.seek(0)
                # 清空文件
                f.truncate()
                for line in lines:
                    f.write(line.replace(oldStr, newStr))

    print('完成更改---', datetime.fromtimestamp(time.time()))


# 遍历目录中所有文件
def listFile(dirPath):
    fileList = []
    for root, dirs, files in os.walk(dirPath):
        for file in files:
            fileList.append(os.path.join(root, file))
    return fileList


# 过滤不需要修改的文件
def filter(file, keywordList):
    for keyword in keywordList:
        if keyword in file:
            return False
    return True


if __name__ == '__main__':
    main()
