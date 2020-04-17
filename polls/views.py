from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
# Create your views here.
from django.http import HttpResponse
from .models import Question, Choice
q = Question.__str__
from .forms import *
# from bs4 import BeautifulSoup
# import urllib.request
# # 
# def get(url):
#     page = urllib.request.urlopen(url)
#     soup = BeautifulSoup(page, 'html.parser')
#     # print(soup)
#     new_feed = soup.find('table', class_='table table-condensed').find_all('a')
#     prob = [new_feed]

#     num_prob = 0
#     for p in new_feed:
#         link = p.get('href')
#         str = p.string
#         if not str:
#             continue
#         num_prob+=1
#     return num_prob
def index(request):
    

    # url =  'https://www.spoj.com/PTIT/users/lebahoailamson/'
    # num_prob = get('https://www.spoj.com/PTIT/users/meoconxinhxan/')
    # page = urllib.request.urlopen(url)
    # soup = BeautifulSoup(page, 'html.parser')

    # print(soup)
    # new_feed = soup.find('table', class_='table table-condensed').find_all('a')
    # prob = [new_feed]

    # num_prob = 0
    # for p in new_feed:
    #     link = p.get('href')
    #     str = p.string
    #     if not str:
    #         continue
    #     num_prob+=1;    
        # print('Link: {}'.format( str))

    # latest_question_list = Question.objects.get(pk = 1)
    # context = {'latest_question_list': latest_question_list}
    return render(request,"/home/hoaileba/PythonDJ/WEB/mysite/polls/templates/index.htm")

def detail(request,question_id):
    return HttpResponse("you are looking at question : %s" % question_id)


def upload(request):
    print(request.method)
    img = ""
    if request.method == "POST":
        uploaded =  request.FILES["photo"]
        # path += uploaded.name
        # print(path)
        fs  = FileSystemStorage()
        name = fs.save(uploaded.name,uploaded)
        img = fs.url(name)
        # form = ImageForm(request.POST,request.FILES)
        # # print(request.FILES["document"].name)
        # if form.is_valid():
        #     form.save()
        #     return redirect('success')
    else :
        form = ImageForm()
    
    return render(request,'/home/hoaileba/PythonDJ/WEB/mysite/polls/templates/index.htm',{'direct' : img})