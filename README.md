# ManMetHacks-2.0
Sentiment analysis of daily news using python

Instructions

To run the program:
- Place all the files in the same folder
- Execute the Main file.
- Necessary libraries: requests, newspaper

To use the program:
- We recomend the website: https://www.ccn.com/ to try the progam quickly.
- Another good website is: https://www.marketwatch.com/
- You can try other newspaper websites however some will take a while.
- It is very imporpant to input the complete url.

Understanding the program:
A positive score indicates positive sentiment and vice-versa.
This is a collaborative project between Ivan Baeza and Juan del Aguila.

This project aims to develop a program that lets the user know the daily facts quicker than a manual check. The user will be asked to introduce the URL of the newspaper of your choice. Once introduced, the program will scan every headline and tell the user which of the Fortune 500 companies are mentioned the most. The user would then proceed to point out which company he is most interested in. The program would then ask which of the headlines in which the company is mentioned the user is most interested in.

Once selected the article, then the main purpose of the programe would come to use. The program will analyze the article, and compare the words appearing in the article with a database which gives the main words of the alphabet a number between -5 and 5 depending on the positive or negative feeling attached to that word. By comparing to this database the program will give the article a score representing how positive or negative the article feels about that company, as well as a selection of the 3 sentences with the most positive and negative feelings attached so that the user can see the highlights of the article in a quick manner.

For trying the program, we would recommend using a webpage such as "https://www.ccn.com/"; as it has a limited number of articles with a high mention of companies. Otherwise, depending on the number of articles on the webpage, it might take longer to process the webpage. Webpages with more than 100 articles will be limited to analyze the first 100 articles.
