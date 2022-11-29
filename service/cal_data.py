import os
import shutil
import linecache


# d = {'q': '2ws'}
# f = open('2-te.3mod')
# #
# # # 文件行数
# count = len(f.readlines())
# print(count)
# f.close()
# count = 0

# f = open('2-te.3mod', 'w')
# f.seek(3, 0)
# f.write('23')
# for i in range(count):
#     if i == 7:
#         a = ''.join('123')
#         f.write(a)


# main = "EM3D.exe"
# f2 = os.popen(main)
# data = f2.readlines()
# f2.close()
# print(data)
#
# count = 0
# with open('2-te.3mod', "r+", encoding="utf-8") as read_f:
#     data = read_f.readlines()
#     with open('2-te.3mod', 'w') as write_f:
#         for line in data:
#             count += 1
#             if count == 7:
#                 newline = line.strip() + " 123" + "\n"
#                 write_f.writelines(newline)
#             else:
#                 write_f.writelines(line)

# 第七行的输入数据
# a = 1e-7
# print(a)

# 设置前两行固定参数
def parameters():
    data = '0 0 0\n'
    EPS = str(float(1e-7))
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
    data = '0 0.5 0.5 0.25 -9999.0\n' \
           '0 0.1 0.1 0.05 30.48\n' \
           '0 0.5 0.5 0.125 45.72\n'
    return data


# 接收阵列的坐标
def recevier_data(recevier_num: int, point_r: float):
    recevier_snum = str(recevier_num)
    data = recevier_snum + ' 0' + ' 1' + '\n'
    # for s in [x * 0.1 for x in range(0, 50)]:
    coor_dict = {'coordinate_r': '0.0 0.0 %s ' % (point_r * 0.3048 * 5 + 18.40709 * 0.0254), 'coordinate_s': '0.0 0.0 %s ' % (point_r * 0.3048 * 5 + 24.7685 * 0.0254)}
    angle_dict = {'angle1': '0.0 0.0', 'angle2': '0.0 90.0', 'angle3': '90.0 0.0'}
    for key, value in coor_dict.items():
        for key1, value1 in angle_dict.items():
            data = data + value + value1 + '\n'
    return data


# 定义源的信息
def sources_information(source_num: int, point_s: float ):
    angle = ['0.0 0.0', '0.0 90.0', '90.0 0.0']
    coor = '0.0 0.0 %s' % (point_s * 0.3048 * 5)
    source_s_num = str(source_num)
    data = source_s_num + '\n'
    for i in range(source_num):
        data = data + '1' + '\n'
        data = data + '2 ' + angle[i] + '\n'
        data = data + coor + '\n'
    return data


# 定义X Y Z三个方向的网格长度 boundaries_x是X_num-1
def node_length(x_begin, x_end, x_step, y_begin, y_end, y_step, z_begin, z_end, z_step):
    data = ''
    for i in range(x_begin, x_end, x_step):
        length = str(float(i * 0.1))
        data = data + length + ' '
    data = data + '\n'  # linux os.linesep

    for j in range(y_begin, y_end, y_step):
        length1 = str(float(j * 0.1))
        data = data + length1 + ' '
    data = data + '\n'

    for k in range(z_begin, z_end, z_step):
        length2 = str(float(k))
        data = data + length2 + ' '
    data = data + '\n'

    # 定义boundaries_num
    x_num = str(int((x_end - x_begin) / x_step - 1))
    y_num = str(int((y_end - y_begin) / y_step - 1))
    z_num = str(int((z_end - z_begin) / z_step - 1))

    data = data + '1 ' + x_num + '\n'
    data = data + '1 ' + y_num + '\n'
    data = data + '1 ' + z_num + '\n'

    return data


# 定义最后两行参数
def else_information():
    data = '0' + '\n'
    data = data + '1000.0 ' + '1000.0 ' + '1000.0 '
    return data


if __name__ == '__main__':
    from sys import argv
    i = argv[1]
    #for i in range(0, 2):
    with open('%s.3mod' % i, 'w') as write_f:
        newline = parameters()  # 前两行信息
        write_f.writelines(newline)

        newline = grid_num(41, 41, 161) + '\n'  # 设置网格点数
        write_f.writelines(newline)

        newline = frequency_information(1, 3, 26256.0)  # 频率信息
        write_f.writelines(newline)

        newline = model_background_information()  # 背景模型信息
        write_f.writelines(newline)

        newline = recevier_data(6, float(i))  # 设置接收点的坐标
        write_f.writelines(newline)

        newline = sources_information(3, float(i))  # 设置源的信息
        write_f.writelines(newline)

        newline = node_length(-10, 11, 1, -10, 11, 1, -160, 162, 5)  # 网格信息
        write_f.writelines(newline)

        newline = else_information()  # 设置最后两行信息
        write_f.writelines(newline)

    # with open('demo.prop', 'w') as write_f:
    #     a = ('0.5' + ' ') * 100 * 40 * 40
    #     b = ('0.5' + ' ') * 100 * 40 * 40
    #     c = ('0.25' + ' ') * 100 * 40 * 40
    #     d = ('0.1' + ' ') * 40 * 40 * 40
    #     e = ('0.1' + ' ') * 40 * 40 * 40
    #     f = ('0.05' + ' ') * 40 * 40 * 40
    #     h = ('0.5' + ' ') * 20 * 40 * 40
    #     i = ('0.5' + ' ') * 20 * 40 * 40
    #     j = ('0.125' + ' ') * 20 * 40 * 40
    #     newline = a + '\n' + b + '\n' + c + '\n' + d + '\n' + e + '\n' + f + '\n' + h + '\n' + i + '\n' + j
    #     write_f.writelines(newline)



    shutil.copyfile(r'C:\\Users\\Lijing\\Desktop\\wellbore_correction_library\\service\\demo.prop',
                    'C:\\Users\\Lijing\\Desktop\\wellbore_correction_library\\service\\%s.prop' % i)
    os.system('EM3D2.exe')

