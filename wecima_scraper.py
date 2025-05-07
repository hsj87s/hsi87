import requests
from bs4 import BeautifulSoup

url = 'https://wecima.click/movies'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# استخراج الأفلام
items = soup.select('.Grid--WecimaPosts .GridItem')
html_blocks = ""

for item in items:
    title = item.select_one('.Title').text.strip()
    img = item.select_one('img')['data-src']
    link = item.select_one('a')['href']
    html_blocks += f'''
    <div class="movie-card" onclick="openPlayer('{link}')">
        <img src="{img}" alt="{title}">
        <div class="movie-info">
            <h3>{title}</h3>
        </div>
    </div>
    '''

# تحميل قالب index.html
with open("index.html", "r", encoding="utf-8") as f:
    html_template = f.read()

# إدخال المحتوى في div#movieContainer
output_html = html_template.replace(
    '<div class="container" id="movieContainer">', 
    f'<div class="container" id="movieContainer">\n{html_blocks}'
)

# حفظ النتيجة
with open("index.html", "w", encoding="utf-8") as f:
    f.write(output_html)

print("تم تحديث الموقع بنجاح!")