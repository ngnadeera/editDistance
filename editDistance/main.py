
def computeEditDistance (s,t):
    cache = {}

    '''

    :param s: s word
    :param t: t word
    :return: minimum number of letters needed to be changed in order to make s equal to t
    '''

    def recurse(m,n):

        if (m,n) in cache:
            return cache[(m,n)]

        '''

        :param m: len of s
        :param n: len of t
        :return: minimum number of letters needed to be changed in order to make s equal to t
        '''

        if m == 0:
            return n
        elif n == 0:
            return m
        elif s[m-1] == t[n-1]:
            return recurse(m-1,n-1)
        else:
            subCost = 1 + recurse(m-1,n-1)
            insCost = 1 + recurse(m,n-1)
            delCost = 1 + recurse(m-1,n)

            result = min(subCost,insCost,delCost)
        cache[(m,n)] = result
        return result
    return recurse(len(s),len(t))


if __name__ == '__main__':
    result = computeEditDistance("cat", "cats")
    print("result: ", result)



