import random
import time
import csv


fields = ['Example No', 'Time', 'Input Size']
rows = []


def ruzzo_tompa(scores, input_name):
    start = time.time_ns() / (10 ** 9)
    #start = time.time()
    # Use a breakpoint in the code line below to debug your script.
    """Ruzzo–Tompa algorithm."""

    k = 0
    total = 0
    # Allocating arrays of size n
    I, L, R, Lidx = [[0] * len(scores) for _ in range(4)]
    for i, s in enumerate(scores):
        total += s
        # print("total=", total)
        if s > 0:
            # store I[k] by (start,end) indices of scores
            I[k] = (i, i + 1)
            Lidx[k] = i
            L[k] = total - s
            R[k] = total

            #print("Pass #", i)
            #print("total:", total, "-", "s:", s, " = ", total - s)
            #print("k=", k)
            #print("I: ", I, " I[k]: ", I[k])
            #print("Lidx: ", Lidx, " Lidx[k]: ", Lidx[k])
            #print("L: ", L, " L[k]: ", L[k])
            #print("R: ", R, " R[k]: ", R[k])

            while True:
                #print("L: ", L)
                #print("R: ", R)
                maxj = None
                for j in range(k - 1, -1, -1):
                    #print("J: ", j, " k: ", k)
                    if L[j] < L[k]:
                        maxj = j
                        #print("L[j]=", L[j], "<", "L[k]=", L[k], " : ", maxj)
                        break
                if maxj is not None and R[maxj] < R[k]:
                    I[maxj] = (Lidx[maxj], i + 1)
                    R[maxj] = total
                    k = maxj
                    #print("I[maxj]=", I[maxj])
                    #print("R[maxj]=", R[maxj])
                    #print("k=", k)
                else:
                    k += 1
                    break
    # Getting maximal subsequences using stored indices
    #print("total: ", total)

    #end = time.time()
    end = time.time_ns() / (10 ** 9)
    run_time = end - start
    #print("execution time: ", run_time)

    #rows.append([input_name, str(run_time)])

    return [scores[I[l][0]: I[l][1]] for l in range(k)]


def homework1(n):
    Lockers = [0] * (n+1)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j % i == 0:
                if Lockers[j] == 0:
                    Lockers[j] = 1
                else:
                    Lockers[j] = 0
                print(Lockers, " I: ", i, " J: ", j)

    print("Lockers: ", Lockers[1:])


def homework2(A, B, n):
    A.reverse()
    B.reverse()
    a, b, c1 = 0, 0, 0
    C = [0] * (n + 1)
    for i in range(n):
        a += A[i] * pow(2, i)
        b += B[i] * pow(2, i)

    c1 = a + b
    j = 0
    while c1 > 0:
        C[j] = (c1 % 2)
        c1 //= 2
        j += 1
    C.reverse()
    return C


def homework5_BF(input):
    substrings = []
    for i in range(len(input)):
        if input[i] == 'a':
            temp = []
            for j in range(i, len(input)):
                temp.append(input[j])
                if input[j] == 'b':
                    substrings.append(temp.copy())

    return len(substrings)


def homework5_EF(input):
    a_total, substr_count = 0, 0
    for i in range(len(input)):

        if input[i] == 'a':
            a_total += 1

        if input[i] == 'b':
            substr_count = substr_count + a_total

    return substr_count


def write_to_csv(data):
    filename = "ruzzo_tompa_runtimes6.csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(data)

    rows = []


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    example1 = [4, -5, 3, -3, 1, 2, -2, 2, -2, 1, 5]
    example2 = [0, 0, 0, 0, 0]
    example3 = [1, 2, 3, 4, 5]
    example4 = [-1, -1, -1, -1, -1]
    example5 = [-1, -2, -3, -4, -5]

    ex1 = [1]
    start = time.time_ns() / (10 ** 9)
    test = ruzzo_tompa(ex1, 'example1')
    #print(test)
    end = time.time_ns() / (10 ** 9)
    run_time = end - start
    rows.append(['example1', str(run_time), '1'])
    #write_to_csv(rows)

    ex2 = [-1, 2]
    start = time.time_ns() / (10 ** 9)
    test = ruzzo_tompa(ex2, 'example2')
    #print(test)
    end = time.time_ns() / (10 ** 9)
    run_time = end - start
    rows.append(['example2', str(run_time), '2'])
    #write_to_csv(rows)

    ex3 = []
    for i in range(10):
        ex3.append(random.randint(-5, 5))

    start = time.time_ns() / (10 ** 9)
    #print("example 3: ", ex3)
    test = ruzzo_tompa(ex3, 'example3')
    #print(test)
    end = time.time_ns() / (10 ** 9)
    run_time = end - start
    rows.append(['example3', str(run_time), '10'])
    #write_to_csv(rows)

    avg_run_time = 0.0
    for j in range(100):
        ex3 = []
        for i in range(100):
            ex3.append(random.randint(-5, 5))

        start = time.time_ns() / (10 ** 9)
        #print("example 4: ", ex3)
        test = ruzzo_tompa(ex3, 'example4')
        #print(test)
        end = time.time_ns() / (10 ** 9)
        run_time = end - start
        avg_run_time += run_time
    avg_run_time = avg_run_time / 100
    rows.append(['example4', str(avg_run_time), '100'])
    print(f"Average execution time {str(100)}: ", avg_run_time)
    #write_to_csv(rows)

    avg_run_time = 0.0
    for j in range(100):
        ex3 = []
        for i in range(1000):
            ex3.append(random.randint(-5, 5))

        start = time.time_ns() / (10 ** 9)
        #print("example 5: ", ex3)
        test = ruzzo_tompa(ex3, 'example5')
        #print(test)
        end = time.time_ns() / (10 ** 9)
        run_time = end - start
        avg_run_time += run_time
    avg_run_time = avg_run_time / 100
    rows.append(['example5', str(avg_run_time), '1000'])
    print(f"Average execution time {str(1000)}: ", avg_run_time)
    #write_to_csv(rows)

    avg_run_time = 0.0
    for j in range(100):
        ex3 = []
        for i in range(int((10000-1000)/2)):
            ex3.append(random.randint(-5, 5))

        start = time.time_ns() / (10 ** 9)
        # print("example 5: ", ex3)
        test = ruzzo_tompa(ex3, 'example6')
        # print(test)
        end = time.time_ns() / (10 ** 9)
        run_time = end - start
        avg_run_time += run_time
    avg_run_time = avg_run_time / 100
    rows.append(['example6', str(avg_run_time), str(int((10000-1000)/2))])
    print(f"Average execution time {str(int((10000-1000)/2))}: ", avg_run_time)
    #write_to_csv(rows)

    avg_run_time = 0.0
    for j in range(100):
        ex3 = []
        for i in range(10000):
            ex3.append(random.randint(-5, 5))

        start = time.time_ns() / (10 ** 9)
        #print("example 6: ", ex3)
        test = ruzzo_tompa(ex3, 'example7')
        #print(test)
        end = time.time_ns() / (10 ** 9)
        run_time = end - start
        avg_run_time += run_time
    avg_run_time = avg_run_time / 100
    rows.append(['example7', str(avg_run_time), '10000'])
    print(f"Average execution time {str(10000)}: ", avg_run_time)
    #write_to_csv(rows)

    avg_run_time = 0.0
    for j in range(100):
        ex3 = []
        for i in range(int((100000 - 10000)/2)):
            ex3.append(random.randint(-5, 5))

        start = time.time_ns() / (10 ** 9)
        #print("example 7: ", ex3)
        test = ruzzo_tompa(ex3, 'example8')
        #print(test)
        end = time.time_ns() / (10 ** 9)
        run_time = end - start
        avg_run_time += run_time
    avg_run_time = avg_run_time / 100
    rows.append(['example8', str(avg_run_time), str(int((100000 - 10000)/2))])
    print(f"Average execution time {str(int((100000 - 10000)/2))}: ", avg_run_time)
    #write_to_csv(rows)

    avg_run_time = 0.0
    for j in range(100):
        ex3 = []
        for i in range(100000):
            ex3.append(random.randint(-5, 5))

        start = time.time_ns() / (10 ** 9)
        #print("example 7: ", ex3)
        test = ruzzo_tompa(ex3, 'example9')
        #print(test)
        end = time.time_ns() / (10 ** 9)
        run_time = end - start
        avg_run_time += run_time
    avg_run_time = avg_run_time / 100
    rows.append(['example9', str(avg_run_time), '100000'])
    print(f"Average execution time {str(100000)}: ", avg_run_time)
    #write_to_csv(rows)

    avg_run_time = 0.0
    for j in range(100):
        ex3 = []
        for i in range(int((1000000-100000)/2)):
            ex3.append(random.randint(-5, 5))

        start = time.time_ns() / (10 ** 9)
        #print("example 7: ", ex3)
        test = ruzzo_tompa(ex3, 'example10')
        #print(test)
        end = time.time_ns() / (10 ** 9)
        run_time = end - start
        avg_run_time += run_time
    avg_run_time = avg_run_time / 100
    rows.append(['example10', str(avg_run_time), str(int((1000000-100000)/2))])
    print(f"Average execution time {str(int((1000000-100000)/2))}: ", avg_run_time)
    #write_to_csv(rows)

    avg_run_time = 0.0
    for j in range(100):
        ex3 = []
        for i in range(1000000):
            ex3.append(random.randint(-5, 5))

        start = time.time_ns() / (10 ** 9)
        #print("example 8: ", ex3)
        test = ruzzo_tompa(ex3, 'example11')
        #print(test)
        end = time.time_ns() / (10 ** 9)
        run_time = end - start
        avg_run_time += run_time
    avg_run_time = avg_run_time / 100
    rows.append(['example11', str(avg_run_time), '1000000'])
    print(f"Average execution time {str(1000000)}: ", avg_run_time)
    #write_to_csv(rows)

    avg_run_time = 0.0
    for j in range(100):
        ex3 = []
        for i in range(int(1000000/2)):
            ex3.append(random.randint(-5, 5))

        start = time.time_ns() / (10 ** 9)
        # print("example 8: ", ex3)
        test = ruzzo_tompa(ex3, 'example12')
        # print(test)
        end = time.time_ns() / (10 ** 9)
        run_time = end - start
        avg_run_time += run_time
    avg_run_time = avg_run_time / 100
    rows.append(['example12', str(avg_run_time), str(int(1000000/2))])
    print(f"Average execution time {str(int(1000000/2))}: ", avg_run_time)
    #write_to_csv(rows)

    write_to_csv(rows)
    # print(test)

    # homework1(10)
    # print(homework2([0,1,1], [0,0,1], 3))
    # print(homework5_BF(['c','a','b','a','a','x','b','y','a']))
    # print(homework5_EF(['c','a','b','a','a','x','b','y','a']))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
