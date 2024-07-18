### mySQL에서 문자열 붙이기

`concat`을 쓰면 된다.

```sql
update perform_seat_info set booked_seat = concat(booked_seat, '3열 4석,', '4열 1석,') where perform_num = 24;
```

- 주의사항: null값일 땐 안됨.

<br><br>

## 식별 관계

**부모테이블의 기본키(PK)를 자식테이블에서 외래키(FK)이자 기본키(PF)로 사용**하는 관계

```
- 부모 테이블의 주키(Primary Key)가 자식 테이블의 주키로 사용되는 관계.
- 부모 테이블의 주키가 자식 테이블의 FK이자 PK로 사용되는 경우를 말한다.
- 자식 테이블의 행을 추가할 때 부모 테이블의 참조행이 없다면 자식 테이블의 행을 추가하는 일이 불가능하다.
- 게시판 글과 글에 딸린 첨부파일과의 관계를 예로 들 수 있다 (첨부파일은 반드시 포함되는 글이 있어야 한다).
```

부모 테이블의 PK가 자식 테이블에서도 PK로 쓰였다면? 식별관계 → **직선**으로 표시

<br>

**⇒ PK, FK 동시에 설정하는 방법**

```sql
CREATE TABLE OrderDetails2 ( PFOrder_ID NUMBER(3), PFProduct_ID NUMBER(3),
CONSTRAINT PF PRIMARY KEY (PFOrder_ID, PFProduct_ID),
CONSTRAINT FK_1 FOREIGN KEY (PFProduct_ID) REFERENCES Product(Product_ID),
CONSTRAINT FK_2 FOREIGN KEY (PFOrder_ID) REFERENCES Orderr(Order_ID) );

출처: https://micropilot.tistory.com/2390
```

<br>

## 비식별 관계

: **부모테이블의 기본키(PK)를 자식테이블에서 외래키(FK)로만 사용**하는 관계

```
- 부모 테이블의 주키가 자식 테이블의 일반 컬럼이나 외부키(Foreign Key) 컬럼에 저장되는 관계
- 자식 테이블의 행을 추가할 때 부모 테이블에 참조 행이 없이도 자식 테이블에는 행을 추가하는 일이 가능하다
- 부모 테이블의 주키가 자식 테이블의 FK컬럼에 저장되더라도 FK는 null 을 허용하기 때문에 부모 테이블의 참조행이 없어도 자식 테이블의 행을 추가할 수 있다
- 부서 테이블과 사원 테이블의 관계를 예로 들 수 있다(부서를 배정 받지 못한 사원도 사원 테이블에 추가할 수 있어야 한다)
```

<br><br>

# 각종 오류 해결

### Public Key Retrieval is not allowed ~ 오류 발생 시.

> jdbc:mysql://localhost:3306/river?`allowPublicKeyRetrieval=true`

DB연결할 때 위와 같이 추가해주면 해결된다. MySQL 8.0 이상 버전일 때 나는 오류라고 함.

(오류 날 때도 있고, 안날 때도 있고..)
