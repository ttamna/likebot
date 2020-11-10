# -*- coding: utf-8 -*-

import instapy
from instapy.util import smart_run

import secret


session = instapy.InstaPy(username=secret.user, password=secret.passwd, headless_browser=True)

# let's go! :>
with smart_run(session):
    # settings
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=6000,
                                    max_following=3000,
                                    min_followers=50,
                                    min_following=50)

    session.set_quota_supervisor(enabled=True,
                                 sleep_after=["likes", "comments", "follows",
                                              "unfollows", "server_calls"],
                                 sleepyhead=True, stochastic_flow=True,
                                 notify_me=False,
                                 peak_likes=(56, 999),
                                 peak_comments=(25, 120),
                                 peak_follows=(48, 125),
                                 peak_unfollows=(35, 400),
                                 peak_server_calls=(500, 4500))

    session.set_simulation(enabled=False)

    # filter
    session.set_ignore_users([])
    session.set_ignore_if_contains([])
    session.set_dont_like(
        ['dick', 'squirt', 'gay', 'homo', '#fit', '#fitfam', '#fittips',
         '#abs', '#kids', '#children', '#child',
         '[nazi',
         'jew', 'judaism', '[muslim', '[islam', 'bangladesh', '[hijab',
         '[niqab', '[farright', '[rightwing',
         '#conservative', 'death', 'racist'])

    session.set_action_delays(enabled=True, like=5, comment=5, follow=5, unfollow=30,
                              randomize=True, random_range=(70, 140))

    # like by tag
    TAG_BASE = ['cat', 'dog', 'nature']
    HASH_COUNT = 3
    INTERACTS = 3
    session.set_user_interact(amount=INTERACTS, randomize=True, percentage=50,
                              media='Photo')

    LIKES = int(600/(len(TAG_BASE)*HASH_COUNT)/3)

    session.set_smart_hashtags(TAG_BASE, limit=HASH_COUNT, sort='random', log_tags=True)
    session.set_delimit_liking(enabled=True, max=500, min=4)

    session.set_do_comment(enabled=True, percentage=40)            # comment
    session.set_comments(['😍'])

    session.like_by_tags(use_smart_hashtags=True, amount=LIKES, media='Photo', interact=True)

    # interact with my followers
    MY_FOLLOWERS = session.grab_followers(
        username=secret.user, amount="full", live_match=True, store_locally=True)

    session.set_do_follow(enabled=True, percentage=10, times=1)   # Follow my follower?
    session.set_do_like(enabled=True, percentage=80)               # like my follower's?
    session.set_do_comment(enabled=True, percentage=40)            # comment my follower's?
    session.set_comments(['👏 ', '👍'])

    session.interact_by_users(MY_FOLLOWERS, amount=100, randomize=True, media="Photo")

    # interact with star's followers
    session.set_do_follow(enabled=False, percentage=25, times=1)  # follow star's follower?
    session.set_do_like(enabled=True, percentage=80)              # like star's follower?
    session.set_do_comment(enabled=False, percentage=80)          # comment star's follower?
    session.set_comments(['👏 ', '👍'])

    session.interact_user_followers(
        ['natgeo', 'catsofweek', 'catsofweek'], amount=50, randomize=True)

    # unfollow
    session.set_dont_unfollow_active_users(enabled=True, posts=3)
    session.unfollow_users(amount=25, InstapyFollowed=(True, "nonfollowers"),
                           style="RANDOM",
                           unfollow_after=168 * 60 * 60,
                           sleep_delay=600)
