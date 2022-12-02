# CS50P Project - Building a Reddit Bot

![Tylers's CS50 Python certifcate.](https://certificates.cs50.io/d8d2d726-c0a4-4606-a939-44beed8d0eec.png?size=letter "Tyler's cs50p cert")
<br><br>
This is my project for  [CS50P (2022) Harvard OpenCourseWare](https://cs50.harvard.edu/python/2022/), check out what's required to acheive the certificate. <br> 
Also, look at [my other CS50P repo](https://github.com/tylersay/CS50P) for the coursework, and my take on the problem sets.
<br><br>
For this project, I made a reddit bot that monitors Reddit, and post replies to reddit submissions.
### [Click here for 3min video demo](https://youtu.be/TMAgoZ9I5Ts)
<br><br>
## Technologies Used
### Python
This is an obvious one. Python.
### PRAW library
[Python Reddit API Wrapper ("PRAW")](https://praw.readthedocs.io/en/stable/index.html) is the main library, the engine that is driving our project. I stand on the shoulder of this giant, to ~~troll~~ automate replies to reddit.
<br><br>
> WARNING!!!
>Reddit, like all websites, has [**rules for scraping**](https://github.com/reddit-archive/reddit/wiki/API).
>Bots can make thousands of requests a second, and it's not nice to overload servers. Ignore the rules at your own peril!!!
<br>


<br><br>
## After Action Review
### What happened:
This project seems simple, using some of the topics like opening and writing files. The PRAW library handled the Reddit API without me having to parse and drill into the JSON file returned.
### Why was there an error:
My reddit account did not have enough "reputation" to post comments in such frequency, so I had to set a longer time-out. (Reddit's API calling requirements vs more stringent commenting requirements.)
### What could be done better:
There are other functionallities of PRAW not explored; I could use the bot for comment extracting and parsing, without commenting, to circumvent the Reddit "account reputation" requirements. 
<br><br>
Practical use-case includes: with a defined list, count instances popular stocks/shares being discussed, which senator/representative is being discussed in reddit
