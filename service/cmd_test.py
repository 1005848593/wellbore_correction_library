import os
import random
import shutil
import threading
import time
from concurrent.futures import ThreadPoolExecutor



def cmd(index: int):
    os.system(
        r'echo C:\Users\Lijing\Desktop\wellbore_correction_library\service\%s.3mod | python C:\Users\Lijing\Desktop\wellbore_correction_library\service\cal_data_w.py %s'
        % (index, index))


def fun(index):
    time.sleep(random.randint(1, 10))
    print(index)


if __name__ == '__main__':
    start = time.time()
    for i in range(0, 1):
        cmd(i)
        print(f'===========> 第 %s 轮结束，耗时:{time.time() - start:.4f}s <===========' % (i + 1))


    # thead_pool = ThreadPoolExecutor(max_workers=32)
    # for i in range(0, 30):
    #     thead_pool.submit(cmd, i)
    # time.sleep(10)
    # thead_pool.shutdown(wait=True)
