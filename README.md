# ptxt_list

识典古籍全库漢字频率表

myresult.zen(识典BMP).csv  ————  识典全库在 URO+ (20992)和 CJK-A（6592） 上的频率。

myresult.zen(识典A区).csv  ————  识典全库在  CJK-A（6592） 上的频率。前一个表的真子集。

myresult.zen(识典B区).csv  ————  识典全库在  plane02（60383， CJK-I 662 不含） 上的频率。

myresult.zen(识典第三平面含CJK-I区).csv  ————  识典全库在  plane03（9131）和CJK-I（662） 上的频率。


所使用的文本达 5.24 GB ，超 26亿漢字。


须用的工具 python 3.12.5+ ; pip ; 
须用的库 pandas sys io


须用的代码：


```python
import io
import sys
import pandas as pd

#table = pd.read_csv('BMP.csv', encoding='utf-8')
#table = pd.read_csv('CJKA.csv', encoding='utf-8')
#table = pd.read_csv('Unicode-SIP.csv', encoding='utf-8')
table = pd.read_csv('Unicode-TIP.csv', encoding='utf-8')
table.head()
# 
head = min(table['decimalism'])
end = max(table['decimalism'])
l = end - head +1

# 
result = [0] * l
with open('80.sh','r', encoding='utf-8') as f:
    while True:
        c = f.read(1)
        # print(c)
        if not c:
            print("end")
            break
        # break
        ordd = ord(c)
        if (ordd<=end) and (ordd>=head):
            result[ordd-head]+=1


# 
with open('myresult.zen.csv','w', encoding='utf-8') as f:
    for num, times in enumerate(result):
        if times != 0:
            if (chr(num+head)) in table['kanji'].values:
                f.write("%s,%s,%s\n"%(hex(num+head) , chr(num+head), times ))

```


输入文件为  80.sh（必须是 utf-8 ）； 输出自动保存为 myresult.zen.csv






