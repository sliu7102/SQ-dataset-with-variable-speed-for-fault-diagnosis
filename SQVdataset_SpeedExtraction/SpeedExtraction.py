
r"""
    @Author : sliu
    @README : SQV数据集 转速曲线提取
    @Date   : 2023-11-02 15: 02: 17
    @Related: 
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

import seaborn as sns
sns.set(style='darkgrid')
mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False   #用来正常显示负号
mpl.rcParams['agg.path.chunksize'] = 10000


def txtRead(fileDir, startLine=0):                                              # 从文本文件读取数据
    data = []
    with open(fileDir, 'r') as file:
        lines = file.readlines() 
    for line in lines[startLine:]:
        if line.strip():                                                        # 跳过空行
            lineData = line.strip().split('\t')
            lineData = [float(value) for value in lineData] 
            data.append(lineData)
    return np.array(data)


def extractSpeedCurve(fs, pluse):                                               # 提取转速曲线
    m = 1
    rise_instant = [0]
    for k in range(1, len(pluse) - 1):                                          # 这里的阈值条件(-1.7, -4等)是根据实际脉冲信号设计的, 会因脉冲信号不同而有差异
        if (pluse[k] - pluse[k - 1] < -1.7) and pluse[k] < -4 and (k - rise_instant[m - 1] > 200):
            m += 1
            rise_instant.append(k)                                              # 取满足判断条件的脉冲点序列，最小间隔为200

    rise_instant = rise_instant[1:]                                             # 存储的是键相点序列
    rise_time_s = np.array(rise_instant) / fs                                   # 键相点序列的时间
    dt = np.diff(rise_time_s)                                                   # 计算每一转所用的时间
    speed_per_convolution = 1 / dt                                              # 瞬时转速的估计（每转时间的倒数，转/秒）
    speed_per_min = speed_per_convolution * 60                                  # 转速（转/分）

    # ******总结：键相点时间和瞬时转速估计******
    rise_time_t = rise_time_s[1:]
    speed_per_v = speed_per_min

    return rise_time_t, speed_per_v


if __name__ == '__main__':

    filePath = './data/REC3642_ch3.txt'                                               
    rawSpeed = txtRead(filePath, startLine=17)                                  # 读取原始转速脉冲数据 0-16行为表头信息 0列为时间轴

    Fs = 25600                                                                  # 采样频率
    time, speed = extractSpeedCurve(Fs, rawSpeed[:, 1])                         # 计算转速曲线


    fig, ax = plt.subplots(2, 1, figsize=(6, 6))                                # 结果可视化
    TICKSIZE = 15
    LABELSIZE = 16
    plt.subplots_adjust(wspace= 0.2, hspace= 0.45) 
    axes = ax.flatten()
    axes[0].plot(rawSpeed[:, 0], rawSpeed[:, 1], 'r', linewidth=0.7, alpha=0.7)
    axes[1].plot(time, speed, 'b', linewidth=1)
    axes[0].set_xlabel('时间/s', fontsize=LABELSIZE)
    axes[0].set_ylabel('电压/V', fontsize=LABELSIZE)
    axes[1].set_xlabel('时间/s', fontsize=LABELSIZE)
    axes[1].set_ylabel('转速/rpm', fontsize=LABELSIZE)
    for i in range(2):
        axes[i].tick_params(labelsize=TICKSIZE, pad=0.1)
    plt.savefig('./speedCurve.png', bbox_inches='tight', dpi=800)
    # plt.show()

    np.savetxt('time.csv', time)
    np.savetxt('speed.csv', speed)
