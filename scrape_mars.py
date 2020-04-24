# Import Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import pandas as pd

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()

    # Initial url to visit
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    # Fetch the first headline and paragraph visible below it
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    list_item = soup.select_one('ul.item_list li.slide')
    news_title = list_item.find('div', class_='content_title')
    teaser = list_item.find('div', class_='article_teaser_body')

    # Featured Images
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    # Initial URL
    browser.visit(image_url)

    # Clicking "Full Image" button
    footer = browser.find_by_tag('footer')
    within_footer = footer.find_by_tag('a').click()

    # Clicking "more info" button
    more_info = browser.find_by_id('fancybox-lock')
    a_tag = more_info.find_by_tag('a[class="button"]').click()

    # Save the featured image url
    featured_jpg_img = browser.url

    ##### TWITTER PORTION


    # Mars Facts
    mfacts_url = 'https://space-facts.com/mars/'

    # Using Pandas, read in the html to a table
    mars_tables = pd.read_html(mfacts_url)
    mars_tables

    # Transform table into dataframe
    mfacts_df = mars_tables[0]
    mfacts_df.columns = ['description', 'value']
    mfacts_df

    # Mars Hemispheres

    # Hemisphere One
    h_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(h_url)
    # Caputring the titles (one)
    head = browser.find_by_tag('div[class="collapsible results"]')
    div = browser.find_by_tag('div[class="item"]')[0]
    title_1 = div.find_by_tag('h3')
    # Clicking to the images (one)
    head = browser.find_by_tag('div[class="collapsible results"]')
    div = browser.find_by_tag('div[class="description"]')[0]
    image = div.find_by_tag('a').click()
    # Capturing full size image
    head = browser.find_by_tag('div[class="widget block bar"]')
    ul = browser.find_by_tag('ul')
    li = ul.find_by_tag('li')[0]
    image1 = li.find_by_tag('a').click()
    image1_url = browser.url

    # Hemisphere Two
    h_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(h_url)
    # Capturing the titles (two)
    head = browser.find_by_tag('div[class="collapsible results"]')
    div = browser.find_by_tag('div[class="item"]')[1]
    title_2 = div.find_by_tag('h3')
    # Clicking to the images (two)
    head = browser.find_by_tag('div[class="collapsible results"]')
    div = browser.find_by_tag('div[class="description"]')[1]
    image = div.find_by_tag('a').click()
    # Capturing full size image
    head = browser.find_by_tag('div[class="widget block bar"]')
    ul = browser.find_by_tag('ul')
    li = ul.find_by_tag('li')[0]
    image2 = li.find_by_tag('a').click()
    image2_url = browser.url

    # Hemisphere Three
    h_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(h_url)
    # Capturing the titles (three)
    head = browser.find_by_tag('div[class="collapsible results"]')
    div = browser.find_by_tag('div[class="item"]')[2]
    title_3 = div.find_by_tag('h3')
    # Clicking to the images (three)
    head = browser.find_by_tag('div[class="collapsible results"]')
    div = browser.find_by_tag('div[class="description"]')[2]
    image = div.find_by_tag('a').click()
    # Capturing full size image
    head = browser.find_by_tag('div[class="widget block bar"]')
    ul = browser.find_by_tag('ul')
    li = ul.find_by_tag('li')[0]
    image3 = li.find_by_tag('a').click()
    image3_url = browser.url

    # Hemisphere Four
    h_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(h_url)
    # Capturing the titles (4)
    head = browser.find_by_tag('div[class="collapsible results"]')
    div = browser.find_by_tag('div[class="item"]')[3]
    title_4 = div.find_by_tag('h3')
    # Clicking to the images (four)
    head = browser.find_by_tag('div[class="collapsible results"]')
    div = browser.find_by_tag('div[class="description"]')[3]
    image = div.find_by_tag('a').click()
    # Capturing full size image
    head = browser.find_by_tag('div[class="widget block bar"]')
    ul = browser.find_by_tag('ul')
    li = ul.find_by_tag('li')[0]
    image4 = li.find_by_tag('a').click()
    image4_url = browser.url

    # All hemisphere data dictionary
    hemis_dict = [
    {"title": {title_1}, "img_url": {image1_url}},
    {"title": {title_2}, "img_url": {image2_url}},
    {"title": {title_3}, "img_url": {image3_url}},
    {"title": {title_4}, "img_url": {image4_url}}
]

    browser.quit()

    return mars_data