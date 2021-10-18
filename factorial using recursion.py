def fact(n,N):
    if n>=N:
        return n
    else:
        return n*fact(n+1,N)

if __name__ == '__main__':                                                          """hackerrank"""
    N = int(input().strip())

    print(fact(1,N))
