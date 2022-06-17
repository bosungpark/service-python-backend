# pylint: disable=C0103

"""
FUNC navigation(){

    N과 M에 각각 4, 6 지정
    maps = [["☐","◼","☐","☐","☐","☐"],
    ["☐","◼","☐","◼","☐","◼"],
    ["☐","◼","☐","◼","☐","☐"],
    ["☐","☐","☐","◼","☐","☐"]]

    user = "예) 0 0\n  x,y의 형식으로 유저의 좌표를 입력해주세요: " 로 입력받아서 새 리스트 생성, 분할
    store = "예) 5 3\n  x,y의 형식으로 가게의 좌표를 입력해주세요: " 로 입력받아서 새 리스트 생성, 분할

    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    flag = FALSE

    FUNC dfs(node){
        바깥 함수에서 쓰인 flag 변수 쓸 수 있도록

        if flag{
            RETURN}

        x, y = node
        maps[y][x] 을 ˙ 으로 지정
        IF 입력받은 좌표가 store의 x, y 좌표와 같을 경우{
            maps에서 유저의 좌표 🏠 지정
            maps에서 store의 좌표 🍟 지정

            ******************************** 출력
            가능한 경로를 탐색합니다 출력
            ******************************** 출력

            FOR m IN maps{
                m 출력}

            ******************************** 출력
            탐색된 경로를 따라 이동해주세요 출력
            ******************************** 출력
            flag = TRUE
            반환}

        FOR i IN range(4){
            IF x+dx[i]가 M보다 작고 0과 같거나 크고 y+dy[i]가 N보다 작고 0과 같거나 크면{
                IF maps[y+dy[i]][x+dx[i]] 가 "☐"와 같으면{
                    node에 [x+dx[i],y+dy[i]]값 넣어줌}
                    maps[y+dy[i]][x+dx[i]]를 "☐"로 지정}}
    dfs(user)반환}
}
"""


def navigation():
    """
    배달 기사님 혹은 고객님들이 길을 잃어버리지 않도록 경로를 소개해줍니다.
    가능하면 예시에 있는 좌표를 입력하기를 권장드립니다.
    """
    N,M=4,6
    maps=[["☐","◼","☐","☐","☐","☐"],
          ["☐","◼","☐","◼","☐","◼"],
          ["☐","◼","☐","◼","☐","☐"],
          ["☐","☐","☐","◼","☐","☐"]]

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
        maps[y][x]="˙"
        if x==store[0] and y==store[1]:
            maps[user[1]][user[0]]="🏠"
            maps[store[1]][store[0]]="🍟"

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
                if maps[y+dy[i]][x+dx[i]]=="☐":
                    dfs([x+dx[i],y+dy[i]])
                    maps[y+dy[i]][x+dx[i]]="☐"
    return dfs(user)
