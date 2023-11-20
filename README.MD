<<<<<<< HEAD
# Project Overview:
# I intend to answer the following questions (more to come probably, but this is what I want to find so far):
# What are the most common numbers drawn in the Powerball?
# What are the least common numbers drawn in the Powerball?
# What are the most common number combinations drawn in the Powerball?
# What are the least common number combinations drawn in the Powerball?
# What is the average jackpot size for the Powerball?
# What is the largest jackpot won in the Powerball?
# What is the smallest jackpot won in the Powerball?
# How often is the Powerball jackpot won?
# How often do players win the Powerball jackpot by playing a specific number combination?
# What is the average amount of money spent on Powerball tickets by a single player?
# What is the total amount of money spent on Powerball tickets each year?
# What is the economic impact of the Powerball lottery?
# What are the social and economic factors that influence people to play the Powerball lottery?
# Winners by State?
# Taking Cash option vs Annulity option?

# 
To accomplish this I will be taking a number of different data sources, as of now I have 2 CSV’s with a combined total of 12 years of lottery winning numbers.  By using Pandas(dataframes and filtering), Matplotlib(visuals), and maybe Numpy for array’s and if there are any advanced calculations (not sure there will be but I’ll try to work it in to show understanding of the package).  Using these I should be able to answer 1 - 7.  For 8, I built a web scraper to extract specific winning dates with BeautifulSoup and Request packages.  For 9, I will need to find a data source for picked numbers vs random numbers, then do the same kind of analysis as the previous questions.  For 10, same thing.  I am not sure if there is going to be any substantial data on #10, if I had to guess, maybe there will be an article I can reference, in which case I will be building two different web scrapers with BeautifulSoup anyway, so that will just be a 3rd.  11 - 13 will still need some reliable data sources before I can really find out what I need to do to extract that data.  Hopefully for some of these I will be building API’s to read them in for analysis.  I plan on (not sure exactly where but I’ll wrangle in it) building a database and working some of the parts through SQL in some yet undetermined SQL program.

# Technical Insight:
I will code most of this in the Pycharm Community Center Edition, Jupyter Notebook and some kind of SQL program.  I plan to use Pandas, Matplotlib, Numpy, BeautifulSoup, Requests and building API’s to read, analyze, visualize, scrape, and calculate my data.  I’ll probably also use beautify in BeautifulSoup to help with visualizations.  I plan to use Pandas as really the workhorse of my analysis just because of its functionality does most of the things I want to accomplish.  Matplotlib for visualizations.  Numpy for arrays and advanced calculations (and honestly for the learning, I’m sure I’ll use it at some point).  BeautifulSoup for its webscraper functionality in tandem with Requests to read in URLs to beautifulSoup.  I plan to build API’s to help with either the Web Scraping or to read in certain types of data.  (Do using API calls and Pagination count as using API’s?  OR do I need to actually build one to do something) As of now, I don’t fully understand any of these I would say, but making them function will be a fantastic series of lessons that will allow me to practice.  I also want to try to learn both Tableau and PowerBI to make dashboards to demonstrate a understanding of how to use these

# Visual Aides:  
I’ll find many different ways to visually express my findings in a comprehensive way.   I will probably use wireframes (Powerpoint, etc) as a presentation tool, more than likely in the introductions to help people understand my questions and how I intend to accomplish them.  This is where the dashboards from Tableau and PowerBI would come into play.

# Solicit Mentor Feedback:  
I will check in with my mentors on the regular to help with any blocks I have, any guidance in the right direction if I bite off more than I could chew, resources for learning all the things I still need to learn to do what needs doing.  Most importantly, checking in periodically to make sure I am hitting above and beyond all my requirements.

# Project Plan Format:  
I am aesthetically disabled.  I have no idea what looks good, but I will probably just look at different projects and whatever is in trend in big marketplaces and just utilize and adapt those fonts and displays.

# Process Steps:
Scrape Data website, write to CSV
Data dis Jupyter Notebook MPL
Clean Data, remove crap.  Add extra column for day of the week (datetime, format specification)
With clean data - Create script that creates database in SQL, insert row for each CSV file
Script that works against data in DB for analysis
Tableau or Matplotlib


# TABLEAU LINKS!!!!!:
# 2015 - Present Jackpot Amount Won by State  -  https://public.tableau.com/views/2015-PresentJackpotAmountWonbyState/Dashboard1?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link
# Powerball Winners by State  -  https://public.tableau.com/views/PowerballWinnersbyState/Sheet1?:language=en-US&:display_count=n&:origin=viz_share_link
=======
# Project Overview:
# I intend to answer the following questions (more to come probably, but this is what I want to find so far):
# What are the most common numbers drawn in the Powerball?
# What are the least common numbers drawn in the Powerball?
# What are the most common number combinations drawn in the Powerball?
# What are the least common number combinations drawn in the Powerball?
# What is the average jackpot size for the Powerball?
# What is the largest jackpot won in the Powerball?
# What is the smallest jackpot won in the Powerball?
# How often is the Powerball jackpot won?
# How often do players win the Powerball jackpot by playing a specific number combination?
# What is the average amount of money spent on Powerball tickets by a single player?
# What is the total amount of money spent on Powerball tickets each year?
# What is the economic impact of the Powerball lottery?
# What are the social and economic factors that influence people to play the Powerball lottery?
# Winners by State?
# Taking Cash option vs Annulity option?

# 
To accomplish this I will be taking a number of different data sources, as of now I have 2 CSV’s with a combined total of 12 years of lottery winning numbers.  By using Pandas(dataframes and filtering), Matplotlib(visuals), and maybe Numpy for array’s and if there are any advanced calculations (not sure there will be but I’ll try to work it in to show understanding of the package).  Using these I should be able to answer 1 - 7.  For 8, I built a web scraper to extract specific winning dates with BeautifulSoup and Request packages.  For 9, I will need to find a data source for picked numbers vs random numbers, then do the same kind of analysis as the previous questions.  For 10, same thing.  I am not sure if there is going to be any substantial data on #10, if I had to guess, maybe there will be an article I can reference, in which case I will be building two different web scrapers with BeautifulSoup anyway, so that will just be a 3rd.  11 - 13 will still need some reliable data sources before I can really find out what I need to do to extract that data.  Hopefully for some of these I will be building API’s to read them in for analysis.  I plan on (not sure exactly where but I’ll wrangle in it) building a database and working some of the parts through SQL in some yet undetermined SQL program.

# Technical Insight:
I will code most of this in the Pycharm Community Center Edition, Jupyter Notebook and some kind of SQL program.  I plan to use Pandas, Matplotlib, Numpy, BeautifulSoup, Requests and building API’s to read, analyze, visualize, scrape, and calculate my data.  I’ll probably also use beautify in BeautifulSoup to help with visualizations.  I plan to use Pandas as really the workhorse of my analysis just because of its functionality does most of the things I want to accomplish.  Matplotlib for visualizations.  Numpy for arrays and advanced calculations (and honestly for the learning, I’m sure I’ll use it at some point).  BeautifulSoup for its webscraper functionality in tandem with Requests to read in URLs to beautifulSoup.  I plan to build API’s to help with either the Web Scraping or to read in certain types of data.  (Do using API calls and Pagination count as using API’s?  OR do I need to actually build one to do something) As of now, I don’t fully understand any of these I would say, but making them function will be a fantastic series of lessons that will allow me to practice.  I also want to try to learn both Tableau and PowerBI to make dashboards to demonstrate a understanding of how to use these

# Visual Aides:  
I’ll find many different ways to visually express my findings in a comprehensive way.   I will probably use wireframes (Powerpoint, etc) as a presentation tool, more than likely in the introductions to help people understand my questions and how I intend to accomplish them.  This is where the dashboards from Tableau and PowerBI would come into play.

# Solicit Mentor Feedback:  
I will check in with my mentors on the regular to help with any blocks I have, any guidance in the right direction if I bite off more than I could chew, resources for learning all the things I still need to learn to do what needs doing.  Most importantly, checking in periodically to make sure I am hitting above and beyond all my requirements.

# Project Plan Format:  
I am aesthetically disabled.  I have no idea what looks good, but I will probably just look at different projects and whatever is in trend in big marketplaces and just utilize and adapt those fonts and displays.

# Process Steps:
Scrape Data website, write to CSV
Data dis Jupyter Notebook MPL
Clean Data, remove crap.  Add extra column for day of the week (datetime, format specification)
With clean data - Create script that creates database in SQL, insert row for each CSV file
Script that works against data in DB for analysis
Tableau or Matplotlib


# TABLEAU LINKS!!!!!:
# 2015 - Present Jackpot Amount Won by State  -  https://public.tableau.com/views/2015-PresentJackpotAmountWonbyState/Dashboard1?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link
# Powerball Winners by State  -  https://public.tableau.com/views/PowerballWinnersbyState/Sheet1?:language=en-US&:display_count=n&:origin=viz_share_link
>>>>>>> 2b512835f280dcbecb1c1a7dc31d9531d45013f2
# State Powerball Winners Bar  -  https://public.tableau.com/views/StatePBWinners/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link