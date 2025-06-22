
# 
import io
import sys
import pandas as pd

table = pd.read_csv('BMP.csv', encoding='utf-8')
#table = pd.read_csv('CJKA.csv', encoding='utf-8')
#table = pd.read_csv('Unicode-SIP.csv', encoding='utf-8')
#table = pd.read_csv('Unicode-TIP.csv', encoding='utf-8')

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


# 
# != 