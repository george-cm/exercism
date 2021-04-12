from matrix import Matrix

def main():
    m1 = Matrix("1 2 3\n4 5 6\n7 8 9")
    print(m1)
    print("")
    print(m1.transposed_str())
    
    print(m1.column(3))
    m1.column(3)[0] = 0
    print("")
    print(m1)
    print("")
    print(m1.transposed_str())
    print(m1.column(3))

if __name__ == "__main__":
    main()