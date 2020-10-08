# Flipkart ReviewScrapper

Hosted on [http://reviewscrapper-bold-grysbok-nk.cfapps.io/](http://reviewscrapper-bold-grysbok-nk.cfapps.io/) <br/>
The goal here originally was to create a dataset of flipkart reviews in the form of csv files  which can be further used for sentiment analysis. In addition, scrapped reviews are shown on the webpage using flask and csv files are formed when you execute this project in your system.

# Project Flow:

```mermaid
graph TD
A[Search on UI i.e index.html based on some keyword such as 'oneplus']  --> B[Pass this keyword 'oneplus' to the flipkart search url ] 

B --> C[Click on the first search result of flipkart]
C-->D[Go to the product and navigate to the Review Section]
D-->E[Scrap the reviews and write them in csv file ]
E-->F[Display them on result.html page]

```

# Prerequisites:

The things needed for executing this  python based web scraper are:<br/>
• Python (3.x) installed.<br/>
• Anaconda installed.<br/>
• A Python IDE (Integrated Development Environment): like PyCharm, Spyder, or any
other IDE of choice.<br/>
• Flask Installed. (A simple command: pip install flask)<br/>
• Basic understanding of Python and HTML.<br/>

## Steps to execute this project in Pycharm/Anaconda Environment:

1. Create a new project in Pycharm.<br/>
2. Make sure you select **New environment using :Conda**<br/>
3. Click create and right click on the project name and select **Show In Explorer** option and go inside project name folder.<br/>
4. Download this project and copy paste all these files into your flask project folder.<br/>
5. Go to pycham terminal and type the following command:
	
	pip install -r requirements.txt
	
This command will install all the libraries such as flask,beautiful soup,etc. required to execute this project.<br/>
6.Right click on flask_app.py file and select Run option.
****

