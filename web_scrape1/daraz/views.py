from django.shortcuts import render,redirect

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
    all_data = TestProduct.objects.all()
    all_data_dict = {'data':all_data}
    return render(request,'daraz/form.html',context=all_data_dict)


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

        return redirect('/daraz/show/')
    else:
        return HttpResponse("This is not POST METHOD")

# Create your views here.

def minus (request):
    pass

