import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from splinter import Browser
import flask


def scrape():
    scrape_dict = {}

    # Open Browser
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser(
        'chrome', **executable_path, headless=False)

    # NASA Mars News
    nasa_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(nasa_url)
    soup_nasa = bs(browser.html)
    articles_dict = {"Title": [], "Paragraph": []}
    articles = soup_nasa.find_all("li", class_="slide")
    for article in articles:
        articles_dict["Title"].append(
            article.find('div', class_="content_title").text)
        articles_dict["Paragraph"].append(article.find(
            'div', class_="article_teaser_body").text)
    scrape_dict["Mars_News"] = articles_dict

    # JPL Mars Space Images - Featured Image
    jpl_img_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_img_url)
    soup_jpl = bs(browser.html)
    start_url = 'https://www.jpl.nasa.gov'
    featured_image_url = start_url + \
        soup_jpl.find("a", class_="button")["data-fancybox-href"]
    scrape_dict["Featured_Image"] = featured_image_url

    # Mars Weather
    weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(weather_url)
    soup_weather = bs(browser.html)
    tweet = soup_weather.find('div', class_='content').find('p')
    unwanted = tweet.find('a')
    unwanted.extract()
    scrape_dict["Weather"] = tweet.text

    # Mars Facts
    facts_url = "https://space-facts.com/mars/"
    facts_df = pd.read_html(facts_url)[0]
    facts_df = facts_df.rename(columns={0: "description", 1: "value"})
    facts_df = facts_df.set_index("description")
    scrape_dict["Mars_Facts"] = facts_df.to_html()

    # Mars Hemispheres
    astrogeology_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(astrogeology_url)
    soup_astro = bs(browser.html)
    imgs = soup_astro.find_all("div", class_="item")
    hemisphere_hrefs = []
    for div in imgs:
        hemisphere_hrefs.append(div.find('a')['href'])
    hemisphere_image_urls = []
    start_url = "https://astrogeology.usgs.gov"
    for href in hemisphere_hrefs:
        url = start_url + href
        browser.visit(url)
        soup_hemisphere = bs(browser.html)
        hemisphere = {"title": soup_hemisphere.find('h2').text.strip(" Enhanced"),
                      "img_url": soup_hemisphere.find('div', class_="downloads").find("a")["href"]}
        hemisphere_image_urls.append(hemisphere)
    scrape_dict["Hemisphere"] = hemisphere_image_urls

    browser.quit()

    return scrape_dict
