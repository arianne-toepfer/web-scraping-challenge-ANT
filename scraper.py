# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# #Worked collaborately with Bitty Fennie on this homework

# %%
from bs4 import BeautifulSoup
import requests
import os
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser
import pandas as pd

# %% [markdown]
# #NASA Mars News Scraping

def scrape():
# URL of page to be scraped
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    # Retrieve page with the requests module
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')


    # %%
    soup


    # %%
    print(soup.prettify())


    # %%
    # Examine the html and look for the section that identifies the News titles
    news_results = soup.find_all('div', class_='features')
    news_results


    # %%
    # Loop through returned results
    for result in news_results:
        
        #Retrieve the News title and paragraph
        news_title = result.find('div', class_='content_title').text 
        news_p = result.find('div', class_='rollover_description_inner').text  
        #Print the first title and paragraph
        print(news_title)
        print(news_p) 

    # %% [markdown]
    # #JPL Mars Space Images-Featured Image Scraping

    # %%
    # URL of page to be scraped
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'

    # Retrieve page with the requests module
    response = requests.get(url)

    soup2 = BeautifulSoup(response.text, 'html.parser')


    # %%
    print(soup2.prettify())


    # %%
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # %%
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)


    # %%

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    image_header = soup.find_all('div', class_='header')

    for image in image_header:
        picture = image.find('a', class_='showimg fancybox-thumbs')
        link = picture['href']

        print(link)

    # %% [markdown]
    # #Mars Facts Scraping

    # %%
    url = "https://space-facts.com/mars/"


    # %%
    tables = pd.read_html(url)
    tables


    # %%
    #Add header and clean up dataframe
    facts_df = tables[0]
    facts_df = facts_df.rename(columns={0: 'Description'})
    facts_df = facts_df.rename(columns={1: "Mars Fact"})
    facts_df.head()


    # %%
    #Convert Dataframe to html
    html_table =facts_df.to_html()
    html_table


    # %%
    #Make it pretty
    html_table.replace('\n', '')

    # %% [markdown]
    # #Hemisphere images to HTML

    # %%
    hemisphere_image_urls = [
        {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
        {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"}]
    hemisphere_image_urls

    # %%
    scraped_data = {"News Title":news_title, "News Descriptor": news_p, "Featured Image": link, "Mars Fact Table": html_table, "Hemisphere Images": hemisphere_image_urls} 

    # %%
    return scraped_data



