## html의 radio 버튼이 변경될 시 이벤트 처리

```javascript
$("input[name='payment']").change(function () {
  var test = $("input[name='payment']:checked").val();
  alert(test);
});
```

```html
input type="radio" name="payment" value="신용카드" checked>신용카드
<input type="radio" name="payment" value="무통장입금" />무통장입금
<input type="radio" name="payment" value="휴대폰결제" />휴대폰결제
```

<br>
현재 진행 중인 프로젝트(포트폴리오)에 적용해보았다. script만 변경.

```javascript
$(document).ready(function () {
  $("#selectPay_phone").hide(); // 초깃값 설정
  $("#selectPay_noBank").hide(); // 초깃값 설정

  $("input[name='payment']").change(function () {
    // 휴대폰 결제 선택 시.
    if ($("input[name='payment']:checked").val() == "휴대폰결제") {
      $("#selectPay_card").hide();
      $("#selectPay_noBank").hide();
      $("#selectPay_phone").show();
    }
    // 무통장입금 결제 선택 시.
    else if ($("input[name='payment']:checked").val() == "무통장입금") {
      $("#selectPay_card").hide();
      $("#selectPay_phone").hide();
      $("#selectPay_noBank").show();
    }
    // 신용카드 결제 선택 시.
    else if ($("input[name='payment']:checked").val() == "신용카드") {
      $("#selectPay_phone").hide();
      $("#selectPay_noBank").hide();
      $("#selectPay_card").show();
    }
  });
});
```
