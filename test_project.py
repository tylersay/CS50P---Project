from project import check_posts_replied, bot_search_and_reply
import praw


def test_check_posts_replied():
    assert check_posts_replied() == ['test_asdf', 'test_qwer', 'test_zxcv']


def test_check_posts_replied_after_running_once():
    assert check_posts_replied() == ['test_asdf', 'test_qwer', 'test_zxcv', 'wtihjn', 'wsqlk5', 'wqtuo1']


def test_bot_search_and_reply():
    reddit = praw.Reddit("bot1")
    subreddit = reddit.subreddit("pythonforengineers")
    post_replied = ['test_asdf', 'test_qwer', 'test_zxcv']
    assert bot_search_and_reply(subreddit, post_replied) == ['wtihjn', 'wsqlk5', 'wqtuo1']


