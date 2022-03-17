# coding: utf-8
import json
import time
import requests
import feedparser
feed=feedparser.parse("http://zhihu.com/rss")
def dingding_robot(data):
    webhook = "[your_token_is_here]"
    headers = {'content-type': 'application/json'} 
    r = requests.post(webhook, headers=headers, data=json.dumps(data))
    r.encoding = 'utf-8'
    return (r.text)

if __name__ == "__main__":
    while True:
        for i in range(60):
            print('===========第'+str(i+1)+'篇文章===========')
            print(feed.entries[i].id)
            sendword = '# **[' + feed.feed.title + ']**'+'\n'+'## '+ feed.entries[i].title +'\n'+ str(feed.entries[i].summary)[:100] + '...'
            sendword = sendword.replace('</p>','')
            sendword = sendword.replace('<p>','')
            sendword = sendword.replace('<ul>','')
            sendword = sendword.replace('</ul>','')
            sendword = sendword.replace('<li>','')
            sendword = sendword.replace('</li>','')
            sendword = sendword.replace('<b>','')
            sendword = sendword.replace('</b>','')
            sendword = sendword.replace('<img src="','')
            sendword = sendword.replace('<h1>','')
            sendword = sendword.replace('</h1>','')
            sendword = sendword.replace('<h2>','')
            sendword = sendword.replace('</h2>','')
            sendword = sendword.replace('<h3>','')
            sendword = sendword.replace('</h3>','')
            sendword = sendword.replace('<h4>','')
            sendword = sendword.replace('</h4>','')
            sendword = sendword.replace('<h5>','')
            sendword = sendword.replace('</h5>','')
            sendword = sendword.replace('<h6>','')
            sendword = sendword.replace('</h6>','')
            sendword = sendword.replace('<i>','')
            sendword = sendword.replace('</i>','')
            sendword = sendword.replace('<blockquote>','')
            sendword = sendword.replace('<hr />','')
            sendword = sendword.replace('<hr />','')
            sendword = sendword.replace('<br />','')
            sendword = sendword.replace('<a class=" wrap external" href="','')
            print(sendword)
            data = {
            "actionCard": {
                "title": feed.feed.title + ' - ' + feed.entries[i].title , 
                "text": sendword, 
                    "btnOrientation": "0", 
                "singleTitle" : "了解更多",
                "singleURL" : feed.entries[i].id
            }, 
            "msgtype": "actionCard"
            }
            
            res = dingding_robot(data)
            print(res) 
            time.sleep(3600)
