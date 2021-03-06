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

From the <b>/home/pi/</b> directory, git the code from https://github.com/mvartani76/RPi-TwitterBot-Tutorial-Python.

<pre class="code-text-only" style="display: none;">
<code>sudo git clone https://github.com/mvartani76/RPi-TwitterBot-Tutorial-Python</code>
</pre>

This will create the directory <b>RPi-TwitterBot-Tutorial-Python</b>.<br>

There are four python source files in this directory that utilize the twython python library.
<ol>
<li><b>SillyCamPicTweeter.py</b>	- This code tweets a picture from a USB webcam </li>
<li><b>SillyGPIOTweeter.py</b>	- This code tweets the status changes of GPIO pins 7,9,11,13, and 15 only when they change as twitter forbids duplicate tweets</li>
<li><b>SillyTempTweeter.py</b>	- This code tweets the Raspberry Pi CPU temperature one time</li>
<li><b>SillyTweeter.py</b> - This code allows the user to tweet random text from the command line</li>
</ol>

Each of the files will have the following lines of code but you will need to replace the relevant keys with your information that you received from Twitter when registering your app.
<pre class="code-text-only" style="display: none;">
<code>#!/usr/bin/env python
import sys
from twython import Twython
CONSUMER_KEY = <b>'***************YOUR DATA*****************'</b>
CONSUMER_SECRET = <b>'***************YOUR DATA*****************'</b>
ACCESS_KEY = <b>'***************YOUR DATA*****************'</b>
ACCESS_SECRET = <b>'***************YOUR DATA*****************'</b>

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

api.update_status(status=sys.argv[1])
</code></pre>
If you want, you can ake it executable with the following command (replacing your Python file name for the relevant file)

<pre class="code-text-only" style="display: none;">
<code>sudo chmod +x SillyTweeter.py</code>
</pre>
You should now be able to test your ability to post tweets like so:

<pre class="code-text-only" style="display: none;">
<code>python SillyTweeter.py 'Hello Everyone, this is my Raspberry Pi tweetin'
python SillyGPIOTweeter.py
python Silly TempTweeter.py
python SillyCamPicTweeter.py</code>
</pre>
