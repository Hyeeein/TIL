from django.shortcuts import render
from django.http import JsonResponse
from . import starbucks02

def index(request):
    return render(request, 'index.html')

def starbucks(request):
    list_all = list()

    sido_all = starbucks02.getSido()
    for sido in sido_all:
        if sido == '17':
            result = starbucks02.getStore(sido_code=sido)
            print(result)
            list_all.extend(result)
        else:
            gugun_all = starbucks02.getGuGun(sido)
            for gugun in gugun_all:
                result = starbucks02.getStore(gugun_code=gugun)
                print(result)
                list_all.extend(result)

    # print(list_all)
    # print(len(list_all))

    result_dict = dict()
    result_dict['list'] = list_all

    return JsonResponse(result_dict)
    # 앞에서 만든 딕셔너리를 JsonResponse 해주면 장고가 알아서 바꿔서 response 해줌