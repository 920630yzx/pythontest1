num1 = 10
num1 = 10.9
num2 = num1
print(num1)

num3 = num4 = num5 = 10
print(num1, num2, num3, num4, num5)

num6, num7 = 6, 7
print(num6, num7) #直接打印多个变量
print('abc',num6, num7) #复合的打印

num1=input('输入一个数字')  #通过input输入的都是字符串的格式
num2=input('输入一个数字')
print('num1+num2=',num1+num2) #注意此时的num1是字符串并不是数字，所以不能直接相加
print('num1+num2=',int(num1)+int(num2))
print('num1+num2=',float(num1)+float(num2)) #针对小数的情况

var1='\\n' #两个\代表一个\字符，可使转义字符失效
print(var1)



'''
一、算术运算符
+ - *（乘） /（除）%（取余） **（幂） //(整除)
二、赋值运算符
变量 = 值  	//将右边的值，赋值给左边的变量
三、复合的赋值运算符
+= -= *= /= %= **= //=
//a += 3 <-->  a = a + 3
四、关系运算符
关系运算符描述值与值之间的关系
>  <  >=  <=  ==(等于)  !=（不等于）
值1 > 值2
【注】如果关系运算符和左右值描述的关系成立，则关系表达式的值为True，否则为False。
【注】表达式描述的关系成立，也成为【表达式为真】，反之，也称为【表达式为假】。

五、逻辑运算符
值1 and 值2		读作 "与"
【注】对于and表达式，如果值1和值2都是真，总表达式为真，值1值2只要有一个假，总表达式为假。
值1 or 值2		读作 "或"
【注】对于or表达式，如果值1和值2都是真，总表达式为真，值1值2如果只有一个为真，另一个为假，总表达式仍为真。只有值1值2均为假，总表达式才为假。
not 值			读作 "非"
【注】对于not表达式，如果值为真，则总表达式为假，如果值为假，总表达式为真。



【流程控制】正常的Python代码会由上至下依次执行每一句。流程控制则在特定条件触发时，修改代码的正常执行顺序。
六、if语句
if 表达式:
	单行或多行语句
【注】当程序执行到if语句，首先判断【表达式】是否为真，如果为真，执行【单行或多行语句】，否则不执行【单行或多行语句】，直接执行后面的语句。

七、if...else...语句
if 表达式:
	语句1
else:
	语句2
【注】当程序执行到ifelse语句，首先判断【表达式】，如果为真，执行【语句1】，不执行【语句2】。否则执行【语句2】不执行【语句1】

八、if...elif...语句
if 表达式1:
	语句1
elif 表达式2:
	语句2
elif 表达式3:
	语句3
else:
	语句4
【注】当程序执行到该语句，首先判断【表达式1】，如果成立，执行【语句1】，然后，跳过整个ifelif语句，执行后面的代码。如果【表达式1】不成立，判断【表达式2】是否成立，如果成立，执行【语句2】，然后跳过整个ifelif语句，执行后面代码，如果不成立，再判断【表达式3】，依次类推。如果所有表达式都不成立，执行语句4.elif可以有无数个。

九、while语句
while 表达式:
	语句
【注】当程序执行到while语句，首先判断【表达式】，成立，执行【语句】，不成立，不执行【语句】；如果成立，执行完语句，会再回到【表达式】，如果仍然成立，再次执行【语句】，然后再回到判断【表达式】，直到【表达式】不成立，跳出while结构，执行后面的语句。
【另】python没有do while，同样python没有 switch

十、for语句   for i in range(0,100):   #0到99     for i in range(100,0,-1) #从100到1   '左侧是闭区间，右侧是开区间'

十一、break与continue
break：中断当前循环，跳出当前循环,无视if
continue：中断本次循环，进入下一次循环
'''


