import shutil
import pathlib
import os
import  zipfile    # 这个库也支持包的压缩，并且支持设置密码
'''
shutil 是高级的文件，文件夹处理模块

文件目录的copy，移动，复制 ，多个文件内容追加,压缩和解压

  压缩 shutil.make_archive( base_name='压缩后的文件名'，format=‘压缩后的后缀名’，base_dir‘压缩的源文件’)
'''

#shutil文件复制，移动基础练习

shutil.copy('app.log','app1.log')  #复制文件
shutil.copyfile('app.log','app2.xls') #复制文件内容,目标文件可以与源文件类别不同



mulu=os.path.split(__file__)[0]
pathfile=pathlib.Path(mulu)/'app.log'       #这里使用pathfile直接用/斜杠拼接
print(pathfile)

#查看支持的压缩格式
print(shutil.get_archive_formats())

#压缩
#shutil.make_archive(base_name='applog',format='zip',base_dir=pathfile)

#解压
zipfile=pathlib.Path(mulu)/'applog.zip'
print(zipfile)

#shutil.unpack_archive(filename=zipfile,extract_dir=None,format='zip',)