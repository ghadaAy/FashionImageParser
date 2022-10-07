# FashionImageParser
Welcome!
This project is purely for learning purposes.

## Goal:
Scrape bershka's images using Scrapy: https://www.bershka.com/es/en/h-woman.html

## Steps:
1. Create a script that tests proxies and gives us a list of working proxies to use in our scraping.
2. Create our Spider and pipeline to scrape the pages.

## I- Proxy List

We have a list of proxies that we downloaded freely. 
The issue is that these proxies don't work all the time and might change alot.
1. We created a script workingProxies.py that tests proxies from proxies.txt and adds the working ones to working_proxy.txt
#### For windows
2. Create a bat file proxySearch.bat to run our script needs to run workingProxies regularly in the background.

## II- Scraping
1. To make sure that the scraper will work, change the USER_AGENT using this method: 
![Untitled-2022-10-07-1355](https://user-images.githubusercontent.com/41645667/194582581-91e476ed-54e9-4955-b908-a4abccf67a03.png)

2. To run the spider you just have to install requirements.txt inside a new conda environment preferably and then cd into fashion/fashion to finally run this command:
scrapy crawl fashion_spidy
