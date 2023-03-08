while True:
    xd = eval(input("请输入xd:"))
    xw = eval(input("请输入xw:"))
    xf = eval(input("请输入xf:"))
    R = eval(input("请输入R:"))
    a = eval(input("请输入a:"))
    f = (xd-xw)/(xf-xw)
    print("f=",round(f,3))
    print("精馏段操作方程:yn+1="+str(round(R/(R+1),7))+"*xn+"+str(round(xd/(R+1),7)))
    print("平衡关系:xn="+"yn/("+str(a)+"-"+str(round(a-1,3))+"yn)")
    print("提馏段操作方程:yn+m+1="+str(round((R+f)/(R+1),7))+"*xn+m+"+"("+str(-1*round(((f-1)/(R+1))*xw,7))+")")

    #精馏段操作方程
    def Gyn1(x):
        yn1 = round(R/(R+1),7)*x+round(xd/(R+1),7)
        return round(yn1,3)

    #平衡关系
    def Gxn(yn):
        xn = yn/(a-round(a-1,3)*yn)
        return round(xn,3)

    #提溜段操作方程
    def Gynm1(x):
        ynm1 = round((R+f)/(R+1),7)*x-round(((f-1)/(R+1))*xw,7)
        return round(ynm1,3)

    #y1=xd时，用平衡关系式算出x1
    print("y1="+str(xd),"x1="+str(round(Gxn(xd),3)))

    #开始计数，从i=2开始，已知量为y1和x1
    i = 2 
    xn = Gxn(xd)
    yn = xd

    #精馏段循环开始
    while True:
        xn1 = xn                                                         #保留上一个xn的值
        yn = Gyn1(xn)                                                    #计算新的yn
        xn = Gxn(yn)                                                     #计算新的xn
        if xn < xf:                                                      #如果新的xn比xf小了，那么就取上一个xn的值，结束精馏段
            break
        print("y"+str(i)+"="+str(yn),"x"+str(i)+"="+str(xn))
        i = i+1

    #提示用户进入提馏段
    print("计算提馏段，取x"+str(i-1)+"="+str(round((xn1+xf)*0.5,3)))

    #求平均值
    xn = round((xn1+xf)*0.5,3)

    #接着精馏段的计数，继续计数
    while xn >= xw:
        yn = Gynm1(xn)
        xn = Gxn(yn)
        print("y"+str(i)+"="+str(yn),"x"+str(i)+"="+str(xn))
        i = i+1

    #计算汇总
    print("得到理论塔板数"+str(i-1)+"个,减去塔釜一个，为"+str(i-2)+"个")
