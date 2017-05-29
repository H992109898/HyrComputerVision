from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import product
from database_model import user
from database_model import connection
from database_model import mycount
from database_model import user_product
import thread

@csrf_exempt
def login(request):

    data = json.loads(request.body)    
    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = "*"
    conn = connection.conn
    cursor = conn.cursor()
    res = user.search_by_username(cursor, data['username'])
    if res == 0:
        response.write(0)
    else:
        if(data['password'] == res['password']):
            response.write(1)
        else:
            response.write(0)    
    cursor.close()
    return  response

#return 1 if success, return 0 if username exist, return -1 if email exist
@csrf_exempt
def register(request):
    data = json.loads(request.body)    
    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = "*"
    conn = connection.conn
    cursor = conn.cursor()
    if user.exist_username(cursor, data['username']):
        response.write(0)
    elif user.exist_email(cursor, data['email']):
        response.write(-1)
    else:
        user.add(cursor, data['username'], data['password'], data['email'])
        response.write(1)
    cursor.close()

    return  response

@csrf_exempt
def myaccount_server(request):

    response = HttpResponse()
    if(request.POST.get('change_head') == "true"):
       
        mycount.change_head(request.FILES.get('img'), request.POST.get('username'))
        response.write(1)
        
    if(request.POST.get('init_data') == "true"):
        user_info = mycount.init_data_request(request.POST.get('username'))
        del user_info['registered_time']
        response.write(json.dumps(user_info))
    
    if(request.POST.get('init_buy_record') == "true"):
        response.write(json.dumps(user_product.search_by_username(request.POST.get('username'))))
    
    if(request.POST.get('change_info') == "true"):
        response.write(mycount.change_user_info(request.POST.get('username'), request.POST.get('password'),request.POST.get('email')))
    
    response['Access-Control-Allow-Origin'] = "*"
    return response

        
@csrf_exempt
def buy_product(request):
    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = "*" 
    data = json.loads(request.body)
            
    if user_product.is_exist(data['username'], data['product'], data['type']):
        response.write(0)
    else:
        response.write(1)
        
        user_product.add_buy_product_record(data['username'], data['product'], data['type'])
    
    return  response

@csrf_exempt
def emotion(request):
    data = json.loads(request.body)    
    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = "*"
    print json.dumps(product.emotion.predict.get_result(data['url']))
    response.write(json.dumps(product.emotion.predict.get_result(data['url'])))
    
    return response

@csrf_exempt
def emotion_file(request):
    img = request.FILES.get('img')
    f = open("test.png", "wb")
    for chunk in img.chunks():
        f.write(chunk)
    f.close()
    response = HttpResponse()
    response.write(json.dumps(product.emotion.predict.get_file_result("test.png")))
    response['Access-Control-Allow-Origin'] = "*"
    
    return response

@csrf_exempt
def face(request):
    data = json.loads(request.body)    
    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = "*"
    response.write(json.dumps(product.face.predict.get_result(data['url'])))
    return response

@csrf_exempt
def face_file(request):
    img = request.FILES.get('img')
    f = open("test.png", "wb")
    for chunk in img.chunks():
        f.write(chunk)
    f.close()
    response = HttpResponse()
    response.write(json.dumps(product.face.predict.get_file_result("test.png")))
    response['Access-Control-Allow-Origin'] = "*"
    
    return response

@csrf_exempt
def carPlate(request):
#     data = json.loads(request.body)    
    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = "*"
    response.write(1)
    return response

@csrf_exempt
def carPlate_file(request):
    img = request.FILES.get('img')
    f = open("test.png", "wb")
    for chunk in img.chunks():
        f.write(chunk)
    f.close()

    response = HttpResponse()
    response.write(json.dumps({'fuck_you':1}))
    response['Access-Control-Allow-Origin'] = "*"

    return response

@csrf_exempt
def object(request):
#     data = json.loads(request.body)    
    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = "*"
    response.write(1)
    return response

@csrf_exempt
def object_file(request):
    img = request.FILES.get('img')
    f = open("test.png", "wb")
    for chunk in img.chunks():
        f.write(chunk)
    f.close()
    response = HttpResponse()
    response.write(1)
    response['Access-Control-Allow-Origin'] = "*"
    
    return response


def index_html(request):
    return render(request, 'index.html')

def app_html(request):
    return render(request, 'app.html')

def carPlate_html(request):
    return render(request, 'carPlate.html')

def document_html(request):
    return render(request, 'document.html')

def emotion_html(request):
    return render(request, 'emotion.html')

def face_html(request):
    return render(request, 'face.html')

def login_html(request):
    return render(request, 'login.html')

def myAccount_html(request):
    return render(request, 'myAccount.html')

def object_html(request):
    return render(request, 'object.html')

def price_html(request):
    print 111
    return render(request, 'price.html')

def registered_html(request):
    return render(request, 'registered.html')



