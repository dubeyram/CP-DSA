n = int(input())
s = input()
count=0
if "00" not in s and "11" not in s:
    print(0)

else:
    s = list(s)

    for i in range(1,n):
        if s[0]==s[1]!=s[2]:
            s[0]=s[2]
            count +=1
        elif s[i]==s[i-1]=="1":
            s[i]="0"
            print("yes")
            count+=1
        elif s[i]==s[i-1]=="0":
            s[i]="1"
            count+=1
        print(s)
    print(count)