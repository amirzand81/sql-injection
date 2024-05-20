from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
import jwt
import datetime
from django.conf import settings

# Ensure your SECRET_KEY is in settings.py
SECRET_KEY = settings.SECRET_KEY

def get_user(user_id, password):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM users WHERE user_id='{user_id}' AND password='{password}'")
        row = cursor.fetchone()
        
    return row

def create_jwt(user):
    payload = {
        'user_id': user[0],  # Assuming user_id is the first field in the tuple
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

@csrf_exempt
def login_view(request):

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        user = get_user(user_id, password)
        if user:
            token = create_jwt(user)
            request.session['token'] = token
            return redirect('/search/')
        else:
            HttpResponse('Invalid credentials', status=401)
            return redirect('/login/')
        
    return render(request, 'login.html')


def search_view(request):
    token = request.session.get('token')
    if not token:
        return redirect('/login/')
    
    search_query = request.GET.get('search_query', '')
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        
    except jwt.ExpiredSignatureError:
        HttpResponse('Token expired', status=401)
        return redirect('/login/')

    except jwt.InvalidTokenError:
        HttpResponse('Invalid token', status=401)
        return redirect('/login/')

    products = []
    
    if search_query:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM products WHERE name LIKE '{search_query}'")
            products = cursor.fetchall()
        
        product_dicts = [
            {
                'product_id': product[0],
                'name': product[1],
                'owner': product[2],
                'description': product[3],
                'count': product[4],
                'price': product[5],
                'category': product[6],
            }
            
            for product in products
        ]
        
    else:
        product_dicts = []

    return render(request, 'search.html', {'products': product_dicts, 'search_query': search_query})
