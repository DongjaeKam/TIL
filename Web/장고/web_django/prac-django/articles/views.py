from django.shortcuts import render

import random

# Create your views here.

def index(request):
    #메인 페이지를 보여준다.

    names= ['john','smith','bob','ailen','quick']

   
   
   
    context = { "name": "감동재" ,"img" : "https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg"}


    context['name'] = random.choice(names)


    return render(request,'index.html',context)

def welcome(request,name):
    
    names= ['john','smith','bob','ailen','quick']
    
    


    context = { "name": "감동재" ,"img" : "https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg"}


    context['name'] = name
  

    return render(request,'welcome.html',context)



def menu(request):

    menu= ['삼겹살','라면','국밥']
    images = ['https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/201702/27/117f5b49-1d09-4550-8ab7-87c0d82614de.jpg' ,'https://health.chosun.com/site/data/img_dir/2020/09/07/2020090702900_0.jpg','https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA4MzFfMjgw%2FMDAxNjYxOTE4OTc4NjY2.fMgtlRv-QCroHMV_-nUErOwfkhmk-g_Wqf60Ed77hm0g.2SlF_wajp0GsG9URjqUlZBP0kQVtkBVweTVVa5iHtAEg.JPEG.susanjang0228%2FKakaoTalk_20220831_124646060_17.jpg&type=sc960_832' ]
    i = random.randint(0,2) 

    context = { "menu": menu[i] ,"img" : images[i]}

    return render(request,'menu.html',context)


def lotto(request):

    numbers= []

    for i in range(5):

        number=set([])

        while len(number) < 6:
            number.add(random.randint(1, 45))

        numbers.append(list(number))

        
    context = { "numbers": numbers }
    return render(request,'lotto.html',context)