# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]

class a:

    def __init__(self):
        self.H, self.W, self.A, self.B = (map(int, input().split()))
        self.HW = [[0] * self.W] * self.H
        self.Anum = 0
        self.ret = 0

    def tateCheck(self,h, w):
        if self.W - 1 <= w:
            return False
        if self.HW[h][w] == 0 and self.HW[h + 1][w] == 0:
            ret = True
        else:
            ret = False
        return ret

    def yokoCheck(self,h, w):
        if self.W - 1 <= w:
            return False
        if self.HW[h][w] == 0 and self.HW[h][w + 1] == 0:
            ret = True
        else:
            ret = False
        return ret

    def tateume(self):
        for h in range(self.H):
            for w in range(self.W):
                if self.tateCheck(h, w) == True:
                    self.HW[h, w] = 1
                    self.HW[h + 1, w] = 1
                    self.Anum += 1
                    if self.Anum == self.A:
                        self.ret += 1
                    else:
                        # self.tateume()
                        None
                    Anum -= 1
                    HW[h, w] = 0
                    HW[h + 1, w] = 0

    def debugprint():
        for w in HW:
            print(w)
    def rtnprint():
        print(rtn)


a = a()
a.debugprint()
a.tateume()
a.rtnprint()


