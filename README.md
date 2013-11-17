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
