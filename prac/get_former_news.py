import os

# directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
fname = "corona_news.txt"
f_path = os.path.join(BASE_DIR, fname)

def write_news(new_news):
    former_news = read_news()
    new_news = list(set(former_news)|set(new_news))
    
    with open(f_path, 'w') as f:
        f.writelines(f"{line}\n" for line in new_news)

        
def read_news():
    with open(f_path, 'r') as f:
        former_news = []
        for line in f.readlines():
            former_news.append(line[:-1])
        return former_news