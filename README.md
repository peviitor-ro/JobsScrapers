
# Job Scrapers for Peviitor.ro

This project aims to streamline the process of gathering job details, including job title, city, country, and link, and subsequently integrating them into the peviitor.ro. This initiative leverages the power of Python and incorporates essential libraries like bs4 (Beautiful Soup) and requests for web scraping.

## Objectives

This project encompasses the following primary objectives:

- Enhanced Accessibility: Facilitate easier access to job listings for a wider audience by extracting data from various company websites and seamlessly integrating it into peviitor.ro.

- Automated Data Refresh: Integrate scrapers into GitHub Actions for scheduled, daily execution, ensuring that the job listings remain current and reliable.

- Data Validation Testing: Conduct thorough testing of the scrapers to validate that the scraped data aligns precisely with the information available on peviitor.ro.

## Features

The project incorporates the following key features:

- BeautifulSoup4 (bs4): A Python library for web scraping purposes, allowing for efficient extraction of data from HTML and XML files.
- Requests: A popular Python library for making HTTP requests, essential for fetching web page content.
- GitHub Actions: Enables automated workflows directly from GitHub repositories, in this context, ensuring regular updates of job listings.
- Pytest: A testing framework for Python that facilitates efficient and scalable testing.
- API Testing: In-depth testing of APIs to guarantee data accuracy and reliability.
- Multiple Assertions: Rigorous validation of multiple data points to ensure comprehensive accuracy.
- Data Validation: The project emphasizes the importance of verifying scraped data against the information available on peviitor.ro.

## API Test Run with parallel running

[https://github.com/peviitor-ro/JobsScrapers/assets/91252395/26dfbf52-d1c0-4213-8331-963ebd1dd94f](https://github-production-user-asset-6210df.s3.amazonaws.com/91252395/278391776-26dfbf52-d1c0-4213-8331-963ebd1dd94f.mp4)

## API Test Run without parallel running

[https://github.com/peviitor-ro/JobsScrapers/assets/91252395/8acaafb9-dff0-4f4f-ad7c-3f138e2daba8](https://github-production-user-asset-6210df.s3.amazonaws.com/91252395/277583302-8acaafb9-dff0-4f4f-ad7c-3f138e2daba8.mp4)

## HTML Report

For detailed insights into the test results, an HTML report is generated, providing a comprehensive overview of the scraping process.

![jobsscrapersapi](https://github.com/peviitor-ro/JobsScrapers/assets/91252395/49a3f31e-72c0-4c0b-acd9-265bc8160f51)


## Setup

To get started with the project, follow these steps:

- Install and Configure Python 3: Ensure you have Python 3 installed and properly configured on your system.
- Set Up Your IDE: Prepare your preferred Integrated Development Environment (IDE) for working on this project.
- Import Cloned Repository as Project: Clone the repository and import it into your IDE as a new project.
- Add Folder Path to PYTHONPATH: Include the path of the project folder in the PYTHONPATH variable in your environment settings.
- Install Required Packages: Use the following command to install all the necessary packages: 
```bash
pip install -r requirements.txt
```
- Running Tests: Execute the tests by running the following command:
```bash
pytest
```
