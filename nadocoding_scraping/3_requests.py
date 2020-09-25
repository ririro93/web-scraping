import requests

res = requests.get("https://google.com")
print("status: ", res.status_code)

# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제있음")

res.raise_for_status() # 문제 있으면 바로 코드 종료 됨
print(len(res.text))

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
