from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def first_func(request):
    html = """
    <!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <title>Foydalanuvchi Ma'lumotlari</title>
</head>
<body>
    <!-- Foydalanuvchi ma'lumotlarini kiritish uchun shakl -->
    <h2>Foydalanuvchi Ma'lumotlari</h2>
    <form>
        <!-- Ism kiritish -->
        <label for="name">Ism:</label>
        <input type="text" id="name" name="name" placeholder="Enter your name" required>
        <br>

        <!-- Yosh kiritish -->
        <label for="age">Yosh:</label>
        <input type="number" id="age" name="age" placeholder="Enter your age" min="1" required>
        <br>

        <!-- Telefon raqamini kiritish -->
        <label for="phone">Telefon raqami:</label>
        <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" pattern="[0-9]{10}" required>
        <br>
        <a href="2">Keyingi sahifa</a>

    </form>
</body>
</html>



    """
    return HttpResponse(html)


def second_func(request):
    html = """
    <!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <title>Bizning Ijtimoiy Tarmoqlar</title>
</head>
<body>
    <h2>Bizni Ijtimoiy Tarmoqlarda Toping</h2>

    <!-- Instagram uchun havola -->
    <a href="https://www.instagram.com/" target="_blank">Instagram</a>
    <br>

    <!-- YouTube uchun havola -->
    <a href="https://www.youtube.com/" target="_blank">YouTube</a>
    <br>

    <!-- Telegram uchun havola -->
    <a href="https://t.me/" target="_blank">Telegram</a>
    <br>

    <!-- Oldingi sahifaga qaytish uchun havola -->
    <a href="1">Oldingi sahifaga qaytish</a>
</body>
</html>



    """
    return HttpResponse(html)
