import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return JsonResponse({
                "status": True, 
                "message": "Login Berhasil", 
                "username": username
            }, status=200)
        else:
            return JsonResponse({
                "status": False, 
                "message": "Username atau password salah"
            }, status=401)
    
    return JsonResponse({"status": False, "message": "Method not allowed"}, status=405)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({"status": False, "message": "Username sudah digunakan"}, status=400)
        
        User.objects.create_user(username=username, password=password)
        return JsonResponse({"status": True, "message": "Akun berhasil dibuat"}, status=200)
    return JsonResponse({"status": False, "message": "Method not allowed"}, status=405)

@csrf_exempt
def logout(request):
    username = request.user.username
    try:
        auth_logout(request)
        return JsonResponse({"status": True, "message": "Logout berhasil", "username": username}, status=200)
    except:
        return JsonResponse({"status": False, "message": "Logout gagal"}, status=401)