from django.shortcuts import render

# Create your views here.
from .models import TestProduct
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
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver.get('https://www.ubereats.com/ie/search?diningMode=DELIVERY&kn=BreakfastAndBrunch&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMk5ldyUyMFlvcmslMjIlMkMlMjJyZWZlcmVuY2UlMjIlM0ElMjJDaElKT3dnXzA2VlB3b2tSWXY1MzRRYVBDOGclMjIlMkMlMjJyZWZlcmVuY2VUeXBlJTIyJTNBJTIyZ29vZ2xlX3BsYWNlcyUyMiUyQyUyMmxhdGl0dWRlJTIyJTNBNDAuNzEzNTIlMkMlMjJsb25naXR1ZGUlMjIlM0EtNzQuMDA2ODg1JTdE&q=Breakfast%20%26%20brunch&sc=HOME_FEED_ITEM')
    # # title = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='main-content']/div/div/div[2]/div/div[3]/div[1]/div/a/h3"))).text

    # count = len(driver.find_elements(by=By.CLASS_NAME,value='li'))
    # print("Count",count)

    # total_product = count
    # title_list = []
    # for i in range(1,79):
    #     x_path = '//*[@id="main-content"]/div/div/div[2]/div/div[3]/div['+str(i)+']/div/a/h3'
    #     print(x_path)
    #     title = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, x_path)))

    #     title_list.append(title.text)


    #     print(title_list)


    
    # scrape  = {"title":title_list,"price":90}
    # # time.sleep(500)
    # # driver.quit()

    # # return HttpResponse(title)

    # ti = "Daraz Product One"

    # product = TestProduct(title=ti)
    # product.save()

    return render(request,'daraz/form.html')
def add(request):
    if (request.method == "POST"):
        url = request.POST.get('w_url')
        x1 = request.POST.get('x1')
        x2 = request.POST.get('x2')
        t_count = request.POST.get('t_count')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)
        title_list = []
        for product in range(1,int(t_count)+1):
            loop_div = x1+"div["+str(product)+"]"+x2
            print(loop_div)
            x_path = loop_div
            title = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x_path)))
            title_list.append(title.text)
            product = TestProduct(title=title.text)
            product.save()
        time.sleep(50)
        print(title_list)
            # url = 'https://www.daraz.com.bd/mens-clothing/?page='+str(page)+''
            # driver.get(url)


        #     count = len(driver.find_elements(by=By.CLASS_NAME,value='gridItem--Yd0sa'))
        #     print(count)

        #     for prod in range(1,count+1):
        #         
        #         # print(x_path)
        #         title = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x_path)))

        #         title_list.append(title.text)
        # # 




        # print(len(title_list))
        return HttpResponse(t_count)
        # return render(request,'daraz/form.html')
    else:
        return HttpResponse("This is not POST METHOD")

# Create your views here.

