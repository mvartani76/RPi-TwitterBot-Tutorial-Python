RPi-TwitterBot-Tutorial-Python
==============================

TwitterBot Python Tutorial taken from http://www.makeuseof.com/tag/how-to-build-a-raspberry-pi-twitter-bot/

Install Twython
===============
<pre class="code-text-only" style="display: none;">
<code>sudo apt-get update</code>
<code>sudo apt-get upgrade</code>
<code>sudo apt-get install python-setuptools</code>
<code>sudo easy_install pip</code>
<code>sudo pip install twython</code>
</pre>

Registering a Twitter app
=========================
In order to use the Twitter API – that is, the REST interface that we’ll use to post new Tweets and generally
interact with Twitter outisde of the twitter website – we’ll need to register a new app. We register a new app 
from https://dev.twitter.com/apps/new – you do not need to specify a callback URL, and just make up a website if you want.
 
 
<img src="http://main.makeuseoflimited.netdna-cdn.com/wp-content/uploads/2013/08/new-twitter-app.jpg">
 
 You’ll see something resembling this once you’re done – these keys are unique to you.

<img src="http://main.makeuseoflimited.netdna-cdn.com/wp-content/uploads/2013/08/twitter-app.jpg">

By default, the app is set to read-only, so we won’t be able to publish tweets without changing that to Read and Write. Go to the Settings tab and change the Application type.

<img src="http://main.makeuseoflimited.netdna-cdn.com/wp-content/uploads/2013/08/readwrite-access.jpg">

Once saved, head back to the Details tab and click the button at the bottom to create an OAuth access token – this gives your application access to your own Twitter account. Refresh, and leave the page open for later – we’ll need to copy paste some of those keys in a minute.

<img src="http://main.makeuseoflimited.netdna-cdn.com/wp-content/uploads/2013/08/access-token.jpg">

Create Your Python Project(s)
=============================

Begin by making a new directory to house your Tweet project, then create a new file.
mkdir SillyTweeter
cd SillyTweeter
sudo nano SillyTweeter.py
You can call it whatever you like, obviously.
In the text editor that appears, copy and paste the following, replacing the consumer key with the relevant key from the Twitter application page we left open earlier. Each key is surrounded by single quotes, so be sure not to miss those. Note that ACCESS_KEY is referred to as Access token on the Twitter app page.
<pre class="code-text-only" style="display: none;">
<code>#!/usr/bin/env python
import sys
from twython import Twython
CONSUMER_KEY = '***************YOUR DATA*****************'
CONSUMER_SECRET = '***************YOUR DATA*****************'
ACCESS_KEY = '***************YOUR DATA*****************'
ACCESS_SECRET = '***************YOUR DATA*****************'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

api.update_status(status=sys.argv[1])
</code></pre>
Hit Ctrl-X, and press Y to exit and save the file. Make it executable with the following command (replacing your Python file name if you chose something else)
sudo chmod +x SillyTweeter.py
You should now be able to test your ability to post tweets like so:
python SillyTweeter.py 'Hello Everyone, this is my Raspberry Pi tweetin
