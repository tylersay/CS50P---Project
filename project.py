import praw
import os
import random


def main():
    reddit = praw.Reddit("bot1")
    subreddit = reddit.subreddit("pythonforengineers")

    posts_replied = check_posts_replied()

    bot_search_and_reply(subreddit, posts_replied)


def check_posts_replied():
    if not os.path.isfile("posts_replied.txt"):
        posts_replied = []
    else:
        with open("posts_replied.txt", "r") as f:
            posts_replied = f.read().split("\n")
            posts_replied = list(filter(None, posts_replied))
            print(f"post replied: {posts_replied}")
            return posts_replied


def bot_search_and_reply(subreddit, post_replied):
    trigger_phrase = ["i love python", "i love turtles"]
    # trigger_phrase = ["my third bot post", "my second bot post"]
    # trigger_phrase = ["bot", "test", "says"]
    reply_text = ["I'm flexing my pythons", "Light weight baby", "Yeah buddy", "The King", "The greatest"]
    sub_ids = []
    #########################################
    #########################################
    for s in subreddit.hot(limit=10):
    # for s in subreddit.stream.submissions():
    # for s in subreddit.comments(limit=1000):
    # for s in subreddit.stream.comments():
    #########################################
    #########################################
        if s.id not in post_replied:
            for t in trigger_phrase:
                if t in s.title.lower():        #submission title
                # if t in s.body.lower():       #comment body
                    print(f"replying to Title:, ID: {s.id}, author: {s.author}")
                    sub_ids.append(s.id)
                    #############################
                    ########## CAUTION ##########
                    s.reply(body = f"Beepboop {random.choice(reply_text)}")
                    #############################
                    update_postsreplied(s.id)
                    break # break prevents matching 2 test_titles in one submission


def update_postsreplied(id):
    with open("posts_replied.txt", "a") as f:
        print(f"update {id}")
        f.write(f"{id}\n")



if __name__ == "__main__":
    main()