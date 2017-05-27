## 一行代码实现更改 Android 项目包名。

有时候难免会遇到奇葩需求，比如：更改包名。于是这个用 Python 编写的脚本应运而生，主要用途就是更改 Android 项目的包名。

这个也是近期学习 Python 之后写的一个小东西。

笔者使用环境：

- macOs Sierra

- Python3

使用方法：

- 拷贝文件 change_package_name.py 到项目的根目录

- Terminal cd xxx(项目的根目录)

- 运行 Python 命令：python3 change_package_name.py

- 更改完成

## 实现思路
遍历项目中的所有文件，匹配出需要更改的字符串，然后更改，过滤一些不需要更改的文件

#### 1. 遍历目录得到所有的文件

```
def listFile(dirPath):
    fileList = []
    for root, dirs, files in os.walk(dirPath):
        for file in files:
            fileList.append(os.path.join(root, file))
    return fileList
```

#### 2. 过滤不需要修改的文件，比如图片、libs、class 等

完整的过滤关键词

```
keywordList = ['.git', '.jks', '.class', 'libs', 'assets', '.apk', 'drawable', 'mipmap', '.gradle', 'gradlew']
```

得到过滤之后的文件

```
def filter(file, keywordList):
    for keyword in keywordList:
        if keyword in file:
            return False
    return True
```

#### 3. 开始对过滤之后的每个文件逐行读取匹配的字符串并且更改，因为要读和写文件所以要加入权限 r+ ，否则会报权限错误

```
with open(file, 'r+', errors='ignore') as f:
    lines = f.readlines()
    # 不要让 python 记住执行到这里，从文件头开始
    f.seek(0)
    # 清空文件
    f.truncate()
    for line in lines:
        f.write(line.replace(oldStr, newStr))
```

#### 4. 最终只需要一行代码就可以实现更改 Android 项目包名

```
python3 change_package_name.py
```

之后打开 Android studio 发现 包名确实已经更改了，但是左边的文件路径还是原来的，这时候需要对文件夹做手动调整，目前这点还没找到更好的方法。

![image](https://github.com/mawb23/change-android-package-name/blob/master/pic/build.png)
