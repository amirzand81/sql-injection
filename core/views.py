from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection, DatabaseError
from django.views.decorators.csrf import csrf_exempt
import jwt
import datetime
from django.conf import settings

# Ensure your SECRET_KEY is in settings.py
SECRET_KEY = settings.SECRET_KEY

def get_user(user_id, password):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM users WHERE user_id='{user_id}' AND password='{password}'")
            row = cursor.fetchone()
    except DatabaseError as e:
        print(f"Database error: {e}")
        return None

    if row is not None:
        return list(row)[-1]

def create_jwt(user):
    payload = {
        'user_id': user[0],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def decode_jwt(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return HttpResponse('Token expired', status=401)
    except jwt.InvalidTokenError:
        return HttpResponse('Invalid token', status=401)

@csrf_exempt
def login_view(request):

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        user = get_user(user_id, password)
        
        if user == 'Admin':
            token = create_jwt(user)
            request.session['token'] = token
            return redirect('/panel/')
        
        elif user == 'Regular' or user == 'Guest':
            token = create_jwt(user)
            request.session['token'] = token
            return redirect('/search/')
        
        else:
            return HttpResponse('Invalid credentials', status=401)
        
    return render(request, 'login.html')

def search_view(request):
    token = request.session.get('token')
    if not token:
        return redirect('/login/')
    
    search_query = request.GET.get('search_query', '')
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return HttpResponse('Token expired', status=401)
    except jwt.InvalidTokenError:
        return HttpResponse('Invalid token', status=401)

    products = []
    
    if search_query:
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM products WHERE name LIKE '{search_query}'")
                products = cursor.fetchall()
        except DatabaseError as e:
            print(f"Database error: {e}")
            products = []
        
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

def admin_panel(request):
    token = request.session.get('token')
    if not token:
        return redirect('/login/')
    
    payload = decode_jwt(token)
    if isinstance(payload, HttpResponse):
        return payload

    if payload['user_id'] != 'A':
        return HttpResponse('Not Allowed', status=403)

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()
    except DatabaseError as e:
        print(f"Database error: {e}")
        return HttpResponse('Database error', status=500)

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

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
    except DatabaseError as e:
        print(f"Database error: {e}")
        return HttpResponse('Database error', status=500)

    user_dicts = [
        {
            'user_id': user[0],
            'name': user[1],
            'password': user[2],
            'address': user[3],
            'age': user[4],
            'phone': user[5],
            'user_type': user[6]
        }
        for user in users
    ]

    return render(request, 'panel.html', {'products': product_dicts, 'users': user_dicts})
