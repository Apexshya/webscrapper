# Web Scraper

## Project Detail
This is a web scraping project developed using Python and Scrapy framework. The purpose of this project is to extract job details from a multi-page website listing data analyst job postings.

## Setting up the project

- **Clone the repository**
  ```bash
  git clone https://github.com/Apexshya/webscrapper

- **Install Dependencies**
  - Install Python
  - Create a Virtual Environment with pipenv
    ```bash
    pip install pipenv
    pipenv shell
    ```
  - Or Create a Virtual Environment with virtualenv
    ```bash
    virtualenv .

    # Activate Virtual Environment:
    # - Windows:
    .\Scripts\activate
    # - Linux and Mac:
    source ./bin/activate
    ```

  - Install Scrapy
    ```bash
    pip install scrapy
    ```




  - Install Project Requirements
    ```bash
    pip install -r requirements.txt
    ```

- **Set up Scrapy project**
  ```bash
  cd webscrapper
  cd task  # Navigate to the project directory


- **Run the Spider**
  ```bash
  scrapy crawl job_spider

  
 - **View the data**
  ```bash
  scrapy crawl job_spider -o items.csv #scrape data from the website, and save the scraped data to a CSV file named "items.csv" in the current directory.

