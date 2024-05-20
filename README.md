# BFS-crawler
> BFS crawler with url filtering and level checking

# Project Stack
- python
- BeautifulSoup
- urllib

# Project Result
![image](https://github.com/Jaden000/BFS-crawler/assets/84056591/1a5256de-41bd-4c37-961b-e88be0d465b5)


# Description
### Project Design
- BFS 탐색 대상: url <br>
- Seed url: https://news.naver.com 또는 argv[1] <br>
- 차별점: url 필터링, depth 기록

<br>

### Crawling Process
1. seed url(크롤링을 시작할 페이지 url) 지정
2. seed url의 페이지에 등장하는 url 수집
(2.5. 중복 및 관련성 없는 url 제거)
3. url 집합에 접근
4. 2-3 단계의 반복


https://velog.io/@jadennotjade/웹-크롤링crawling-1-BFS를-이용한-크롤링-설계하기 <br>
https://velog.io/@jadennotjade/웹-크롤링crawling-2-BFS-CrawlerBFS-크롤러-구현
