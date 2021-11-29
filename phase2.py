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


lst=[[0,0,0,0,0,0],
     [0,0,1,0,4,0],
     [0,2,0,3,0,0],
     [0,0,5,0,6,0],
     [0,0,0,0,0,0]]
for i in range (0,5):
    print(peak(lst,i))
