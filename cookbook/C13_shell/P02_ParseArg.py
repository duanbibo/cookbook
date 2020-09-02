import argparse


'''

标准库支持的命令行库：标准库中留下的getopt、optparse和argparse就是证明  docopt

argparse自optparse脱胎而来，所以用法倒也大致相同，都是先生成一个parser实例，然后增加参数声明

解析命令行的库:
      命令 
      选项 参数
      选项 ：长选项， 短选项
     
     命令        执行文件    命令行子命令     命令行选项   选项的参数
     python3  serch.py    cookbook          -f         w      --partern
     
    位置参数 是第一个: 一般只配置参数，位置参数直接传值就可以了， 
       可选参数： 必须需要-参数 值， --参数 值..   在命令行中出现  
'''

#描述当前命令行的作用
##prefix_chars :设置的解析命令行的字符串前缀
parse=argparse.ArgumentParser(description="Serch some file",prefix_chars='-',prog='程序名')


#为当前命令行添加参数
#
#type：将输入转化成该数据类型，如dict，file对象，list这些
# nargs :代表这个参数的值是可多个的，可以控制数量 nargs=3,也可以不控制数量 nargs="*
#metavar :元变量 ，主要用来描述位置参数的变量名称。
#dest 目标：主要还是为了保证使用可选参数-和 -- 时，能够有一个有效的变量来接受处理它
#     保存到ArgumentParser对象时的属性名，省略该参数时默认“--dog”这样去掉“--”，建议写上dest的值
#default：默认值
#help 帮助信息

#传递给的第一个参数 必须是一系列标志或简单的参数名称
parse.add_argument(dest='filenames',metavar='filename',nargs='*')



#配置长短选项 ，设置必填参数，aciton =append ,参数的值放在字典中进行追加。
#action=count ,通过当前命令出现的次数，如 -v action=count   -vvv 日志详细程度最高
#action=version ,打印版本号并退出



parse.add_argument('-p','--pat',metavar='pattern',required=True,dest='pattern',action='append',
                   help='text pattern to serch for')

#设置可选参数，如果选择了可选参数后，选择的值只能是这个里面的
parse.add_argument('--l',dest='choices',choices=[1,2,3])


#为命令行传入文件，并且对文件获取指定的权限。读写
parse.add_argument('-f',dest='file',type=argparse.FileType('wb',0))


#退出和错误指令，避免调用 sys的exit
#parse.exit()
#parse.error()

#将参数字符串转换为对象，并将其分配为名称空间的属性。返回填充的名称空间。
args=parse.parse_args()


print(args.filenames)#打印参数的值，参数取的是dest内的值
print(args.patterns)