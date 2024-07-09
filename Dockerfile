FROM python:3.9-slim
WORKDIR /usr/src/app
COPY scrape_web_page.py /usr/src/app/scrape_web_page.py
RUN pip install requests beautifulsoup4
RUN chmod +x /usr/src/app/scrape_web_page.py
CMD ["python", "/usr/src/app/scrape_web_page.py"]