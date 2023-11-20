#!/usr/bin/env python
# coding: utf-8

# # steps for webscraper

# # 1.first we setting up the environment
# 

# In[ ]:


pip install request
pip install html5lib
pip install bs4


# ## 2.get the HTML

# In[ ]:


in order to work with HTML ,we will have to get the HTML as a string


# # 3.parse the HTML

# In[ ]:


once the html is fetched and parsed,the next step is to 
manipulate the tree using bs4 function to get our job done


# 

# In[18]:


pip install requests


# In[19]:


pip install html5lib


# In[20]:


pip install bs4


# In[21]:


import requests
from bs4 import BeautifulSoup
url='https://codewithharry.com'


# In[22]:


r=requests.get(url)


# In[23]:


htmlContent=r.content


# In[24]:


print(htmlContent)


# In[25]:


#parse the html
soup=BeautifulSoup(htmlContent,'html.parser')
print(soup.prettify)


# In[26]:


#commenly used types of objects:
# 1.tag
# 2.navigablestring
#3.comment
#beautifulsoup


# In[27]:


#html tree traversal
title=soup.title
print(type(soup))


# In[28]:


print(type(title.string))


# In[29]:


# get the all paragraph from the page
paras=soup.find_all('p')
print(paras)


# In[30]:


# get the all tags from the page
anchors=soup.find_all('a')
print(anchors)


# In[31]:


#get classes of any elements in the html
print(soup.find('p')['class'])


# In[32]:


#find all the elements with class lead
print(soup.find_all('p',class_='lead'))


# In[33]:


#get the text from the elements
print(soup.find('p').get_text())


# In[34]:


print(soup.get_text())


# In[35]:


#get all the links on the page
anchors=soup.find_all('a')
for link in anchors:
    print(link.get('href'))


# In[36]:


anchors=soup.find_all('a')
all_links=set()
for link in anchors:
    if (link.get('href')!='#'):
        linktext='https://codewithharry.com'+link.get('href')
        all_links.add(link)
        print(linktext)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # WEBSCRAPING USING AUTOSCRAPER

# In[1]:


get_ipython().system('pip install autoscraper')


# In[2]:


from autoscraper import AutoScraper


# In[53]:


flipkart_url="https://www.flipkart.com/search?q=shoes&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_2_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_2_0_na_na_na&as-pos=2&as-type=TRENDING&suggestionId=shoes&requestId=8dcc3865-54f6-41cc-a96e-ce582d893dec"
wanted_list=['₹595','RapidBoxSneakers For Men','20114']


# In[54]:


scraper=AutoScraper()
result=scraper.build(flipkart_url,wanted_list)
print(result)


# In[55]:


scraper.get_result_similar(flipkart_url,grouped=True)


# In[57]:


scraper.set_rule_aliases({'rule_045i':'Title'})
scraper.keep_rules(['rule_045i'])
scraper.save('flipkart-search')


# In[58]:


results=scraper.get_result_similar('https://www.flipkart.com/search?q=shoes%20for%20women&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off',group_by_alias=True)


# In[59]:


results['Title']


# # WEB SCRAPING USIING BEATIFUL SOUP LIBRARY

# In[60]:


pip install beautifulsoup4


# In[61]:


import requests


# In[63]:


from bs4 import  BeautifulSoup


# In[65]:


req=requests.get('https://www.geeksforgeeks.org/courses/search?search=Data%20Structures%20algorithms&source=google&medium=cpc&device=c&keyword=gfg%20dsa%20practice&matchtype=b&campaignid=20299375360&adgroup=156190096491&gad_source=1&gclid=CjwKCAiA9dGqBhAqEiwAmRpTC5fvuc1oH_TeTNw22lWdX0lXCMGOxuEIs3SSacmK3QIuaVxCpUGiwhoCtXYQAvD_BwE')


# In[67]:


soup=BeautifulSoup(req.content,"html.parser")


# In[ ]:





# In[ ]:





# In[69]:


print(soup.get_text())


# In[74]:


print(soup.prettify())


# In[71]:


res=soup.title


# In[72]:


print(res.prettify())


# In[73]:


print(res.get_text())


# In[ ]:





# 

# In[ ]:





# In[ ]:





# # web scraping by using machenical soup

# In[4]:


pip install MechanicalSoup


# In[ ]:



    


# In[ ]:





# In[ ]:




