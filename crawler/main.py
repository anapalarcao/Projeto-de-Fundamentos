#Fazer rodar o crawler no modo multithread

import threading
from queue import Queue
import spider
from domain import *
from general import *
from authenticatior_twitter import *
from requests_oauthlib import OAuth1Session
#incializando a api do twitter

session = OAuth1Session(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
response = session.get('https://api.twitter.com/1.1/search/tweets.json?q=%23python') # %23 é o código para "#" na web e o que va ser buscado é guradado nessa variável q
print (response.status_code)
print(requests.utils.quote('#python')) #codifica os caracteres
url =  "https://api.twitter.com/1.1/search/tweets.json?q=%s"
url = url % (requests.utils.quote("#python"))
response = session.get(url)
tweets= json.loads(response.content) #serve para decodificar o conteúdo retornardo já que é uma string no fromato json
print(tweets.keys())

PROJECT_NAME = 'the crawler' #variável constante
HOMEPAGE = 'https://twitter.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
spider.Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


#create worker threads (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


#do the next job in the queue
def work():
    while True:
        url = queue.get()
        spider.Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


#Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

# checa se há itens em queue.txt para aplicar o crawl
def crawl():
    queue_links = file_to_set(QUEUE_FILE)
    if len(queue_links) > 0:
        print(str(len(queue_links))+ 'links in the queue')
        create_jobs()


create_workers()
crawl()