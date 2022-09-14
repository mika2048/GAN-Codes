import timeit
class Insertion:pass
class Selection:pass
class Shell:pass
class Merge:pass
class Quick:pass
class Heap:pass

def time(alg:str,a:list)->float:
    timer=timeit.default_timer()
    if alg=='Insertion':Insertion.sort(a)
    if alg=='Selection':Selection.sort(a)
    if alg=='Shell':Shell.sort(a)
    if alg=='Merge':Merge.sort(a)
    if alg=='Quick':Quick.sort(a)
    if alg=='Heap':Heap.sort(a)
    return timeit.default_timer()-timer