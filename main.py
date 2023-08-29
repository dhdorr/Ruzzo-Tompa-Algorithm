def ruzzo_tompa(scores):
    # Use a breakpoint in the code line below to debug your script.
    """Ruzzo–Tompa algorithm."""
    k = 0
    total = 0
    # Allocating arrays of size n
    I, L, R, Lidx = [[0] * len(scores) for _ in range(4)]
    for i, s in enumerate(scores):
        total += s
        print("total=", total)
        if s > 0:
            # store I[k] by (start,end) indices of scores
            I[k] = (i, i + 1)
            Lidx[k] = i
            L[k] = total - s
            R[k] = total

            print("Pass #", i)
            print("total:", total, "-", "s:", s, " = ", total - s)
            print("k=", k)
            print("I: ", I, " I[k]: ", I[k])
            print("Lidx: ", Lidx, " Lidx[k]: ", Lidx[k])
            print("L: ", L, " L[k]: ", L[k])
            print("R: ", R, " R[k]: ", R[k])

            while True:
                maxj = None
                for j in range(k - 1, -1, -1):
                    print("J: ", j, " k: ", k)
                    if L[j] < L[k]:
                        maxj = j
                        print("L[j]=", L[j], "<", "L[k]=", L[k], " : ", maxj)
                        break
                if maxj is not None and R[maxj] < R[k]:
                    I[maxj] = (Lidx[maxj], i + 1)
                    R[maxj] = total
                    k = maxj
                    print("I[maxj]=", I[maxj])
                    print("R[maxj]=", R[maxj])
                    print("k=", k)
                else:
                    k += 1
                    break
    # Getting maximal subsequences using stored indices
    return [scores[I[l][0]: I[l][1]] for l in range(k)]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Input: ", [4, -5, 3, -3, 1, 2, -2, 2])
    test = ruzzo_tompa([4, -5, 3, -3, 1, 2, -2, 2])
    print(test)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
