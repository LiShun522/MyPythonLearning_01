
budget = 1800
if budget >= 1800:
    print("可以嘗試泰晶殿，服務好大保健...")
else:
    print("1200元的性價比較好...")

budget = input("我的預算:")

msg = f"""
-------大保健-------
預算:{budget}
建議:
------謝謝惠顧-------
"""

print(msg)

budget = 2000

if budget <500:
    print("15分鐘體驗...")
elif budget < 800:
    print("半小時服務...")
elif budget < 1200:
    print("一小時深層...")
elif budget < 1800:
    print("兩小時全包大保健")
#超過這些區域，最後用else來判斷
else:
    print("你該去找更好的了")

#頂層代碼之下，必須留空格，官方建議四格或tab鍵，二擇一。

#嵌套分支:最多在四層，再多系統笨拙，後續不易發展。
loneliness = 90
money = 1000

if loneliness > 70:
    print("寂寞難耐，要去大保健")
    if money < 2800:
        print("你還是玩自己吧!")