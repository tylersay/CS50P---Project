import praw
import os
import random


def main():
    reddit = praw.Reddit("bot1")
    posts_replied = check_posts_replied()
    subreddit = reddit.subreddit("pythonforengineers")
    # look for discussions in the "hot" tab, "hot" means poplar
    submission_ids = find_hot(subreddit, posts_replied)
    # find_hot(subreddit)
    print(submission_ids)
    # print(reddit.user.me())
    # posts_replied.append(submission_id)
    update_postsreplied(submission_ids)

def update_postsreplied(sub_ids):
    with open("posts_replied.txt", "a") as f:
        for id in sub_ids:
            f.write(f"{id}\n")

def check_posts_replied():
    if not os.path.isfile("posts_replied.txt"):
        posts_replied = []
    else:
        with open("posts_replied.txt", "r") as f:
            posts_replied = f.read().split("\n")
            posts_replied = list(filter(None, posts_replied))
            print(posts_replied)
            return posts_replied


def find_hot(subreddit, post_replied):
    # questions = ["transformation", "bulk or cut"]
    test_qn = ["i love python", "i love turtles"]
    reply_text = ["I'm flexing my pythons", "Light weight baby", "Yeah buddy", "The King"]
    sub_ids = []
    # for submission in subreddit.stream.submissions():
    for submission in subreddit.hot(limit=10):
        if submission.id not in post_replied:
            for qn in test_qn:
                if qn in submission.title.lower():
                    #############################
                    ########## CAUTION ##########
                    # submission.reply(random.choice(reply_text))
                    #############################
                    print(f"replying to Title: {submission.title}")
                    print(f"ID: {submission.id}")
                    sub_ids.append(submission.id)
                    break # break prevents matching 2 qn in one title, ie "am i fat or skinny, should i bulk or cut"
    return sub_ids

if __name__ == "__main__":
    main()