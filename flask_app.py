import os

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

app = Flask(__name__)


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


@app.route('/review', methods=['POST', 'GET'])  # route to show the review comments in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            searchString = request.form['content'].replace(" ", "")
            #print(searchString)
            flipkart_url = "https://www.flipkart.com/search?q=" + searchString
            #print(flipkart_url)
            uClient = uReq(flipkart_url)
            flipkartPage = uClient.read()
            #print(flipkartPage)
            uClient.close()
            flipkart_html = bs(flipkartPage, "html.parser")
            #print(flipkart_html)
            bigboxes = flipkart_html.findAll("div", {"class": "_2pi5LC col-12-12"})
            del bigboxes[0:3]
            box = bigboxes[0]
            #print(bigboxes[0])
            productLink = "https://www.flipkart.com" + box.div.div.div.a['href']
            print("-------------Product html-------------")
            #print(productLink)
            prodRes = requests.get(productLink)
            #prodRes.encoding = 'utf-8'
            prod_html = bs(prodRes.text, "html.parser")
            #print(prod_html)
            commentboxes = prod_html.find_all('div', {'class': "_16PBlm"})
            print(commentboxes)
            filename = searchString + ".csv"
            fw = open(filename, "w", encoding='utf-8')
            headers = "Product, Customer Name, Rating, Heading, Comment \n"
            fw.write(headers)
            reviews = []
            print("Reached here -------------")
            for commentbox in commentboxes:
                print(commentbox)
                try:
                    #name.encode(encoding='utf-8')
                    name = commentbox.div.div.find_all('p', {'class': '_3LWZlK _1BLPMq'})[0].text
                    print(name)
                except:
                    name = 'No Name'

                try:
                    # rating.encode(encoding='utf-8')
                    rating = commentbox.div.div.div.div.text


                except:
                    rating = 'No Rating'

                try:
                    # commentHead.encode(encoding='utf-8')
                    commentHead = commentbox.div.div.div.p.text

                except:
                    commentHead = 'No Comment Heading'
                try:
                    comtag = commentbox.div.div.find_all('div', {'class': ''})
                    # custComment.encode(encoding='utf-8')
                    custComment = comtag[0].div.text
                except Exception as e:
                    print("Exception while creating dictionary: ", e)

                mydict = {"Product": searchString, "Name": name, "Rating": rating, "CommentHead": commentHead,
                          "Comment": custComment}
                reviews.append(mydict)
                content = searchString + "," + name + "," + rating+","+commentHead+","+custComment
                print("////////////////////")
                print(content)
                fw.write(content)


            return render_template('results.html', reviews=reviews[0:(len(reviews) - 1)])
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'
    # return render_template('results.html')

    else:
        return render_template('index.html')

#port = int(os.getenv("PORT")) #comment this while running in local
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True) #uncomment this while running in local
    #app.run(host='0.0.0.0', port=port) #comment this while running in local
    # app.run(host='127.0.0.1', port=8001, debug=True) 
