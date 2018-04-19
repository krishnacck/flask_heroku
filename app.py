from flask import Flask
import requests
import json
import urllib
import sys
app = Flask(__name__)
 
@app.route("/")
def index():
    url = "http://blog.isochal.com/wp-json/wp/v2/posts/"
    res = ""
    r = requests.get(url)
    po = r.json()
    count = 0
    for i in po:
        # print(i)
        # print("")
        # print("")
        # print("")
        # print("")
        # print("")
        # print("")
        # print(count)
        result = {}
        post = i
        result['post_id'] = post['id']
        post_id = post['id']
        # print (post_id)
        result['published_date'] = post['date']
        result['status'] = post['status']
        result['title'] = post['title']['rendered']
        result['content'] = post['content']['rendered']
        # print (content)
        # sys.exit()
        url = "http://blog.isochal.com/wp-json/wp/v2/categories?post="+str(post_id)
        # print(url)
        r = requests.get(url)
        cate = r.json()
        result['category'] = cate[0]['name']
        url = "http://blog.isochal.com/wp-json/wp/v2/media?parent="+str(post_id)
        r3 = requests.get(url)
        media = r3.json()
        result['image'] = media[0]['guid']['rendered']
        # result = result.append()
        # res = res.append(json.dumps(result))
        # print(result)
        count = count+1
        if len(res)>1:
            res = res, result
        else:
            res = result
        # print (res)
    # res = res, result      
    # print(res) 
    # print (res)
    return json.dumps(res)
 
@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/hello/<string:name>/")
def test(name):
    url = "http://blog.isochal.com/wp-json/wp/v2/posts/"
    res = ""
    r = requests.get(url)
    po = r.json()
    count = 0
    for i in po:
        # print(i)
        # print("")
        # print("")
        # print("")
        # print("")
        # print("")
        # print("")
        # print(count)
        result = {}
        post = i
        result['post_id'] = post['id']
        post_id = post['id']
        # print (post_id)
        result['published_date'] = post['date']
        result['status'] = post['status']
        result['title'] = post['title']['rendered']
        result['content'] = post['content']['rendered']
        # print (content)
        # sys.exit()
        url = "http://blog.isochal.com/wp-json/wp/v2/categories?post="+str(post_id)
        # print(url)
        r = requests.get(url)
        cate = r.json()
        result['category'] = cate[0]['name']
        url = "http://blog.isochal.com/wp-json/wp/v2/media?parent="+str(post_id)
        r3 = requests.get(url)
        media = r3.json()
        result['image'] = media[0]['guid']['rendered']
        # result = result.append()
        # res = res.append(json.dumps(result))
        # print(result)
        count = count+1
        if len(res)>1:
            res = res, result
        else:
            res = result
        # print (res)
    # res = res, result      
    # print(res) 
    # print (res)
    return json.dumps(res)

@app.route("/members")
def members():
    return "Members"
 
@app.route("/members/<string:name>/")
def getMember(name):
    return name
 
if __name__ == "__main__":
    app.run()
    # test(1711)
