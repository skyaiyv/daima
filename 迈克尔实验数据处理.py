import math as m
Ub=0.000024
class A:
    def __init__(self): 
        self.d_1=[]
        self.Ua=0.0000
        self.d_ave=0.0000
    def get_d_(self):
            i=0
            while(i<5): 
                a=float(input("请输入:"))
                # a=a1[i]
                self.d_1.append(a)
                i+=1
    def co(self): 
            sum=0.0
            for i in self.d_1: 
                sum+=i
            self.d_ave=sum/5
            print("d的平均值为:%lf"%self.d_ave)
            print("λ的值为:%lf"%(2*self.d_ave/100))

    def Uyuansuan(self):
            sum=0.0
            # print(self.d_ave)
            for i in self.d_1:  
            #    print(i-self.d_ave)
                sum+=(i-self.d_ave)**2
            self.Ua=m.sqrt(sum/20)
            Ud_1=m.sqrt(m.pow(self.Ua, 2)+m.pow(Ub,2))
            # print(sum)
            print("Ua的值为:%lf"%self.Ua)
            print("Ud_1的值为:%g"%Ud_1)
            print("Uλ的值为:%.0g"%(Ud_1*2/100))
    def main(self):
        self.get_d_()
        self.co()
        self.Uyuansuan()
        
if __name__=="__main__":
       b=A()
       b.main()

