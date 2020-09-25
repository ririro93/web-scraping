import time

from get_corona_news import get_corona_news
from send_email import send_email
from get_former_news import write_news, read_news

# init
starttime = time.time()
N = 300
title_list = read_news()
cnt = 0

# activate after every N seconds
while True:
    # get data ready from email
    cnt += 1
    curr_list, title_list = get_corona_news(title_list, cnt)
    write_news(title_list)
    print("curr_list: ", len(curr_list))
    print("title_list: ", len(title_list))
    if curr_list:
        data_str = "</br>".join(list(map(str,curr_list)))
        subject = "Army Corona News"
        sender = 'jh moon <ririro0708@gmail.com>'
        receiver_list = ["iop5632@gmail.com"]

        # send email with the data
        send_email(data_str, subject, sender, receiver_list)
        localtime = time.asctime(time.localtime(time.time()))
        print(localtime, f": email sent to {receiver_list}!")
        
    # repeat after N seconds
    time.sleep(N - ((time.time() - starttime) % N))