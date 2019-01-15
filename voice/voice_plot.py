# -*- coding: utf-8 -*-
import queue
import sys
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

def audio_callback(indata, outdata, frames, time, status):
    """サンプリングごとに呼ばれるコールバック関数"""
    if status:
        print(status, file=sys.stderr)
    indata2 = np.zeros([indata.shape[0],1])
    #print(indata2.shape)
    #print(indata.shape)
    for i in range(indata2.shape[0]):
        if(i < indata2.shape[0]/voice_pitch):
            indata2[i] = indata[voice_pitch*i]
        else:
            indata2[i] = indata[voice_pitch*(i-int(indata2.shape[0]/voice_pitch))]
    outdata[:] = indata2 #indataの型はnumpy.ndarray
    #indataを直接乗算すると音の大きさを変換できる
    #
    global q
    q.put(indata2)


def update_plot(frame):
    """matplotlibのアニメーション更新毎に呼ばれるグラフ更新関数"""

    global plotdata
    while True:
        try:
            data = q.get_nowait()
        except queue.Empty:
            break

        shift = len(data)
        plotdata = np.roll(plotdata, -shift, axis=0)
        plotdata[-shift:, :] = data

        lines[0].set_ydata(plotdata[:, 0])

    return lines

if __name__ == '__main__':
    voice_pitch = 1
    samplerate = 4000   # サンプリング周波数
    window = 0.2        # グラフ表示サンプル数決定係数
    interval = 3        # グラフ更新頻度（ミリ秒）
    channels = 1        # チャンネル数（1固定）
    
    print("voice_pitch? (default 1)")
    voice_pitch = int(input())
    
    q = queue.Queue()

    length = int(window * samplerate)   # グラフに表示するサンプル数
    plotdata = np.zeros((length, 1))

    fig, ax = plt.subplots()
    lines = ax.plot(plotdata)          # グラフのリアルタイム更新の最初はプロットから
    ax.axis((0, len(plotdata), -1, 1))

    stream = sd.Stream(channels=channels, samplerate=samplerate, callback=audio_callback) #収音実行
    ani = FuncAnimation(fig, update_plot, interval=interval, blit=True)
    with stream:
        plt.show()
