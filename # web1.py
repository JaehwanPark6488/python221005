# web1.py
from bs4 import BeautifulSoup

#문자열로 로딩
page = open("c:\\work\\test01.html","rt", encoding ="utf-8").read()

#검색이 용이한 스프 객체
soup = BeautifulSoup(page, "html.parser")
#print( soup.prettify() )
# <p>전체를 검색
print( soup.find_all("p") )
