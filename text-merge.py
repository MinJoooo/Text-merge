
# 여러 줄로 구성된 문장을 (before_file.txt라는 이름으로 작성되어 있어야 함)
# 한 줄로 구성된 문장으로 바꿔줌 (after_file.txt라는 이름으로 완성)

i = 0

while True:
    f1 = open("before_file.txt", "r", encoding='UTF8')
    line = f1.readlines()[i:i+1]        # i+1번째 줄만 읽음
    if not line: break                  # 더 이상 줄이 없으면 끝남
    f1.close()

    line = str(line[0])
    line = line.replace("\n", " ")      # 개행문자를 띄어쓰기로 변환

    f2 = open("after_file.txt", "a", encoding='UTF8')
    f2.write(line)
    f2.close()

    i = i + 1
