# 定义九分分量的值R_**为接收的九个分量的值， X_**为屏蔽的九个分量的值
import cmath
import math
from shutil import move

# R_xx, R_xy, R_xz, R_yx, R_yy, R_yz, R_zx, R_zy, R_zz = 0, 0, 0, 0, 0, 0, 0, 0, 0
# X_xx, X_xy, X_xz, X_yx, X_yy, X_yz, X_zx, X_zy, X_zz = 0, 0, 0, 0, 0, 0, 0, 0, 0

# 定义发射和屏蔽之间的距离L11，发射和接收之间的距离L12
import numpy as np

# L11 = 18.40709 * 0.0254
# L12 = 24.7685 * 0.0254

# i = 1
w = 2 * math.pi * 26256.0
u = 4 * math.pi * (10 ** (-7))

# 发射接收线圈的匝数 X屏蔽 R接收
T = [66, 66, 100.000]

# X1 = [-6, -6, -6]
# R1 = [12, 12, 12]
# X2 = [-10, -10, -10]
# R2 = [21, 21, 21]
# X3 = [-15, -15, -15]
# R3 = [33, 33, 33]
# X4 = [-20.7222, -20.7222, -21]
# R4 = [51, 51, 51]
# X5 = [-31, -31, -31]
# R5 = [82, 82, 82]
# X6 = [-43.9353, -43.9353, -47]
# R6 = [128, 128, 128]
# X7 = [-70, -70, -70]
# R7 = [200, 200, 200]
X = np.array([[-6, -6, -6], [-10, -10, -10], [-15, -15, -15], [-20.7222, -20.7222, -21], [-31, -31, -31],
              [-43.9353, -43.9353, -47], [-70, -70, -70]])
R = np.array([[12, 12, 12], [21, 21, 21], [33, 33, 33], [51, 51, 51], [82, 82, 82], [128, 128, 128], [200, 200, 200]])


# print(C)


# print(C)

# 判断文件取何值
def get_value(line):
    a = cmath.sqrt(-1)
    line = line.split(' ')
    # print(line)
    if line[0] == '':
        value_real = line[1]
        if line[2] == '':
            value_imag = line[3]
        else:
            value_imag = line[2]
    else:
        value_real = line[0]
        if line[1] == '':
            value_imag = line[2]
        else:
            value_imag = line[1]
    value_real = float(value_real)
    value_imag = float(value_imag)
    data = value_real + value_imag * a
    # data = data * 4 * math.pi * math.pi
    return data


# 取值函数
def get_data(i):
    with open(r'.\%s_Hz.out' % i, 'r') as f:
        data = f.readlines()
        for index, line in enumerate(data):
            if index == 15:
                X_xx = get_value(line)
            if index == 16:
                X_xy = get_value(line)
            if index == 17:
                X_xz = get_value(line)
            if index == 18:
                R_xx = get_value(line)
            if index == 19:
                R_xy = get_value(line)
            if index == 20:
                R_xz = get_value(line)
            if index == 21:
                X_yx = get_value(line)
            if index == 22:
                X_yy = get_value(line)
            if index == 23:
                X_yz = get_value(line)
            if index == 24:
                R_yx = get_value(line)
            if index == 25:
                R_yy = get_value(line)
            if index == 26:
                R_yz = get_value(line)
            if index == 27:
                X_zx = get_value(line)
            if index == 28:
                X_zy = get_value(line)
            if index == 29:
                X_zz = get_value(line)
            if index == 30:
                R_zx = get_value(line)
            if index == 31:
                R_zy = get_value(line)
            if index == 32:
                R_zz = get_value(line)
    return X_xx, X_xy, X_xz, R_xx, R_xy, R_xz, X_yx, X_yy, X_yz, \
           R_yx, R_yy, R_yz, X_zx, X_zy, X_zz, R_zx, R_zy, R_zz


# t是发射线圈匝数， x是屏蔽线圈匝数， r是接收线圈匝数， hx是屏蔽磁场， hr是接收磁场
def cal(x, r, hx, hr, n, l11, l12):
    i = cmath.sqrt(-1)
    # 通用的常数
    C = -(8 * i * math.pi * l11 * l12) / (w * u)

    a1 = x * hx
    a2 = r * hr

    a = a1 + a2

    b1 = x * l12
    b2 = r * l11
    b = (b1 + b2)
    sigma = C * (a / b) * n
    # sigma = sigma.real
    # sigma = round(sigma, 8)
    return sigma.real


if __name__ == '__main__':
    L11 = [0.1260, 0.2040, 0.3210, 0.4675, 0.7103, 1.0920, 1.6824]
    L12 = [0.1590, 0.2610, 0.4060, 0.6291, 0.9836, 1.5455, 2.3906]

    for i in range(0, 2):
        # 将其放在同一个文件夹
        # src_path = r'C:\Users\Lijing\Desktop\wellbore_correction_library\test\tong\fre_26256\%s_Hz.out' % i
        # dst_path = r'/test/dip0_azi0/tong/fre_26256/data_out'
        # move(src_path, dst_path)

        X_xx, X_xy, X_xz, R_xx, R_xy, R_xz, X_yx, X_yy, X_yz, \
        R_yx, R_yy, R_yz, X_zx, X_zy, X_zz, R_zx, R_zy, R_zz = get_data(i)
        # print('data ', R_xx, R_xy, R_xz, R_yx, R_yy, R_yz, R_zx, R_zy, R_zz,
        #       X_xx, X_xy, X_xz, X_yx, X_yy, X_yz, X_zx, X_zy, X_zz)

        xx = cal(X[i, 0], R[i, 0], X_xx, R_xx, 1, L11[i], L12[i])
        print('data is:', X_xx, R_xx)
        xy = cal(X[i, 0], R[i, 0], X_xy, R_xy, 1, L11[i], L12[i])
        xz = cal(X[i, 0], R[i, 0], X_xz, R_xz, 2, L11[i], L12[i])
        yx = cal(X[i, 1], R[i, 1], X_yx, R_yx, 1, L11[i], L12[i])
        yy = cal(X[i, 1], R[i, 1], X_yy, R_yy, 1, L11[i], L12[i])
        yz = cal(X[i, 1], R[i, 1], X_yz, R_yz, 2, L11[i], L12[i])
        zx = cal(X[i, 2], R[i, 2], X_zx, R_zx, 2, L11[i], L12[i])
        zy = cal(X[i, 2], R[i, 2], X_zy, R_zy, 2, L11[i], L12[i])
        zz = cal(X[i, 2], R[i, 2], X_zz, R_zz, 1 / 2, L11[i], L12[i])

        # 将电阻率值存放在文件中
        with open('data_sigma', 'a') as write_f:
            # newlines = '   xx   ' + '   xy   ' + '   xz   ' + '   yx   ' + '   yy   ' + '   yz   ' + '   zx   ' \
            #            + '   zy   ' + '   zz   ' + '\n'
            # write_f.writelines(newlines)
            newlines = str(xx) + ' ', str(xy) + ' ', str(xz) + ' ', str(yx) + ' ', str(yy) + ' ', \
                       str(yz) + ' ', str(zx) + ' ', str(zy) + ' ', str(zz) + '\n'
            write_f.writelines(newlines)
