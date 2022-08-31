
A=[[4,2,0],[2,10,4],[0,4,5]]
b=[2,6,5]
def Dominant_diagonal_test(matrix):
    start=0
    for row in range(0,len(matrix)):
        sum = 0
        for col in range(0,len(matrix)):
            sum=sum+matrix[row][col]
        sum-=matrix[start][start]
        if(matrix[start][start]<sum):
            print("Sorry, no Dominant_diagonal_test")
        start+=1
    return True

def gauss_seidel(f1,f2,f3,e):
    #Initial setup
    x0 = 0
    y0 = 0
    z0 = 0
    count = 1
    #Implementation of Gauss Seidel Iteration
    print('\nCount\tx\ty\tz\n')
    condition = True

    while condition:
        x1 = f1(x0, y0, z0)
        y1 = f2(x1, y0, z0)
        z1 = f3(x1, y1, z0)
        print('%d\t%0.10f\t%0.10f\t%0.10f\n' % (count, x1, y1, z1))
        e1 = abs(x0 - x1)
        e2 = abs(y0 - y1)
        e3 = abs(z0 - z1)
        count += 1
        x0 = x1
        y0 = y1
        z0 = z1
        condition = e1 > e and e2 > e and e3 > e

    print('\nSolution: x=%0.10f, y=%0.10f and z = %0.10f\n' % (x1, y1, z1))

    e=1
    x0 = 0
    y0 = 0
    z0 = 0
    c = 0
    while e>0.0000001 and c < 100:
        x1 = f1(x0, y0, z0)
        y1 = f2(x1, y0, z0)
        z1 = f3(x1, y1, z0)
        print('%0.5f\t%0.5f\t%0.5f\t' %(x1, y1, z1))
        e= abs(x0 - x1)
        x0 = x1
        y0 = y1
        z0 = z1
        c += 1

    print('\nSolution: x=%0.5f, y=%0.5f and z = %0.5f\n' % (x1, y1, z1))

def jacobi(f1,f2,f3,e):
    # Initial setup
    x0 = 0
    y0 = 0
    z0 = 0
    count = 1
    print('\nCount\tx\ty\tz\n')
    condition = True
    while condition:
        x1 = f1(x0, y0, z0)
        y1 = f2(x0, y0, z0)
        z1 = f3(x0, y0, z0)
        print('%d\t%0.10f\t%0.10f\t%0.10f\n' % (count, x1, y1, z1))
        e1 = abs(x0 - x1);
        e2 = abs(y0 - y1);
        e3 = abs(z0 - z1);
        count += 1
        x0 = x1
        y0 = y1
        z0 = z1
        condition = e1 > e and e2 > e and e3 > e
    print('\nSolution: x=%0.5f, y=%0.5f and z = %0.5f\n' % (x1, y1, z1))
e = 0.0000001
f1 = lambda x, y, z: (b[0] - y * A[0][1] - z * A[0][2]) / A[0][0]
f2 = lambda x, y, z: (b[1] - x * A[1][0] - z * A[1][2]) / A[1][1]
f3 = lambda x, y, z: (b[2] - x * A[2][0] - y * A[2][1]) / A[2][2]

choose = int(input('Enter the method you want to use (1 for Gauss Seidel, 2 for jacobi): '))
Dominant_diagonal_test(A)
if choose == 1:
    gauss_seidel(f1,f2,f3,e)
if choose == 2:
    jacobi(f1,f2,f3,e)
