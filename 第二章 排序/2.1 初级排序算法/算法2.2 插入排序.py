def less():pass
def exch():pass

class Insertion:
    def sort(a:list)->None:
        # 将a[]按升序排列
        N=len(a)
        for i in range(1,N):
            # 将a[i]插入到a[i-1]、a[i-2]、a[i-3]...之中
            for j in range(i,0,-1):
                if not less(a[j],a[j-1]):
                    break
                exch(a,j,j-1)
    # less()、exch()、isSorted()、main()方法见“排序算法类模板”