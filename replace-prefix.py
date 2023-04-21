#! /usr/bin/env python3
# -*- coding:utf-8 -*-  

# chmod a+x text.py  开启权限
# 脚本功能: 查找所有 .codesnippet 文件的字符串内容并且替换,为了方便xcode快捷呼出codesnippet
# 使用方法: python3 /本文件路径

import os

file_suffix = ".codesnippet"

def replace_first_string_with_holder(file_path, target, holder):
    line_number = None
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for i, line in enumerate(lines):
        if target in line:
            lines[i] = line.replace(target, holder, 1)
            line_number = i + 1
            break
    with open(file_path, 'w') as file:
        file.writelines(lines)
    return line_number

def find_and_replace_in_folder(folder_path, target, holder):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(file_suffix):
                file_path = os.path.join(root, file)
                line_number = replace_first_string_with_holder(file_path, target, holder)
                if line_number:
                    print(f"替换过的文件名: {file}, 生效的行数: {line_number}")


# 主程序
if __name__ == "__main__":
    folder_path = '~/Library/Developer/Xcode/UserData/CodeSnippets'
    find_and_replace_in_folder(folder_path, "<string>wd-", "<string>xxxx-")
