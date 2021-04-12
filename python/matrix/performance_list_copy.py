from timeit import timeit
from datetime import timedelta
from dis import dis

# create a huge list
lst = [i for i in range(1_000_000)]

def list_copy(lst):
    # global lst
    return lst.copy()

def list_slice(lst):
    # global lst
    return lst[:]

def list_list(lst):
    # global lst
    return list(lst)

if __name__ == "__main__":    
    iterations = 1_00
    print("Testing duration of copying a list using list.copy() method and slicing.\n")
    
    d_copy = timedelta(seconds=timeit('list_copy(lst)', number=iterations, globals=globals()))
    print(f"Duration using list.copy() method: {str(d_copy)}")
    print(dis(list_copy))
    
    print("")
    
    d_slice = timedelta(seconds=timeit('list_slice(lst)', number=iterations, globals=globals()))
    print(f"Duration using list slice method: {str(d_copy)}")
    print(dis(list_slice))
    print("")
    
    d_slice = timedelta(seconds=timeit('list_list(lst)', number=iterations, globals=globals()))
    print(f"Duration using list() method: {str(d_copy)}")
    print(dis(list_list))

