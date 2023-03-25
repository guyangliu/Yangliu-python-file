def create_nc():
    name = input('请输入您的姓名：')
    tele = input('请输入您的手机号：')
    nc = {'name': name, 'tele': tele}
    nc_list.append(nc)


def del_nc():
    target = int(input('请输入您想删除的名片序号：'))
    nc_list.pop(target)


def revise_nc():
    target = int(input('请输入您想修改的名片序号：'))
    name_target = input('请输入新的名称：')
    tele_target = input('请输入新的手机号：')
    nc_list[target] = {'name': name_target, 'tele': tele_target}


def search_nc():
    print(nc_list)


def end():
    t = input('是否退出程序？输入"y"确认')
    if t == 'y':
        exit()


nc_list = []
print('欢迎来到名片查询系统V1.0')
while True:
    print('-------------------')
    print('  添加名片请输入"1"\n',
          '  删除名片请输入"2"\n',
          '  修改名片请输入"3"\n',
          '  查询名片请输入"4"\n',
          '  退出程序请输入"5"', sep='')
    print('-------------------')
    o = input()
    if o == '1':
        create_nc()
    elif o == '2':
        del_nc()
    elif o == '3':
        revise_nc()
    elif o == '4':
        search_nc()
    elif o == '5':
        end()
    else:
        print('输入数字有误，请重新输入')
