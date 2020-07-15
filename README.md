# IG-Analytics-API
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
## Start Server
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python main.py
```

## Profile
##
    GET:    /insta/<username>
    DESC:   gets account fullname, bio, profile pic, followers, following, total no of posts
##

## Comments
##
    GET:    /insta/<username>/coms
    DESC:   gets all comments
##

## Likes and Comments
##
    GET:    /insta/<username>/likesncoms
    DESC:   gets no of likes and comments with timeline of day (hours)
##

## Latest Post
##
    GET:    /insta/<username>/latest
    DESC:   gets latest post of the user
##

## Followers timeline
##
    GET:    /insta/<username>/followtimeline
    DESC:   maintains followers timeline(need to open app daily)
##

## Trending Hashtags
##
    GET:    /trending/<key>
    DESC:   gets top 10 trending hashtags on instagram by keyword
##


`NOTE: Don't resquest too frequently, it might break the api`