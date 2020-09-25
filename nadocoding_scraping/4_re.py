# https://www.youtube.com/watch?v=yQ20jZwDjTE&list=PLMsa_0kAjjrd8hYYCwbAuDsXZmHpqHvlV&index=4
import re

# ^ : 문자의 시작을 의미  ex).  (^de) -> destination, desk | fade
# . : 하나의 문자를 의미  ex).  (ca.e) -> care, cave, cafe | caffe
# $ : 문자의 끝을 의미    ex). (se$) -> case, base | face

p = re.compile("ca.e") 

def print_match(m):
    if m:
        print("m.group(): ", m.group()) # 일치하는 문자열 반환
        print("m.string(): ", m.string) # 입력받은 문자열
        print("m.start(): ", m.start()) # 일치하는 문자열의 시작 index
        print("m.end(): ", m.end()) # 일치하는 문자열의 끝 index
        print("m.span(): ", m.span()) # 일치하는 문자열의 시작 / 끝 index
    else:
        print("NO MATCH")

# m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인 -> care
# print_match(m)

# m = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인 -> care
# print_match((m))

lst = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)

########################## 정리
# 1. p = re.compile("원하는 형태")
# 2. m = p.match, p.search, p.findall 사용
