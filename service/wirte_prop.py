import numpy as np
def tran(data):
    data = data.replace(' \n', '')
    #data = data.replace(' ', '')
    data = float(data)
    return data

def tran_num(data):
    data = data.split(' ')
    datax = int(data[0])
    datay = int(data[1])
    dataz = int(data[2])
    return datax, datay, dataz

def tran_all_data(data):
    value = []
    for i in range(len(data)):
        data1 = float(data[i].replace(' \n', ''))
        value.append(data1)
    return value

def get_wangge():
    with open('7.3mod', 'r') as read_f:
        num = read_f.readlines()
        x_num, y_num, z_num = tran_num(num[2])
        #print(x_num, type(x_num), y_num, z_num)
        x = tran_all_data(num[26: 26+x_num])
        y = tran_all_data(num[26+x_num: 26+x_num+y_num])
        z = tran_all_data(num[26+x_num+y_num: 26+x_num+y_num+z_num])
        #print(x, y, z, '\n', len(x), len(y), len(z))
    return x, y, z



# 半径=0.05
def write_data(sigma_layer, sigma_mud, r, write_f):
    x, y, z = get_wangge()
    sigma_layer = str(sigma_layer)
    sigma_mud = str(sigma_mud)
    for i in x:
        for j in y:
            for k in z:
                if (-r < i < r) & (-r < j < r):
                    write_f.write(sigma_mud + ' ')
                else:
                    write_f.write(sigma_layer + ' ')
    write_f.write('\n')

def write(sig_layer, sig_mud, r):
    with open('8.prop', 'w') as write_f:
        write_f.write('Mesh Real Resitivities'+'\n')
        write_data(sig_layer, sig_mud, r, write_f)

        write_f.write('Mesh sigma YY'+'\n')
        write_data(sig_layer, sig_mud, r, write_f)

        write_f.write('Mesh sigma ZZ'+'\n')
        write_data(sig_layer, sig_mud, r, write_f)
write(0.5, 2.0, 0.1)