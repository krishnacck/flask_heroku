from flask import Flask
import requests
import json
import urllib
import sys
app = Flask(__name__)
 
@app.route("/")
def index():
    url = "https://blog.isochal.com/wp-json/wp/v2/posts/"
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
        try:
        	result['post_id'] = post['id']
        except:
        	result = ""
        try:
        	post_id = post['id']
        except:
        	post_id = ""
        # print (post_id)
        try:
        	result['published_date'] = post['date']
        except:
        	result['published_date'] = ""
        try:
        	result['status'] = post['status']
        except:
        	result['status'] = ""
        try:        	
        	result['title'] = post['title']['rendered']
        except:
        	result['title'] = ""
        try:
        	result['content'] = post['content']['rendered']
        except:
        	result['content'] = ""
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
        try:
        	result['image'] = media[0]['guid']['rendered']
        except:
        	result['image'] = ""
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
#    app.run()
    app.run(host='0.0.0.0', port=5050)
    # test(1711)
