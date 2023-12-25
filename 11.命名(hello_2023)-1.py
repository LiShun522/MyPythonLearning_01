print("Hello World")
name="Li Shun Hsun"
age=35
height=172.55
weight=76.5
hobbie="run"
print(name,age,hobbie)

msg = '''
-----------%s info------------
name:%s
age:%d
height:%f cm
weight:%f kg
bobbie:%s
-------------end--------------
''' %(name[0:2],name,age,height,weight,hobbie)

print(msg)

import time
time.sleep(1)

#bool
score = 750
TOEIC = 700
if score >= TOEIC:
    print("You got the job.恭喜你",msg)
else:
    print("Sorry,you didn't get the job.再加油吧!!")
