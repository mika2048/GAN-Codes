def less():pass
def exch():pass
class Selection:
    def sort(a:list)->None:
        N=len(a) # 数组长度
        for i in range(N):
            min=i # 最小元素的索引
            for j in range(i+1,N):
                if less(a[j],a[min]):
                    min=j
            exch(a,i,min)
    # less()、exch()、isSorted()、main()方法见“排序算法类模板”