# -*- coding: utf-8 -*-
# 生成文件夹中所有文件的路径到txt
import os
def listdir(path, list_name):  # 传入存储的list
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        else:
            list_name.append(file_path)
 
list_name=[]
path='E:/my_site/mkdocs-site/docs/Foundation Course/Python/python基础'   #文件夹路径
listdir(path,list_name)
print(list_name)
 
with open('./list.txt','w') as f:     #要存入的txt
    write=''
    for i in list_name:
        write=write + '- ' + str(i).lstrip('E:/my_site/mkdocs-site/docs/Foundation Course/Python/python基础\\Day').rstrip('.md') + ': ' + str(i).replace('E:/my_site/mkdocs-site/docs/','') +'\n'
    f.write(write)