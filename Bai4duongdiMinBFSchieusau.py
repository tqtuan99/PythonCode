from os import close, path

G = []
P = []
n = 0


def Split(string):
    k = string.index(' ')
    str = string[0:k]
    a = int(str, base=10)
    m = string.index(' ', k+1, -1)
    str = string[k + 1:m]
    b = int(str, base = 10)
    str = string[m+1:len(string)]
    c = int(str, base=10)
    return a, b, c


def Init(path, G):
    f = open(path)
    string = f.readline()
    string = string.replace('\t', ' ')
    n, a, z = Split(string)
    for i in range(n+1):
        G.append([])
        for j in range(n+1):
            G[i].append(0)
    while(True):
        string = f.readline()
        if not string:
            break
        string = string.replace('\t', ' ')
        i, j, x = Split(string)
        G[i][j] = G[j][i] = x
    f.close()
    return n, a, z


def Check(M, n, u):
    for i in range(1, n+1):
        if M[i] == u:
            return True
    return False


def ViewMatrix(G, n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print("%d" % G[i][j], end=' ')
        print()


def BFS(G, P, n, s, g):
    open = []
    close = []
    for j in range(n+3):
        open.append(0)
        close.append(0)
        P.append(0)
    top = 1
    open[top] = s
    P[s] = s;
    while(top>0):
        u = open[top]
        top = top - 1
        if u == g:
            return 1
        for v in range(1, n+1):
            if G[u][v] != 0 and not Check(open, n, v) and not Check(close, n, v):
                top = top + 1
                open[top] =v;
                P[v] = u;
        close[u] = u;
    return 0


def Print(P, n, s, g):
    path = []
    for i in range(0, n+1):
        path.append(0)
    print("\nDuong di tu %d" % s, "den %d" % g, "la\n", end=' ');
    path[0]  = g
    i = P[g]
    k = 1
    while i != s:
        path[k] = i
        k = k+1
        i = P[i]
    path[k] = s
    for j in range(0, k+1):
        i = k-j
        if i > 0:
            print("%d => " % path[i], end=' ')
        else:
            print("%d" % path[i], end=' ')


def main():
    n, s, g = Init("Bai4thaphanoi.txt", G)
    print("xem ma tran G: %d" %g,end= '\n')
    ViewMatrix(G,n)
    BFS(G, P, n, s, g)
    Print(P, n, s, g)
if __name__ == "__main__":
    main()
