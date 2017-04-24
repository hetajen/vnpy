# encoding: UTF-8

'''
History
<id>            <author>        <description>
2017042402      hetajen         增加新文件vtBackTesting.py。解耦回测&优化的执行程序。

'''

import time
from ctaAlgo.strategy.strategyAtrRsi import AtrRsiStrategy
from ctaAlgo.ctaBase import MINUTE_DB_NAME

def getEngine():
    from ctaAlgo.ctaBacktesting import BacktestingEngine

    engine = BacktestingEngine()
    engine.setBacktestingMode(engine.BAR_MODE)  # 引擎的回测模式为K线
    engine.setStartDate('20120101')  # 回测用的数据起始日期
    engine.setSlippage(0.2)  # 股指1跳
    engine.setRate(0.3 / 10000)  # 万0.3
    engine.setSize(300)  # 股指合约大小
    engine.setDatabase(MINUTE_DB_NAME, 'IF0000')

    return engine

def getParam(type=0):
    if type == 0:
        setting = {'atrLength': 11}
    else:
        from ctaAlgo.ctaBacktesting import OptimizationSetting
        setting = OptimizationSetting()  # 新建一个优化任务设置对象
        setting.setOptimizeTarget('capital')  # 设置优化排序的目标是策略净盈利
        setting.addParameter('atrLength', 12, 20, 2)  # 增加第一个优化参数atrLength，起始11，结束12，步进1
        setting.addParameter('atrMa', 20, 30, 5)  # 增加第二个优化参数atrMa，起始20，结束30，步进1
        setting.addParameter('rsiLength', 5)  # 增加一个固定数值的参数
    return setting

def backTesting():
    engine = getEngine()
    setting = getParam()

    engine.initStrategy(AtrRsiStrategy, setting)
    engine.runBacktesting() # 开始跑回测
    engine.showBacktestingResult() # 显示回测结果

def optimize():
    engine = getEngine()
    setting = getParam(1)

    engine.runOptimization(AtrRsiStrategy, setting) # 单进程优化。耗时：xxx秒
    #engine.runParallelOptimization(AtrRsiStrategy, setting) # 多进程优化。耗时：xx秒

if __name__ == '__main__':
    start = time.time()
    backTesting()
    # optimize()
    print u'耗时：%s' % (time.time() - start)  # 性能测试