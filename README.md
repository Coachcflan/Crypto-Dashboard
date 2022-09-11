# Crypto-Dashboard
Cryptocurrency Dashboard created with python and bokeh.The dashboard 
allows for an individual to input a coin ID ,coin sector, and daterange.
which will result in information and statistics on the given coin.

## Technologies
* Python 3.8
* pandas 1.0.5
* pycoingecko 2.2
* bokeh 2.1.1
* gensim 3.8.3

# Features
The information generated for on the dashboard includes:
* Coin price chart 
* Bitcoin and Ethereum daily return rolling correlation 
* Price and daily return summary statistics datatable 
* daily returns histogram
* Coin Sector performance scatter plot
  * Average daily return
  * Daily return standard deviation
* Coin description semantic similarity query.



## Launch 
##### This is how you run the dashboard with current market history dataset.
##### Read Auto-updating section to make it a daily auto-updating dashboard. 
* pip install all libraries (assuming python and pandas are already installed)
~~~~
$ pip install pycoingecko
$ pip install bokeh
$ pip install gensim
~~~~
#### If not in proper directory do this to launch project do this:
1.) change to proper directory
~~~~
$ cd Dashboard_folder
~~~~
2.) Launch Dashboard
~~~~
$ bokeh serve --show crypto_dash.ipynb
~~~~
#### If already in proper directory just launch the dashboard:
~~~~
$ bokeh serve --show crypto_dash.ipynb
~~~~
## Auto-updating
* To make it an auto-updating dashboard we must update the market dataset every day.
* To do this create a cron job
### Setting up the cron job
Step one - Edit mode:
~~~~
$ crontab -e
~~~~
Step two - when in edit mode press i on keyboard.
Step three - set up the job with time and paths:
~~~~
5 0 * * * /opt/anaconda3/bin/python3 /(path to update_csv.py file)
~~~~
* The first path is to where python three is located on your local machine.
* This updates your market dataset every day at 12:05am (5 0 * * *).
* To customize your own time checkout [crontab guru](https://crontab.guru/#*).


