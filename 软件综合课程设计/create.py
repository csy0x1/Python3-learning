'''
录入教师信息
Todo:
1.对输入数据进行合法性检查
'''

import prettytable,os,time
from database import Insert_Info

def Input_Info():
    flag=True   #修改信息标识符
    os.system('cls')
    Teacher={}
    Teacher['工号']=input('请输入你的工号: ')
    Teacher['姓名']=input('请输入你的姓名: ')
    Teacher['年龄']=input('请输入你的年龄: ')
    Teacher['职称']=input('请输入你的职称: ')
    Teacher['系名']=input('请输入你所在系: ')
    Teacher['手机号码']=input('请输入你的手机号码: ')
    Teacher['联系地址']=input('请输入你的联系地址: ')
    while flag:
        Show_Info(Teacher)
        print('请确认信息无误，若要修改，请按以下格式键入新内容，否则按回车提交')
        info=input('请输入要修改的信息名以及内容，一次一条，以空格分隔(如姓名 XX): ')
        if(info==''):   #检测用户提交
            if(Insert_Info(Teacher)==False):
                print("操作失败!")
                break
            else:
                print('操作成功！')
                flag=False
                break
        index=0
        for i in info:  #获取用户输入的key值和value值
            if i==' ':
                break
            else:
                index+=1
        key=info[0:index]
        value=info[index+1:]    
        if(key in Teacher):     #检测用户输入的key值是否存在
            Teacher[key]=value
        else:
            print('\n键值不存在!')
            time.sleep(1)
            continue

def Show_Info(info):
    os.system('cls')
    table=prettytable.PrettyTable()     #创建表格
    table.field_names=['信息','内容']   #设置表头
    for key,value in info.items():
        table.add_row([key,value])
    print(table.get_string(title='教师信息'))

if __name__=='__main__':    #调试用
    Input_Info()