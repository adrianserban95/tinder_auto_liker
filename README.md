# Tinder Auto Liker

This is a simple Tinder auto liker bot, please follow the steps below in order to use it:
1. Download [ChromeDriver](https://chromedriver.chromium.org/) and place it in the same folder as *tinder.py*
2. Edit *line 7* and replace */UPDATE_THIS/* with the path to the ChromeDriver
3. Open *tinder.py* from terminal
4. Accept cookies, log-in, allow the browser to track your location
5. Open the terminal again, press "*y*" and *Enter*

## How does it work?
The bot will automatically perform the next actions for 100 profiles:
1. Open the profile
2. Wait 2 seconds
3. Check next photo (repeat this proccess 0 to 4 times)
4. Wait 2 seconds for every photo seen
5. Swipe right
6. Wait 1 second