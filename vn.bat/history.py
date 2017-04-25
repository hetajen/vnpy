# encoding: UTF-8

"""

"""

'''
History
<id>            <author>        <description>
2017041900      hetajen         开启软件后自动连接CTP和DB
2017042100      hetajen         自动执行CTA策略
2017042300      hetajen         新增：从sina财经json接口获取数据
2017042400      hetajen         根据bat脚本参数自动选择交易账户
2017042401      hetajen         修改非同一目录下的文件的引用路径。消除import时找不到文件的报错。
2017042402      hetajen         增加新文件vtBackTesting.py。解耦回测&优化的执行程序。
2017042500      hetajen         Tick数据不再保存到MongoDB。MongoDB只保存M1和D数据。
2017042501      hetajen         自动执行DataRecorder操作（保存M1数据到MongoDB）
'''