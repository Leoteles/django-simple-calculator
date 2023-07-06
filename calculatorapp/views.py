from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader

# Create your views here.
def index(request):
    # template = loader.get_template('calculatorapp/index.html')
    # context = {
    #     'latest_question_list':[1,2,3]
    # }
    # return HttpResponse('sdffdsasdfsdaasdfsd')
    # return HttpResponse(template.render(context,request))
    return render(request,'calculatorapp/index.html')

def submitquery(request):
    try:
        q = request.GET['query']
        ans = eval(q)
        json_dict = {'q':q,
                     'ans': ans,
                     'error':False,
                     'result':True}
    except:
        json_dict = {
            'error': True,
            'result': False,
        }
    return render(request,'calculatorapp/index.html',context=json_dict)
    # return JsonResponse(json_dict)