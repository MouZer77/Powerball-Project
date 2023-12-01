{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ea28d62e",
   "metadata": {},
   "source": [
    "### Project Overview:"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "538cb383",
   "metadata": {},
   "source": [
    "This project aimed to answer a simple question: What's the best way to Win the Powerball?  Simple!  In it, I explore various approaches to try to game the system by analyzing statistical occurrences from the numbers themselves, as well as a little more abstract potential 'Luck' from data of winners.  After all, we are trying to win; why not try everything that COULD improve our odds, even things that aren't the statistics of the numbers themselves.  I explore the best numbers to play, best State to play in, best Jackpot to go for, best month to play, even the best draw date!  \n",
    "\n",
    "As I explored the data and started to see the story, the data painted a different picture: Maybe the Powerball is being played more and more out of desperation?  I briefly touch on what the data COULD potentially be telling us about why more people are playing than ever before; but that's not this project's main purpose.  The main purpose is to WIN!\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b1adbb76",
   "metadata": {},
   "source": [
    "### Technicals:"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "169d1f8d",
   "metadata": {},
   "source": [
    "In this project I demonstrate my ability to go through the Data Analysis process of Discovery, Cleaning, Analysis and Visualization of Data.  I accomplish this by utilizing many Python Libraries such as:\n",
    "\n",
    "Pandas (DataFrames, Everything)\n",
    "\n",
    "MatplotLib(Visualizations)\n",
    "\n",
    "Seaborn(Visualizations)\n",
    "\n",
    "Numpy(Arrays)\n",
    "\n",
    "Re(Analysis and Cleaning)\n",
    "\n",
    "Requests(Web Scrapers)\n",
    "\n",
    "BeautifulSoup4 (Web Scrapers)\n",
    "\n",
    "Datetime (Analysis and Cleaning)\n",
    "\n",
    "SQLite3 (Analysis and Cleaning)\n",
    "\n",
    "As well as the SQL IDE DB Browser and Tableau Public for visualizations.\n",
    "\n",
    "I used the Python IDE’s Jupyter Notebook (Through the Anaconda Suite) and PyCharm Community Edition."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4e048451",
   "metadata": {},
   "source": [
    "### How to Set Up: "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1887764d",
   "metadata": {},
   "source": [
    "1.) Fork the repo and clone the forked repo to your computer\n",
    "\n",
    "2.) Open GitBash (Download if you don't have) in Windows or Terminal in Mac\n",
    "\n",
    "3.) Go to the Powerball Project folder on your computer\n",
    "\n",
    "4.) If you would like to use a Virtual Environment: directions for how to do that here:\n",
    "https://docs.python.org/3/library/venv.html \n",
    "I used the Anaconda suite for my project.  If you would like to as well, beware it is large!  But that can be located here:\n",
    "https://www.anaconda.com/download\n",
    "\n",
    "5.) Once the virtual environment of choice is activated, run pip install -r requirements.txt\n",
    "\n",
    "(For Jupyter Notebook Anaconda Users, just navigate to the project folder and open the notebook \"Final Notebook.ipynb\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a795a8e5",
   "metadata": {},
   "source": [
    "#### In case there is any sort of issue, here are the libraries to be installed:"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f487802d",
   "metadata": {},
   "source": [
    "import pandas as pd\n",
    "\n",
    "import matplotlib.pylab as plt\n",
    "\n",
    "import seaborn as sns\n",
    "\n",
    "import numpy as np\n",
    "\n",
    "plt.style.use('ggplot')\n",
    "\n",
    "import re\n",
    "\n",
    "import requests\n",
    "\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "import datetime as dt\n",
    "\n",
    "import sqlite3 (Only for Work Notebook)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
