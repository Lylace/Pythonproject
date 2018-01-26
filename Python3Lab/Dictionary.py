#딕셔너리 : 매핑 자료구조
#키에 값을 연결시키는 방식으로 데이터를 다루는 방법 제공
#키는 저장된 데이터를 식별하기 위한 번호나 이름
#값은 각 키에 연결되어 저장된 데이터
#따라서, 키만 알면 데이터를 바로 찾을 수 있음
#딕셔너리는 { }에 키:값 형태로 이용
#키:값이 여러개 존재 할 경우 , 로 구분

menu = { '1' : 'newSungJuk', 2 : 'showSungJuk', 'abc' : 'modifySungJuk' }
        #키는 다양한 자료형으로 사용 가능

book = {
         'bookid' : ['1', '2', '3', '4'],
         'bookname' : ['축구의 역사','축구아는 여자','축구의 이해','골프 바이블','피겨 교본'],
         'publisher' : ['굿스포츠', '나무수', '대한미디어', '대한미디어', '굿스포츠'],
         'price' : ['7000', '13000', '22000', '35000', '8000']
}

order = {
    'orderid' : '1', 'custid' : '1', 'bookid' : '1', 'price' : '7000', 'orderdate' : '2014-07-01',
    'orderid' : '2', 'custid' : '1', 'bookid' : '2', 'price' : '13000', 'orderdate' : '2014-07-03',
    'orderid' : '3', 'custid' : '2', 'bookid' : '5', 'price' : '8000', 'orderdate' : '2014-07-03',
    'orderid' : '4', 'custid' : '3', 'bookid' : '2', 'price' : '13000', 'orderdate' : '2014-07-04',
    'orderid' : '5', 'custid' : '4', 'bookid' : '4', 'price' : '35000', 'orderdate' : '2014-07-05',
    'orderid' : '6', 'custid' : '1', 'bookid' : '3', 'price' : '22000', 'orderdate' : '2014-07-07',
    'orderid' : '7', 'custid' : '4', 'bookid' : '3', 'price' : '22000', 'orderdate' : '2014-07-07'
}

customer = {
    'custid' : '1', 'name' : '박지성', 'address' : '영국 런던', 'phone' : '000-5000-0001',
    'custid' : '1', 'name' : '박지성', 'address' : '영국 런던', 'phone' : '000-5000-0001',
    'custid' : '1', 'name' : '박지성', 'address' : '영국 런던', 'phone' : '000-5000-0001',
    'custid' : '1', 'name' : '박지성', 'address' : '영국 런던', 'phone' : '000-5000-0001'
}

books_list = []
for i in range(0,4):
    books_list.append(book['bookid'][i] + ' ')
    books_list.append(book['bookname'][i] + ' ')
    books_list.append(book['publisher'][i]+ ' ')
    books_list.append(book['price'][i]+ ' ')
    books_list.append('\n')

print(''.join(books_list))

#딕셔너리 처리 메서드
print('1' in book)      #딕셔너리에서 in 연산자는 key를 검색
print('bookid' in book)

print(book['bookid'])       #딕셔너리에서 키로 검색
print(book['bookname'])
print(book['price'])
# print(book['orderid'])    #존재하지 않는 키 검색 시 오류!

print(book.get('bookid'))
book['bookid'] = 99         #키로 값 수정
print(book.get('orderid'))  #존재하지 않는 키 검색 시 None 출력

print(book)
book.update({'판형' : '3x4'}) #새로운 키 : 값 추가/수정
print(book)

print(book)
book.update({'판형' : '6x10'}) #새로운 키 : 값 추가/수정
print(book)

del book['판형']              #기존 키 삭제
print(book)

# book.clear()                  #모든 키 삭제

print(book.keys())             #모든 키를 출력
print(book.values())           #모든 값을 출력
print(book.items())            #모든 키:값을 튜플로 출력

items = book.items()           #모든 키:값을 튜플-리스트로 출력
print( list(items) )