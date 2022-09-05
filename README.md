# CS50P Project - Building a Reddit Bot
This is my project for  [CS50P (2022) Harvard OpenCourseWare.](https://cs50.harvard.edu/python/2022/). Shortcut to [project requirements here](https://cs50.harvard.edu/python/2022/project/).<br> 
Also, look at [my other CS50P repo](https://github.com/tylersay/CS50P) for the coursework, and my take on the problem sets.
<br><br>
For this project, I made a reddit bot that monitors Reddit, and post replies to reddit submissions.

#### [Click here for 3min video demo](https://youtu.be/TMAgoZ9I5Ts)
<br><br>
## Technologies Used
#### Python
This is an obvious one. Python.
#### PRAW library
[Python Reddit API Wrapper ("PRAW")](https://praw.readthedocs.io/en/stable/index.html) is the main library, the engine that is driving our project. I stand on the shoulder of this giant, to ~~troll~~ automate replies to reddit.
<br><br>
#### WARNING!!!
Reddit, like all websites, has [**rules for scraping**](https://github.com/reddit-archive/reddit/wiki/API). <br><br>
Bots can make thousands of requests a second, and it's not nice to overload servers. Ignore the rules at your own peril!!!
Two of the more pertinent ones are:
> 1. Clients connecting via OAuth2 may make up to 60 requests per minute. Monitor the following response headers to ensure that you're not exceeding the limits<br>
> 2. NEVER lie about your user-agent. This includes spoofing popular browsers and spoofing other bots. We will ban liars with extreme prejudice.<br>
>> In computing, a [**user agent**](https://en.wikipedia.org/wiki/User_agent) is any software, acting on behalf of a user, which "retrieves, renders and facilitates end-user interaction with Web content". A user agent is therefore a special kind of software agent.

<br>


<br><br>
## After Action Review
#### What happened:
This project seems simple, using some of the topics like opening and writing files. The PRAW library handled the Reddit API without me having to parse and drill into the JSON file returned.
#### Why was there an error:
My reddit account did not have enough "reputation" to post comments in such frequency, so I had to set a longer time-out. (Reddit's API calling requirements vs more stringent commenting requirements.)
#### What could be done better:
There are other functionallities of PRAW not explored; I could use the bot for comment extracting and parsing, without commenting, to circumvent the Reddit "account reputation" requirements. 
<br><br>
Practical use-case includes: with a defined list, count instances popular stocks/shares being discussed, which senator/representative is being discussed in reddit