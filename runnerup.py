if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    new_list = list(dict.fromkeys(list(arr)))
    new_list = sorted(new_list,reverse=True)
    #5new_list = new_list.sort()
    print(new_list[1])
