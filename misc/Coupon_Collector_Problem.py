'''
Coupon Collector Problem Monte Carlo simulation

'''
import random
class Solution:
    def collect_coupon(N, coupNum):
        '''
        Monte Carlo simulation of Coupon Collector’s Problem
        N: number of times you run the experiment
        coupNum: number of different coupons
        
        output:
        Expected number of coupons to buy to complete a collection
        '''
        sum = 0
        for i in range(N):
            count = 0
            a=[]
            flag =1
            while flag:
                x=random.randint(1,coupNum)
                count += 1
                if x not in a:
                    a.append(x)
                    flag = 1
                elif len(a)==coupNum:
                    flag=0
            sum = sum+count
            del a[:]
        return sum/N

a = Solution()
a.collect_coupon(1000000,3)

