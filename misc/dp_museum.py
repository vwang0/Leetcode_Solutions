# 宝物重量及价值
treasure = [{'w':2,'v':3},{'w':3,'v':4},{'w':4,'v':8},{'w':5,'v':8},{'w':9,'v':10}]

# 大盗最大承重和可能拿走的宝物最多件数
max_w, max_num = 20, len(treasure)
# 初始化maxvalue和treasure_used，记录在当前可选宝物范围中，大盗可拿走的最大总价值及对应宝物
mtv = [[0 for i in range(max_w+1)] for j in range(max_num+1)]
treasure_used= [[False for p in range(max_w+1)] for q in range(max_num+1)]
 
# 循环添加宝物至“大盗可选清单”
for i in range(1,max_num+1):
    need_w,get_v = treasure[i-1]['w'],treasure[i-1]['v']  # 添加的宝物的重量和价值
    for j in range(1,max_w+1):
        if i==1:  # 如果清单只有一件宝物
            if j<need_w:  # 如果当前物品重量大于背包容量
                mtv[1][j]=0
            else:  # 如果当前物品可放入背包
                mtv[1][j]=get_v
                treasure_used[1][j] = True
        else:
            if j<need_w:  # 如果当前物品重量大于背包容量
                mtv[i][j]=mtv[i-1][j]  # 和这个物品不存在时一样
            else:  
                # 如果可以放，需要进一步决策：大于上一次选择的最佳方案则更新mtv[i][j]
                treasure_used[i][j] = mtv[i - 1][j - need_w] + get_v> mtv[i - 1][j]
                mtv[i][j]=max(mtv[i-1][j-need_w]+ get_v ,mtv[i-1][j])
                #  记录在mtv[i][j]时是否选择了放入第i-1件宝物
 
print(mtv[max_num][max_w])  # 回溯打印编号
num=max_num
w=max_w
s = ""
while num > 0:
    if treasure_used[num][w]:
        s=s+str(num-1)+" "  # 减一是因为宝物序号是从零开始的
        w = w - treasure[num-1]['w']
        num = num - 1  # 处理依据 mtv[i-1][j-need_w]+ get_v
    else:
        num = num - 1  # 处理依据 mtv[i-1][j]
print(s)