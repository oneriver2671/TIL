## jquery에서 부모, 자식 노드를 선택하는 방법!

```jsx
/* 해당 댓글의 번호, 내용만 뽑아서 가져오게 했다.  */
$(".comment_new_action").click(function () {
  var _comment_re = $(this).parent().children(".comment_new_input").val();
  var _comment_num = $(this).parent().children(".comment_num_hidden").val();
});
```

<br>

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

<br><br>

## datepicker에서 원하는 날짜만 활성화하기

---

최초 jQuery가 기본으로 제공하는 datepicker 코드는, 아래와 같이 간단했다.

```jsx
<link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
<script src="https://code.jquery.com/jquery-1.12.4.js"></script>
<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>


<script>
$('#datepicker').datepicker();
</script>
```

하지만 포트폴리오 작업 중, 원하는 날짜만 활성화하는 것을 원했다. 아래와 같이 코드를 써주니 드디어 해결..!

```jsx

$(function() {
		var performDate = '${performDate.substring(0,10)}';		// jstl에 담긴 날짜정보.

		//선택가능 날짜
		var availableDates = [performDate];		// 여러 날짜가 들어갈 수 있으니, 배열의 형태. (일단 날짜 1개로 고정)
		function available(date) {
			var thismonth = date.getMonth()+1;
			var thisday = date.getDate();

			if(thismonth<10){
				thismonth = "0"+thismonth;
			}

			if(thisday<10){
				thisday = "0"+thisday;
			}
		    ymd = date.getFullYear() + "-" + thismonth + "-" + thisday;

		    if ($.inArray(ymd, availableDates) >= 0) {
		        return [true,"",""];
		    } else {
		        return [false,"",""];
		    }
		}

		$('#datepicker').datepicker({
			dateFormat: "yy-mm-dd",
			regional: "ko",
			beforeShowDay: available
		});

	});
</>
```

<br>
아래는 그냥 해당하는 html.

```html
<div id="datepicker"></div>
<!-- jQuery 오픈소스 사용. -->
```
