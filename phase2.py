import np as numpy
class matrix:
    def __init__(self, data, row, column):
        self.data=data
        self.row=row
        self.column=column

    def set():
        for counter1 in range(0,row+2):
            for counter2 in range(0,column+2):
                if counter1==0 or counter2==0 or counter1==row+1 or counter2==column+1:
                    data[counter1][counter2]=float('-inf')
                else:
                    data[counter1][counter2]=input()

    def Div(lst, low, high, c):
        mid = (low + high)//2
        if low > high:
            return ""
        else:
            if mid+1 < len(lst) and lst[mid][c] > lst[mid+1][c] and lst[mid][c] > lst[mid -1][c] and lst[mid][c] > lst[mid][c + 1] and lst[mid][c] > lst[mid][c - 1]:
                return str(lst[mid][c]) + " " + Div(lst, low, mid-1, c) + Div(lst, mid+1, high, c)
            else:
                return Div(lst, low, mid-1, c) + Div(lst, mid + 1, high, c)

    def peak(lst, c):
        return Div(lst, 0, len(lst), c)



r=int(input())
c=int(input())
d = np.zeros( (r+2, c+2) )

for counter1 in range(0,r+2):
    for counter2 in range(0,c+2):
        if counter1==0 or counter2==0 or counter1==row+1 or counter2==column+1:
            d[counter1][counter2]=-99999
        else:
            d[counter1][counter2]=input()
print()

m1=matrix(d,r,c)
print(m1.peak(d,c))
