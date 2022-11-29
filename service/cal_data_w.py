import os
import shutil
import numpy as np
import linecache
import wirte_prop

# 设置前两行固定参数
def parameters():
    data = '0 0 0\n'
    EPS = str(float(1e-9))
    data = data + '0 50000 ' + EPS + '\n'
    return data


# 定义节点个数
def grid_num(X_num, Y_num, Z_num):
    # global X_num
    X_num = str(X_num)
    Y_num = str(Y_num)
    Z_num = str(Z_num)
    num = X_num + ' ' + Y_num + ' ' + Z_num
    return num


# 定义频率个数
def frequency_information(frequence_num, layer_num, frequence):
    data = str(frequence_num) + ' ' + str(layer_num) + ' 0 0 0\n'
    data = data + str(float(frequence)) + '\n'
    data = data + '0 5 5 0.0\n'
    return data


# 模型背景信息
def model_background_information():
    data = '0 0.5 0.5 0.5 -9999.0\n' \
           '0 0.5 0.5 0.5 30\n' \
           '0 0.5 0.5 0.5 40\n'
    return data

# 仪器有偏心距和偏心角度
def calibrate_coor(de, angle_s, num):
    return


# 接收阵列的坐标
def recevier_data(source_num: int, recevier_num: int):
    recevier_snum = str(recevier_num)
    data = recevier_snum + ' 0' + ' 1' + '\n'
    # for s in [x * 0.1 for x in range(0, 50)]:
    coor_dict = {'coordinate_r': '0.0 0.0 21.4620 ', 'coordinate_s': '0.0 0.0 21.4950 '}
    angle_dict = {'angle1': '0.0 0.0', 'angle2': '0.0 90.0', 'angle3': '90.0 0.0'}

    sources_coor = '0.0 0.0 21.3360'

    for key, value in coor_dict.items():
        for key1, value1 in angle_dict.items():
            data = data + value + value1 + '\n'

    data = data + str(source_num) + '\n'

    for key, value in angle_dict.items():
        data = data + '1' + '\n'
        data = data + '2 ' + value + '\n'
        data = data + sources_coor + '\n'

    return data


#定义源的信息
# def sources_information(source_num: int):
#     angle = ['0.0 0.0', '0.0 90.0', '90.0 0.0']
#     coor = '0.0 0.0 21.3360'
#     source_s_num = str(source_num)
#     data = source_s_num + '\n'
#     for i in range(source_num):
#         data = data + '1' + '\n'
#         data = data + '2 ' + angle[i] + '\n'
#         data = data + coor + '\n'
#     return data


# 定义X Y Z三个方向的网格长度 boundaries_x是X_num-1
def node_length(x_begin, x_end, num_x, y_begin, y_end, num_y, z_begin, z_end, num_z):
    data = ''
    data_x = np.linspace(x_begin, x_end, num_x)
    #data_x = ('%.4f' % data_x)
    for x in data_x:
        x = "{:.4f}".format(x)
        data = data + str(x) + '\n'

    data_y_1 = np.linspace(y_begin, -0.2, 47)
    data_y_2 = np.linspace(-0.19, 0.2, 40)
    data_y_3 = np.linspace(0.25, y_end, 46)
    data_1 = np.append(data_y_1, data_y_2)
    data_y = np.append(data_1, data_y_3)
    for y in data_y:
        y = "{:.4f}".format(y)
        data = data + str(y) + '\n'

    data_z = np.linspace(z_begin, z_end, num_z)
    for z in data_z:
        z = "{:.4f}".format(z)
        data = data + str(z) + '\n'

    x_num = str(num_x - 1)
    y_num = str(num_y - 1)
    z_num = str(num_z - 1)

    data = data + '1 ' + x_num + '\n'
    data = data + '1 ' + y_num + '\n'
    data = data + '1 ' + z_num + '\n'

    return data


# 定义最后两行参数
def else_information():
    data = '0' + '\n'
    data = data + '100.0 ' + '100.0 ' + '100.0 '
    return data


if __name__ == '__main__':
    from sys import argv
    #i = argv[1]
    for i in range(0, 1):
        with open('%s.3mod' % i, 'w') as write_f:
            newline = parameters()  # 前两行信息
            write_f.writelines(newline)

            newline = grid_num(101, 133, 281) + '\n'  # 设置网格点数
            write_f.writelines(newline)

            newline = frequency_information(1, 3, 26256.0)  # 频率信息
            write_f.writelines(newline)

            newline = model_background_information()  # 背景模型信息
            write_f.writelines(newline)

            newline = recevier_data(3, 6)  # 设置接收点的坐标
            write_f.writelines(newline)

            newline = node_length(-2.5, 2.5, 101, -2.5, 2.5, 133, 19, 26, 281)  # 网格信息
            write_f.writelines(newline)

            newline = else_information()  # 设置最后两行信息
            write_f.writelines(newline)
        # 1
        # 写prop文件 参数为地层电阻率，泥浆电阻率，井筒半径
        #wirte_prop.write(0.5, 2.0, 0.05)
        # shutil.copyfile(r'C:\\Users\\Lijing\\Desktop\\wellbore_correction_library\\service\\test.prop',
        #             'C:\\Users\\Lijing\\Desktop\\wellbore_correction_library\\service\\%s.prop' % i)
    os.system('EM3D.exe')