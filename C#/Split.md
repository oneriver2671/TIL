
- '010-1111-2222' → '010', '1111', '2222' 으로 쪼개길 원함
- `Split()` 활용

```c#
 string customerMobile = SiteCookie.CustomerMobile;
 string customerEmail = SiteCookie.CustomerMail;

 CreateViewModel model = new CreateViewModel()
 {
     FrontPhoneNumber = customerMobile.Split('-')[0],
     MiddlePhoneNumber = customerMobile.Split('-')[1],
     BackPhoneNumber = customerMobile.Split('-')[2]
 };
```