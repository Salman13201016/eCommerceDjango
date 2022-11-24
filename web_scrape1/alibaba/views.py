from django.shortcuts import render

from django.shortcuts import HttpResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def show(request):
    # return HttpResponse("Welcome to alibaba")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.ubereats.com/ie/search?diningMode=DELIVERY&kn=BreakfastAndBrunch&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMk5ldyUyMFlvcmslMjIlMkMlMjJyZWZlcmVuY2UlMjIlM0ElMjJDaElKT3dnXzA2VlB3b2tSWXY1MzRRYVBDOGclMjIlMkMlMjJyZWZlcmVuY2VUeXBlJTIyJTNBJTIyZ29vZ2xlX3BsYWNlcyUyMiUyQyUyMmxhdGl0dWRlJTIyJTNBNDAuNzEzNTIlMkMlMjJsb25naXR1ZGUlMjIlM0EtNzQuMDA2ODg1JTdE&q=Breakfast%20%26%20brunch&sc=HOME_FEED_ITEM')
    title = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='main-content']/div/div/div[2]/div/div[3]/div[1]/div/a/h3"))).text
    
    scrape  = {"title":title,"price":90}

    # return HttpResponse(title)

    return render(request,'alibaba/form.html',context=scrape)

# Create your views here.
