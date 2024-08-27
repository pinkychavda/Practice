import re
if __name__ == '__main__':
    n = int(input())
for _ in range(n):
    S = input()
    try:
        re.compile(S)
        print("True")
    except:
        print("False")

