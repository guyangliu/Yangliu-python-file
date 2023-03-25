def create_nc():
    name = input('请输入您的姓名：')
    for nc in nc_list:
        if nc['name'] == name:
            print('该用户已经存在，请重新输入')
            break
    else:
        tele = input('请输入您的手机号：')
        nc = {'name': name, 'tele': tele}
        nc_list.append(nc)


def del_nc():
    target = int(input('请输入您想删除的名片序号：'))
    nc_list.pop(target)


def revise_nc():
    l_long = len(nc_list)
    target = int(input('请输入您想修改的名片序号：'))
    if -1 < target < l_long:
        name_target = input('请输入新的名称：')
        tele_target = input('请输入新的手机号：')
        nc_list[target] = {'name': name_target, 'tele': tele_target}
    else:
        print('该名片不存在，请重新输入')


def all_nc():
    print('序号\t\t', '姓名\t\t', '手机号\t\t', sep='')
    count = 0
    for nc in nc_list:
        print('{}\t\t'.format(count), '{}\t\t'.format(nc['name']), '{}\t\t'.format(nc['tele']), sep='')
        count += 1


def search_nc():
    tar = input('请输入您要查询的人名：')
    for nc in nc_list:
        if nc['name'] == tar:
            print(nc)
            break
    else:
        print('未找到目标用户，请重新输入')


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
          '  浏览全部名片请输入"4"\n',
          '  查询人名请输入"5"\n'
          '  退出程序请输入"6"', sep='')
    print('-------------------')
    o = input()
    if o == '1':
        create_nc()
    elif o == '2':
        del_nc()
    elif o == '3':
        revise_nc()
    elif o == '4':
        all_nc()
    elif o == '5':
        search_nc()
    elif o == '6':
        end()
    else:
        print('输入数字有误，请重新输入')
