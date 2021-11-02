class Power():
    def power1(self):
        result = 1
        for i in range(self.num):
            result = result*self.number
        print('The {} power of {} is {}:'.format(x.num,x.number,result))
        
x = Power()
x.number = int(input('enter num :'))
x.num = int(input('enter the power of num'))
x.power1()         
        
