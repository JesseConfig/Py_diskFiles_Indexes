# -*- coding: UTF-8 -*-
import os
import os.path as pt

# 这个模块实现的功能就是将指定文件夹下的所有文件遍历，并将路径和所在盘符存到一个列表中返回

def scan_file(path):
    result = []
    for root, dirs, files in os.walk(path):
        for f in files:
            file_path = pt.abspath(pt.join(root, f))

            result.append((file_path, file_path[0]))  # 保存路径与盘符

    return result
