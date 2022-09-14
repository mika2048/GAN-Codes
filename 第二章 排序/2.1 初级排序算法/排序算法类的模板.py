class Example:
    def sort(a:list)->None:
        # 请见算法2.1、算法2.2、算法2.3、算法2.4、算法2.5或算法2.7
        pass

    def less(v,w)->bool:
        return v.__le__(w)

    def exch(a:list,i:int,j:int)->None:
        a[i],a[j]=a[j],a[i]

    def show(a:list)->None:
        # 在单行中打印数组
        for i in range(len(a)):
            print(a[i],end=" ")
        print(" ")

    def isSorted(a:list)->bool:
        # 测试数组元素是否有序
        for i in range(1,len(a)):
            if Example.less(a[i],a[i-1]):
                return False
        return True

if __name__=="__main__":
    # 从标准输入读取字符串，将它们排序并输出
    a=input().split(' ')
    Example.sort(a)
    assert Example.isSorted(a)
    Example.show(a)    
