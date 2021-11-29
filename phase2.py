def Div(lst, low, high):
    mid = (low + high)//2
    if low > high:
        return ""
    else:
        if mid+1 < len(lst) and lst[mid] > lst[mid+1] and lst[mid] > lst[mid -1]:
            return str(lst[mid]) + " " + Div(lst, low, mid-1) + Div(lst, mid+1, high)
        else:
            return Div(lst, low, mid-1) + Div(lst, mid + 1, high)

def peak(lst):
    if lst == []:
        return "list is empty"
    elif len(lst) in [1, 2]:
        return "No peak"
    else:
        return Div(lst, 0, len(lst))

print(peak([-999, 18, 5, 2, 9, 1, 10, 100, -999]))
