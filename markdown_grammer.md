`~~strikethrough~~` : ~~strikethrough~~

`>` : Quote (인용문)

> 인용단 여러 단계로 가능함.
>
> > 이렇게
> >
> > > 오오

`[클릭 가능](https://github.com/oneriver2671)` : 클릭되는 링크 생성

`![이미지 내용](이미지 주소)` : 이미지 추가

<br>

- 마크다운 이미지 사이즈 조정

  ```markdown
  ![title](/img/myImg.png){: width="100" height="100"} // 뒤의 px는 생략 가능.
  ![title](/img/myImg.png){: width="100%" height="100%"} // %로도 가능.
  ```

- html로도 이미지 사이즈, 정렬 조정 가능

  ```html
  <center><img src="/img/myImg.png" width="300" height="300" /></center>
  ```

- Table 만들기

  ```
  |Header|Description|

  |--|--|

  | cell1 | cell2 |
  ```

  `| --: | :-- | :--: |` : 오른쪽 정렬 / 왼쪽 정렬/ 가운데 정렬

  <br>

- 글자 색상 넣기
  ```
  <span style="color:red">내용</span>
  ```
  (<span style="color:red">github</span>에서 글자색 변경은 지원되지 않음.)

<br>

- 이모지 &#128525;

```
&#128525;
```

<br>

- `<u>밑줄</u>` : <u>밑줄</u> 긋기. (html 태그)
  (하지만 github에선 지원하지 않는다.)
