from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path':ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit visitcostarica.herokuapp.com

    browser.visit(url)

    time.sleep(5)

    # Scrape page into Soup
    html = browser.html
    time.sleep(5)
    soup = bs(html, 'html.parser')

    # Get the title
    first_title = soup.find_all("div", class_= "content_title")[1].text.strip(

    # Get the descrip
    mars_text = soup.find("div", class_= "article_teaser_body").text

    #MARS IMAGES
    featured_image_url= "https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA18284_ip.jpg"

    #MARS FACTS
    url_marsfacts = 'https://space-facts.com/mars/'

    tables = pd.read_html(url_marsfacts)
    tab1=tables[0]
    table=tab1.rename(columns={0: "Description", 1:"Mars"})
    table.to_html("table.html")

    #Mars Hemisphere images
    hemi_url= "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    
    browser.visit(hemi_url)

    time.sleep(5)
    html_hemi = browser.html
    time.sleep(5)
    soup_hemi = bs(html_hemi, 'html.parser')

    hemi_titles = soup_hemi.find_all('div', class_="item")

    # A blank list to hold the titles
    titles_list = []
    # Loop over td elements
        for title in hemi_titles:
            # If td element has an header3...
            if (title.h3):
                # And the header has text...
                if (title.h3.text):
                    # Append that text to the list
                titles_list.append(title.h3.text)

    hemi_img_list = []

    for title in titles_list:
        # go to Website
        hemi_img_url= "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(hemi_img_url)
    
        #give it time
        time.sleep(5)
    
        # Click each image URL
        browser.click_link_by_partial_text(title)

        # Scrape each page into Soup
        html = browser.html
        hemi_img_soup = bs(html, "html.parser")
        image_url = hemi_img_soup.find_all("li")[0].a["href"]


        # Create a dictionary of title and url
        hemi_img_dict = {"title":title, "image_url":image_url}
        # add this dictionary to the list
        hemi_img_list.append(hemi_img_dict)



    # Close the browser after scraping
    browser.quit()


