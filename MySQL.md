### mySQL에서 문자열 붙이기

`concat`을 쓰면 된다.

```sql
update perform_seat_info set booked_seat = concat(booked_seat, '3열 4석,', '4열 1석,') where perform_num = 24;
```

- 주의사항: null값일 땐 안됨.
