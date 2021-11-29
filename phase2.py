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
    if lst == []:
        return "list is empty"
    elif len(lst) in [1, 2]:
        return "No peak"
    else:
        return Div(lst, 0, len(lst), c)


lst=[[1,1,1,1,1],
     [1,9,1,5,1],
     [1,1,1,1,1],
     [1,1,1,1,1]]
print(peak(lst, 1))
