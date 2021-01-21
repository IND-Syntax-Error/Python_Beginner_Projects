pos = -1

def search(list, n):

    x = 0
    y = len(list)-1

    while x <= y:
        mid = (x+y) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                x = mid+1;
            else:
                y = mid-1;

    return False


list = [4,7,8,12,45,99]
n = 45

if search(list, n):
    print("Found at ",pos+1)
else:
    print("Not Found")