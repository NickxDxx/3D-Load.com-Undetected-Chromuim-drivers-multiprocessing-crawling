import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

import time
import threading
from multiprocessing import Pool
import requests

import csv
import re




categories_link = ['https://3d-load.net/category/addon-resource/', 'https://3d-load.net/category/aiko-3/', 'https://3d-load.net/category/aiko-4/', 'https://3d-load.net/category/genesis-2-female/aiko-6/', 'https://3d-load.net/category/genesis-3-female/aiko-7/', 'https://3d-load.net/category/genesis-8-female/aiko-8/', 'https://3d-load.net/category/genesis-8-female/alawa-8/', 'https://3d-load.net/category/genesis-8-1-male/alex-capital-8-1/', 'https://3d-load.net/category/genesis-8-female/alexandra-8/', 'https://3d-load.net/category/genesis-8-female/angharad-8/', 'https://3d-load.net/category/characters/animals/', 'https://3d-load.net/category/poses/animations/', 'https://3d-load.net/category/genesis-3-female/arabella-7/', 'https://3d-load.net/category/genesis-8-1-female/arcadia-8-1/', 'https://3d-load.net/category/genesis-8-1-female/arianna-8-1/', 'https://3d-load.net/category/genesis-8-male/ashan-8/', 'https://3d-load.net/category/genesis-8-1-male/assassin-8-1/', 'https://3d-load.net/category/genesis-8-female/aubrey-8/', 'https://3d-load.net/category/genesis-8-1-female/august-8-1/', 'https://3d-load.net/category/genesis-8-female/babina-8/', 'https://3d-load.net/category/genesis-2-female/belle-6/', 'https://3d-load.net/category/genesis-3-female/bethany-7/', 'https://3d-load.net/category/genesis-8-1-female/bonnie-8-1/', 'https://3d-load.net/category/genesis-8-female/bridget-8/', 'https://3d-load.net/category/genesis-2-male/brodie-6/', 'https://3d-load.net/category/genesis-8-1-female/brooke-8-1/', 'https://3d-load.net/category/bundles/', 'https://3d-load.net/category/genesis-2-female/callie-6/', 'https://3d-load.net/category/genesis-8-1-female/catty-8-1/', 'https://3d-load.net/category/genesis-8-female/celani-8/', 'https://3d-load.net/category/genesis-3-female/centaur-7-female/', 'https://3d-load.net/category/genesis-3-male/centaur-7-male/', 'https://3d-load.net/category/characters/', 'https://3d-load.net/category/genesis-8-female/charlotte-8/', 'https://3d-load.net/category/genesis-8-male/christian-8/', 'https://3d-load.net/category/genesis-8-female/cj-8/', 'https://3d-load.net/category/genesis-8-1-female/clara-8-1/', 'https://3d-load.net/category/genesis-8-1-female/cleopatra-8-1/', 'https://3d-load.net/category/clothings/', 'https://3d-load.net/category/genesis-8-1-female/coral-8-1/', 'https://3d-load.net/category/genesis-8-1-female/crow-8-1/', 'https://3d-load.net/category/genesis-8-male/dain-8/', 'https://3d-load.net/category/genesis-8-female/daisy-8/', 'https://3d-load.net/category/genesis-3-male/dante-7/', 'https://3d-load.net/category/genesis-8-female/darcy-8/', 'https://3d-load.net/category/genesis-3-male/darius-7/', 'https://3d-load.net/category/genesis-8-male/darius-8/', 'https://3d-load.net/category/genesis-8-male/dasan-8/', 'https://3d-load.net/category/dawn/', 'https://3d-load.net/category/daz-dog-8/', 'https://3d-load.net/category/daz-dragon-3/', 'https://3d-load.net/category/daz-horse-2/', 'https://3d-load.net/category/genesis-8-male/diego-8/', 'https://3d-load.net/category/genesis-8-male/drutherson-8/', 'https://3d-load.net/category/genesis-8-1-male/ebenezer-8-1/', 'https://3d-load.net/category/genesis-8-female/edie-8/', 'https://3d-load.net/category/genesis-8-male/edward-8/', 'https://3d-load.net/category/genesis-3-male/elijah-7/', 'https://3d-load.net/category/genesis-8-male/elios-8/', 'https://3d-load.net/category/genesis-8-female/ellithia-8/', 'https://3d-load.net/category/environment/', 'https://3d-load.net/category/genesis-3-female/eva-7/', 'https://3d-load.net/category/genesis-8-female/eva-8/', 'https://3d-load.net/category/poses/expression/', 'https://3d-load.net/category/genesis-8-male/floyd-8/', 'https://3d-load.net/category/genesis-8-1-male/fred-8-1/', 'https://3d-load.net/category/genesis-8-female/freja-8/', 'https://3d-load.net/category/genesis-8-female/gabriela-8/', 'https://3d-load.net/category/genesis-2-female/', 'https://3d-load.net/category/genesis-2-male/', 'https://3d-load.net/category/genesis-3-female/', 'https://3d-load.net/category/genesis-3-male/', 'https://3d-load.net/category/genesis-8-female/', 'https://3d-load.net/category/genesis-8-female/genesis-8-female-centaur/', 'https://3d-load.net/category/genesis-8-male/', 'https://3d-load.net/category/genesis-8-male/genesis-8-male-centaur/', 'https://3d-load.net/category/genesis-8-1-female/', 'https://3d-load.net/category/genesis-8-1-male/', 'https://3d-load.net/category/genesis-9-female/', 'https://3d-load.net/category/genesis-9-male/', 'https://3d-load.net/category/genesis-female/', 'https://3d-load.net/category/genesis-male/', 'https://3d-load.net/category/genesis-3-female/genevieve-7/', 'https://3d-load.net/category/genesis-3-female/gia-7/', 'https://3d-load.net/category/genesis-8-female/gia-8/', 'https://3d-load.net/category/genesis-2-male/gianni-6/', 'https://3d-load.net/category/genesis-3-male/gianni-7/', 'https://3d-load.net/category/genesis-2-female/girl-6/', 'https://3d-load.net/category/genesis-2-female/giselle-6/', 'https://3d-load.net/category/genesis-8-1-female/hailey-8-1/', 'https://3d-load.net/category/hair/', 'https://3d-load.net/category/genesis-8-1-male/hans-8-1/', 'https://3d-load.net/category/hiro-3/', 'https://3d-load.net/category/genesis-8-male/holt-8/', 'https://3d-load.net/category/genesis-8-female/honni-8/', 'https://3d-load.net/category/genesis-3-male/ivan-7/', 'https://3d-load.net/category/genesis-3-female/izabella-7/', 'https://3d-load.net/category/genesis-8-1-female/jacqueline-8-1/', 'https://3d-load.net/category/genesis-8-1-male/jazz-8-1/', 'https://3d-load.net/category/genesis-8-female/jenni-8/', 'https://3d-load.net/category/genesis-8-1-female/jinx-jones-8-1/', 'https://3d-load.net/category/genesis-8-female/josephene-8/', 'https://3d-load.net/category/genesis-9-female/josie-9/', 'https://3d-load.net/category/genesis-8-male/juan-carlos-8/', 'https://3d-load.net/category/genesis-8-female/kala-8/', 'https://3d-load.net/category/genesis-3-female/kalea-7/', 'https://3d-load.net/category/genesis-8-female/kanade-8/', 'https://3d-load.net/category/genesis-3-female/karen-7/', 'https://3d-load.net/category/genesis-8-female/karyssa-8/', 'https://3d-load.net/category/genesis-8-1-male/kayden-hd-8-1/', 'https://3d-load.net/category/genesis-8-female/kayo-8/', 'https://3d-load.net/category/genesis-2-female/keiko-6/', 'https://3d-load.net/category/genesis-3-male/kenji-7/', 'https://3d-load.net/category/genesis-8-female/khemsit/', 'https://3d-load.net/category/genesis-8-1-female/kiko-8-1/', 'https://3d-load.net/category/genesis-3-male/kimo-7/', 'https://3d-load.net/category/genesis-8-1-male/kola-8-1/', 'https://3d-load.net/category/genesis-8-1-male/kota-8-1/', 'https://3d-load.net/category/genesis-8-male/kwan-8/', 'https://3d-load.net/category/la-femme/', 'https://3d-load.net/category/genesis-8-male/landon-8/', 'https://3d-load.net/category/genesis-8-female/latonya-8/', 'https://3d-load.net/category/genesis-8-1-female/leanne-8-1/', 'https://3d-load.net/category/genesis-3-male/lee-7/', 'https://3d-load.net/category/genesis-8-male/lee-8/', 'https://3d-load.net/category/genesis-8-female/leisa-8/', 'https://3d-load.net/category/genesis-3-male/leo-7/', 'https://3d-load.net/category/addon-resource/lights/', 'https://3d-load.net/category/genesis-3-female/lilith-7/', 'https://3d-load.net/category/genesis-8-male/lucas-8/', 'https://3d-load.net/category/genesis-3-male/lucian-7/', 'https://3d-load.net/category/genesis-8-female/mabel-8/', 'https://3d-load.net/category/genesis-2-female/mei-lin-6/', 'https://3d-load.net/category/genesis-3-female/mei-lin-7/', 'https://3d-load.net/category/genesis-8-female/mei-lin-8/', 'https://3d-load.net/category/genesis-2-male/michael-6/', 'https://3d-load.net/category/michael-8-1/', 'https://3d-load.net/category/micheal-4/', 'https://3d-load.net/category/micheal-5/', 'https://3d-load.net/category/genesis-3-male/micheal-7/', 'https://3d-load.net/category/genesis-8-male/micheal-8/', 'https://3d-load.net/category/genesis-3-female/mika-7/', 'https://3d-load.net/category/genesis-8-female/mika-8/', 'https://3d-load.net/category/genesis-8-female/millawa-8/', 'https://3d-load.net/category/genesis-9-female/minerva-9/', 'https://3d-load.net/category/genesis-3-female/monique-7/', 'https://3d-load.net/category/genesis-8-female/monique-8/', 'https://3d-load.net/category/genesis-8-male/mr-woo-8/', 'https://3d-load.net/category/genesis-8-female/mrs-chow-8/', 'https://3d-load.net/category/genesis-8-male/niko-8/', 'https://3d-load.net/category/genesis-9-male/nikolai-9/', 'https://3d-load.net/category/genesis-8-male/nix-8/', 'https://3d-load.net/category/non-daz-poser-model/', 'https://3d-load.net/category/genesis-8-1-female/noska-8-1/', 'https://3d-load.net/category/genesis-8-male/ollie-8/', 'https://3d-load.net/category/genesis-2-female/olympia-6/', 'https://3d-load.net/category/genesis-3-female/olympia-7/', 'https://3d-load.net/category/genesis-8-female/olympia-8/', 'https://3d-load.net/category/genesis-3-female/ophelia-7/', 'https://3d-load.net/category/genesis-8-male/owen-8/', 'https://3d-load.net/category/genesis-8-1-male/pablo-8-1/', 'https://3d-load.net/category/genesis-8-female/penny-8/', 'https://3d-load.net/category/genesis-9-female/pixie-9/', 'https://3d-load.net/category/poses/', 'https://3d-load.net/category/props/', 'https://3d-load.net/category/genesis-8-female/robyn-8/', 'https://3d-load.net/category/genesis-8-1-female/rosa-maria-8-1/', 'https://3d-load.net/category/genesis-3-female/rune-7/', 'https://3d-load.net/category/genesis-8-female/rynne-8/', 'https://3d-load.net/category/sahira-8/', 'https://3d-load.net/category/genesis-8-female/sakura-8/', 'https://3d-load.net/category/genesis-8-male/sanjay-8/', 'https://3d-load.net/category/genesis-8-1-male/senator-greaves-8-1/', 'https://3d-load.net/category/genesis-8-male/silas-8/', 'https://3d-load.net/category/sofware/', 'https://3d-load.net/category/star/', 'https://3d-load.net/category/genesis-8-female/stefanie-8/', 'https://3d-load.net/category/victoria-4/stephanie-4/', 'https://3d-load.net/category/genesis-8-female/sukai-8/', 'https://3d-load.net/category/genesis-3-female/sunny-7/', 'https://3d-load.net/category/genesis-8-female/sydney-8/', 'https://3d-load.net/category/genesis-8-female/tara-8/', 'https://3d-load.net/category/genesis-8-female/tasha-8/', 'https://3d-load.net/category/genesis-8-female/teen-jane-8/', 'https://3d-load.net/category/genesis-2-female/teen-josie-6/', 'https://3d-load.net/category/genesis-3-female/teen-josie-7/', 'https://3d-load.net/category/genesis-8-female/teen-josie-8/', 'https://3d-load.net/category/genesis-8-female/teen-kaylee-8/', 'https://3d-load.net/category/genesis-8-1-male/teen-kola-8-1/', 'https://3d-load.net/category/genesis-8-female/teen-raven-8/', 'https://3d-load.net/category/texture-shaders/', 'https://3d-load.net/category/genesis-8-male/the-brute-8/', 'https://3d-load.net/category/genesis-2-female/the-girl-6/', 'https://3d-load.net/category/genesis-3-female/the-girl-7/', 'https://3d-load.net/category/genesis-8-female/the-girl-8/', 'https://3d-load.net/category/genesis-3-male/the-guy-7/', 'https://3d-load.net/category/genesis-8-female/tika-8/', 'https://3d-load.net/category/genesis-8-male/toon-dwayne-8/', 'https://3d-load.net/category/genesis-8-female/topsy-8/', 'https://3d-load.net/category/genesis-8-1-male/torian-8-1/', 'https://3d-load.net/category/genesis-8-1-male/torment-8-1/', 'https://3d-load.net/category/genesis-8-male/tristan-8/', 'https://3d-load.net/category/addon-resource/tutorials/', 'https://3d-load.net/category/genesis-3-female/tween-julie-7/', 'https://3d-load.net/category/genesis-3-male/tween-ryan-7/', 'https://3d-load.net/category/genesis-8-female/twosret-8/', 'https://3d-load.net/category/genesis-8-male/valentino-8/', 'https://3d-load.net/category/victoria-3/', 'https://3d-load.net/category/victoria-4/', 'https://3d-load.net/category/victoria-5/', 'https://3d-load.net/category/genesis-2-female/victoria-6/', 'https://3d-load.net/category/genesis-3-female/victoria-7/', 'https://3d-load.net/category/genesis-8-female/victoria-8/', 'https://3d-load.net/category/genesis-8-1-female/victoria-8-1/', 'https://3d-load.net/category/victoria-9/', 'https://3d-load.net/category/genesis-8-male/vladimir-8/', 'https://3d-load.net/category/genesis-8-1-male/wolfgang-8-1/', 'https://3d-load.net/category/genesis-2-female/ysabeau-6/', 'https://3d-load.net/category/genesis-8-male/yuzuru-8/', 'https://3d-load.net/category/genesis-8-1-male/zale-8-1/', 'https://3d-load.net/category/genesis-8-female/zelara-8/']
categories1 = categories_link[0:19]
categories2 = categories_link[20:39]
categories3 = categories_link[40:59]
categories4 = categories_link[60:79]
categories5 = categories_link[80:99]
categories6 = categories_link[100:119]
categories7 = categories_link[120:139]
categories8 = categories_link[140:159]
categories9 = categories_link[160:179]
categories10 = categories_link[180:199]
categories11 = categories_link[200:]



# def test_func(link):
#     sub_results_links = []
#     browser = uc.Chrome()
#     browser.get(link)
#     browser.maximize_window()
#
#     for x in range(2, 1000):
#         WebDriverWait(browser, 25).until(
#             EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div[3]/div/div/div/div')))
#         container = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[3]/div/div/div/div')
#         results_links_raw = container.find_elements(By.TAG_NAME, 'h2')
#         for link_raw in results_links_raw:
#             link = link_raw.get_attribute('href')
#             sub_results_links.append(link)
#         print("Links added" + str(len(results_links_raw)))
#         print("Total " + str(len(sub_results_links)))
#         try:
#             current_click_page = browser.find_element(By.CLASS_NAME, 'next_page').get_attribute('href')
#             browser.get(current_click_page)
#             print("Go to next page: " + str(x))
#         except:
#             print("Work done")
#             return sub_results_links
#
#
#
#
# # def multip():
# #     links = ["https://3d-load.net/category/addon-resource", "https://3d-load.net/category/aiko-4/", "https://3d-load.net/category/genesis-3-female/aiko-7/"]
# #     pool = Pool(processes=5)
# #     for link_n in range(0,len(links)):
# #         link = links[link_n]
# #         pool.apply_async(test_func(link), args={links[link_n]})
# #
# #     pool.close()
# #     pool.join()
#
#
# if __name__ == '__main__':
#     results_links = []
#     with Pool(5) as p:
#         for sub_results in p.map(test_func, ["https://3d-load.net/category/addon-resource", "https://3d-load.net/category/aiko-4/", "https://3d-load.net/category/genesis-3-female/aiko-7/", "https://3d-load.net/category/characters/animals/", "https://3d-load.net/category/genesis-8-male/ashan-8/", "https://3d-load.net/category/genesis-8-male/edward-8/", "https://3d-load.net/category/genesis-8-female/penny-8/", "https://3d-load.net/category/genesis-2-female/keiko-6/"]):
#             print(sub_results)
#

#
def test_func(links):
    sub_results_links = []
    browser = uc.Chrome()
    browser.maximize_window()
    for x in range(len(links)):
        print("start new work!!!"+ links[x])
        browser.get(links[x])
        print("get new link!!")
        for a in range(2, 1000):
            try:
                WebDriverWait(browser, 25).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'next_page')))
                current_click_page = browser.find_element(By.CLASS_NAME, 'next_page').get_attribute('href')

                container = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[3]/div/div/div/div')
                results_links_raw = container.find_elements(By.TAG_NAME, 'h2')
                for link_raw in results_links_raw:
                    link = link_raw.get_attribute('href')
                    sub_results_links.append(link)
                browser.get(current_click_page)
            except:
                container = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[3]/div/div/div/div')
                results_links_raw = container.find_elements(By.TAG_NAME, 'h2')
                for link_raw in results_links_raw:
                    link = link_raw.get_attribute('href')
                    sub_results_links.append(link)
                print("work done")
                break
    browser.close()
    return sub_results_links
