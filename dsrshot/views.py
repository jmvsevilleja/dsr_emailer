import base64
from selenium import webdriver
from datetime import datetime
from django.conf import settings
from django.http import HttpResponse
import urllib.parse as urlparse
import os
from django.shortcuts import render

import chromedriver_install as cdi

# Create your views here.


def index(request):

    return render(request, 'dsrshot/index.html',)


def get_screenshot(request):
    """
    Take a screenshot and return a png file based on the url.
    """

    if request.method == 'POST' and 'url' in request.POST:
        url = request.POST.get('url', '')
        if url is not None and url != '':

            path = cdi.install(file_directory='./lib/', verbose=True,
                               chmod=True, overwrite=False, version=None)
            driver = webdriver.Chrome(path)
            driver.get(url)
            # driver.set_window_size(width, height)

            el = driver.find_element_by_tag_name('body')
            screenshot = el.get_screenshot_as_png()
            # screenshot = driver.get_screenshot_as_png()
            image_64_encode = base64.encodestring(screenshot)
            var_dict = {'screenshot': image_64_encode}

            driver.quit()
            # return render(request, 'index.html', var_dict)
            return render(request, 'dsrshot/index.html', var_dict)
    else:
        return HttpResponse('Error')
