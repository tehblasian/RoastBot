# A Simple RoastBot
## A simple bot that insults you via SMS! Written in Python 2.7

The bot will either select an insult from a user-created list, or fetch a random one from http://www.randominsults.net

The insult is then sent to the user via SMS using the Twilio API*

*Because the bot is running on the trial version of the Twilio API, only the holder of the Twilio account can receive the insults.

If you want to run this for yourself, first create a Twilio account. Then, deploy the Python script to a server and set the inbound request URL to the URL of your server.

Enjoy!



