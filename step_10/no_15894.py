# 맨 밑의 사각형의 개수가 층의 수와 같음
# 좌, 우의 사각형 변의 길이 = 층의 수
# 위 아래 사각형 변의 길이 = 맨 밑의 사각형 개수
# 즉, 실선의 길이는 맨 밑의 사각형 개수 * 4
x = int(input())
print(x*4)