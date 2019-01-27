from django.http import JsonResponse
import tushare as ts

'''
a:代码 '000001'
b:日期 '2018-12-12'
'''

def tick_data(request):
    if request.method == "POST":
        a = request.POST.get('a')
        b = request.POST.get('b')
    else:
        a = request.GET.get('a')
        b = request.GET.get('b')
    df = ts.get_tick_data(a, date=b, src='tt')
    for index, row in df.iterrows():
        print('index:' + str(index))
        print(row)
        '''
        index:934
        time      15:00:05
        price         7.99
        change           0
        volume        5970
        amount     4770030
        type            卖盘
        Name: 934, dtype: object
        [21/Jan/2019 19:45:20] "GET /tick/?a=300080&b=2019-01-21 HTTP/1.1" 200 112707
        '''
    if df is None:
        jsondata = ''
    else:
        jsondata = df.to_json(orient='index')
    response = JsonResponse({'tick': jsondata})
    response["Access-Control-Allow-Headers"] = "Origin,Content-Type,Cookie,Accept,Token"
    return response