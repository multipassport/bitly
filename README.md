# Bitly url shorterer

That is a script which either converts URL to bit.ly shortlink or returns the number of bit.ly shortlink clicks.

### How to install

Before running the script you should get bit.ly [Generic Access Token](https://bitly.com/a/oauth_apps)
It should look like this: `abcd0c405a474414c97cb65e7b8efghj`

Then create an .env file within script directory and paste Token after equal sign(no spaces allowed):
```
BITLY_TOKEN=YourToken
```

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
Finally run following code with your URLs instead of examples:
```
python main.py https://www.google.com/
```
or
```
python main.py https://bit.ly/3e5DVgK
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
