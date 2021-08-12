for _ in range(int(input())):               # for each element in range 0 and input
    n = int(input())                        # read n as integer input
    A = list(map(int, input().split()))     # read the splitted inputs and typecast it to list 
    print(min(A) * (n - 1))                 #print the product of minimum element of A and n-1