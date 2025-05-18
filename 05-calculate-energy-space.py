# 計算矩形面積

length = float (input('請輸入矩形的長度'))
width = float (input ('請輸入矩形的寬度'))

area = length * width
print (f"面積為 {area} 平方公分")

# 套用在身心靈中

print ('你終於來啦～下班辛苦啦～喵！')
print ('\n讓我們一起計算，今天的你為自己創造了多少的「能量修護空間」吧')

length = float (input ('深呼吸～讓我們回想：今天給自己的放空時間有多少吧（如：3分鐘的冥想時間）'))
width = float (input ('那麼～今天有意識的「深呼吸」了幾次呢'))
area = length * width

if area <= 3:
   print ('這樣呀～看來你今天很忙呢喵！再忙也要好好放鬆喔喵！')

elif area <= 10:
    print ('你今天有給自己好多的「能量修復時光」，真是太棒了喵～放空這件事，真是太重要了喵～')

else:
   print (f"哇呀喵～你今天總共為自己創造了 {area} 分鐘 的「能量修護空間」了喵，是能量修復專家呢喵！")
