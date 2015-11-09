<h1>flybot</h1>
<h2>a terminal lookup tool for airports</h2>
Ever find yourself on the way to the airport with no idea what terminal you're flying out of? 
This happens to me all the time, so I made a terminal lookup tool. You plug in the airport and 
your airline, and it tells you your departure terminal.

Most of the work involved scraping the terminal info from various sites with Python using Selenium Webdriver 
and populating a monster Postgres database. The site itself was built in Django. Still squashing bugs, but it works.
