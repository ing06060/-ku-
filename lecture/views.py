from bs4 import BeautifulSoup
import requests
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Lecture
from .forms import SearchForm
from django.shortcuts import redirect


def form_test(request):
    full_list=[]
    if request.method=='POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            num = form.data['number']
            full_list=getLectureList(num)
            return render(request,'result.html',{'full_list':full_list})

    elif request.method=='GET':
        form = SearchForm()
        return render(request,'search.html',{'form':form})
    else:
        pass


def getLectureList(num):
    data=[]
    td_list=[]
    for i in range(1,5):
        req = requests.get('https://kupis.konkuk.ac.kr/sugang/acd/cour/aply/CourBasketInwonInq.jsp?ltYy=2020&ltShtm=B01012&promShyr='+str(i)+'&fg=B&sbjtId='+str(num))
        soup = BeautifulSoup(req.text, 'html.parser')
        name = soup.find('h2',class_='mt0').text
        number = num
        trs = soup.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            for td in tds:
                td_list.append(td.text)

    for i in td_list[1::2]:
        for each in i.split('/'):
            td_list.append(each.strip())
    del td_list[1:8:2]

    data.append(
        {
            'name':name,
            'number':num,
            'fresh_suguni':td_list[0],
            'fresh_sugang':td_list[4],
            'fresh_limit':td_list[5],
            'sopho_suguni':td_list[1],
            'sopho_sugang':td_list[6],
            'sopho_limit':td_list[7],
            'junior_suguni':td_list[2],
            'junior_sugang':td_list[8],
            'junior_limit':td_list[9],
            'senior_suguni':td_list[3],
            'senior_sugang':td_list[10],
            'senior_limit':td_list[11]
        }
    )
    print(data)
    return data

#         policy_url = 'http://www.chemicalnews.co.kr/news/articleList.html?sc_section_code=S1N1&view_type=sm'
#         req = requests.get(policy_url)
#         req.encoding = 'utf-8'
#         html = req.text

#         soup = BeautifulSoup(html, 'html.parser')
#         list_items = soup.find_all('div', class_='list-block')

#         policy_data = []
#         chemical = 'http://www.chemicalnews.co.kr/'

#         for item in list_items:
            
#             title = item.find('div',class_='list-titles').text

#             link = item.find('div',class_='list-image').find('a')
#             if 'href' in link.attrs:
#                 conn = link.attrs['href']

#             image= item.find('div',class_='list-image')['style']
            
#             style = cssutils.parseStyle(image)
#             url = style['background-image']
#             url = url.replace('url(.','').replace(')','')

#             content = item.find('p',class_='list-summary').text

#             etc = item.find('div',class_='list-dated').text
            
#             policy_data.append(
#                 {
#                 'title': title,
#                 'link': chemical + conn,
#                 'img': chemical + 'news/'+ url,
#                 'content': content[0:150],
#                 'etc': etc
#                 }
#             )
#         return render(request, 'news/policy.html',{'policy_data' : policy_data})
#         #     return policy_data

#         # policy_data = policy()
#         # for item in policy_data:
#         #     t = item.get('title')
#         #     l = item.get('link')
#         #     i = item.get('img')
#         #     c = item.get('content')
#         #     e = item.get('etc')
#         #     SearchNews(title=t, link=l,img=i, content=c,etc=e).save()

#         # for t,l,i,c,e in policy_data.items():
#         #     SearchNews(title=t, link=l).save()
#             # return render(request, 'news/policy.html',{'policy_data' : policy_data})
# class getLetureList(View):
#     model = Lecture








