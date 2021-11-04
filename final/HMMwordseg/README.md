# HMMwordseg

基于HMM的中文分词

## 数据集

数据集使用见'icwb2-data\README.md'

arrangement recommendation：

--HMMWORDSEG

|

-----HMMseg

-----icwb2-data

    |

    ------gold

    ------testing

    ------training

-----outputs

-----results

## HMMseg

dataloader.py载入数据

model.py包含Viterbi算法和一些初始化

utils.py包含测试和计算的一些工具

## main.py

主要包含train、eval、inference、demo

使用：python main.py -d pku -m train -s

## 可视化

Ui_spilit.py实现整体GUI框架的搭建

visualization.py实现不同按键的连接和功能、

使用：python visualization.py 