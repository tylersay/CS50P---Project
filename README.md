# CS50P Project - Building a Reddit Bot
A software bot is a program that can interact with websites autonomously.<br><br>
This bot runs in the background and monitors subreddit *Gainit*.And when it sees certain titles, it can reply to it.<br>
#### WARNING!!!
Reddit, like all websites, has [**rules for scraping**](https://github.com/reddit-archive/reddit/wiki/API). <br><br>
Bots can make thousands of requests a second, and it's not nice to overload servers. Ignore the rules at your own peril!!!
Two of the more pertinent ones are:
> 1. Clients connecting via OAuth2 may make up to 60 requests per minute. Monitor the following response headers to ensure that you're not exceeding the limits<br>
> 2. NEVER lie about your user-agent. This includes spoofing popular browsers and spoofing other bots. We will ban liars with extreme prejudice.<br>
>> In computing, a [**user agent**](https://en.wikipedia.org/wiki/User_agent) is any software, acting on behalf of a user, which "retrieves, renders and facilitates end-user interaction with Web content". A user agent is therefore a special kind of software agent.

<br><br>

## Technologies Used
#### Python
This is an obvious one. Python.
#### PRAW library
[Python Reddit API Wrapper ("PRAW")](https://praw.readthedocs.io/en/stable/index.html) is the main library, the engine that is driving our project. I stand on the shoulder of this giant, to ~~troll~~ automate replies to reddit.
