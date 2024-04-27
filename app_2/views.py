from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def get_inform(request):
    html = """
      <!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <title>Ro'yxatga olish</title>
</head>
<body>
    <h2>Foydalanuvchini Ro'yxatga olish</h2>
    <!-- Foydalanuvchi ma'lumotlarini kiritish uchun shakl -->
    <form action="show-data.html" method="get">
        <label for="name">Ism:</label>
        <input type="text" id="name" name="name" placeholder="Ismingizni kiriting" required>
        <br>

        <label for="age">Yosh:</label>
        <input type="number" id="age" name="age" placeholder="Yoshingizni kiriting" required>
        <br>

        <label for="phone">Telefon:</label>
        <input type="tel" id="phone" name="phone" placeholder="Telefon raqamingizni kiriting" required>
        <br>


    </form>
    <a href="return">Ro'yxatga olish</a>
</body>
</html>


    """
    return HttpResponse(html)


def return_inform(request):
    html = """
        <!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <title>Ro'yxatga olish ma'lumotlari</title>
</head>
<body>
    <h2>Foydalanuvchi Ma'lumotlari</h2>
    <!-- GET parametrlari yordamida ma'lumotlarni ko'rsatish -->
    <p>Ism: <span id="display-name"></span></p>
    <p>Yosh: <span id="display-age"></span></p>
    <p>Telefon: <span id="display-phone"></span></p>

    <!-- JavaScript yordamida GET parametrlari orqali ma'lumotlarni ko'rsatish -->
    <script>
        function getQueryParams() {
            var params = {};
            var queryString = window.location.search.substring(1);
            var queries = queryString.split("&");

            queries.forEach(function(query) {
                var [key, value] = query.split("=");
                params[key] = decodeURIComponent(value);
            });

            return params;
        }

        var queryParams = getQueryParams();

        document.getElementById("display-name").innerText = queryParams["name"];
        document.getElementById("display-age").innerText = queryParams["age"];
        document.getElementById("display-phone").innerText = queryParams["phone"];
    </script>
</body>
</html>


    """
    return HttpResponse(html)
