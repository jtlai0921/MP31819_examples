'''
n為球的數目
m為盒子數目
box_list為紀錄各個盒子串列所放入球的個數
當m=1表示此盒子串列只有一個元素:
  例如[3]表示這個盒子放入3顆球
當m=2表示此盒子串列有二個盒:
  例如[1,2]表示第1個盒子放入1顆球,
            第2個盒子放入2顆球
當m=3表示此盒子串列有三個盒子:
  例如[1,2,0]表示第1個盒子放入1顆球,
               第2個盒子放入2顆球,
               第3個盒子放入0顆球
  例如[3,0,0]表示第1個盒子放入3顆球,
               第2個盒子放入0顆球,
               第3個盒子放入0顆球
index是用來作為盒子串列的索引
'''
def ball_to_box(n,m,box_list,index):
    if m==0: #如果只有一個盒子則所有球全部放入
        box_list[index]=n
        print(box_list)
        return
    for i in range(n+1):
        box_list[index]=i
        ball_to_box(n-i,m-1,box_list,index+1)
n=1  #預設至少一顆球
while n!=0:
    n=int(input('請輸入球的數目: '))
    m=int(input('請輸入盒子數目: '))
    box_list=[0 for i in range(0,m)] #每個盒子歸零
    ball_to_box(n,m-1,box_list,0)
    again=input('是否要繼續 y 或 n ?')
    if again==('n' or 'N'):
        break
print('歡迎您的使用,程式結束!!!')
