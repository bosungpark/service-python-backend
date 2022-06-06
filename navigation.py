def navigation():
    """
    배달 기사님 혹은 고객님들이 길을 잃어버리지 않도록 경로를 소개해줍니다.
    가능하면 예시에 있는 좌표를 입력하기를 권장드립니다.
    """
    N,M=4,6
    maps=[[" ","◼"," "," "," "," "],[" ","◼"," ","◼"," ","◼"],[" ","◼"," ","◼"," "," "],[" "," "," ","◼"," "," "]]

    user=list(map(int,input("예) 0 0\n  x,y의 형식으로 유저의 좌표를 입력해주세요: ").split()))
    store=list(map(int,input("예) 5 3\n  x,y의 형식으로 가게의 좌표를 입력해주세요: ").split()))

    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    flag=False

    def dfs(node):
        nonlocal flag

        if flag:
            return

        x,y=node
        maps[y][x]="😀"
        if x==store[0] and y==store[1]:

            print("********************************")
            print("가능한 경로를 탐색합니다")
            print("********************************")
            for m in maps:
                print(*m)
            print("********************************")
            print("탐색된 경로를 따라 이동해주세요")
            print("********************************")
            flag=True
            return

            
        for i in range(4):
            if 0<=x+dx[i]<M and 0<=y+dy[i]<N:
                if maps[y+dy[i]][x+dx[i]]==" ":
                    dfs([x+dx[i],y+dy[i]])
                    maps[y+dy[i]][x+dx[i]]=" "
    return dfs(user)
