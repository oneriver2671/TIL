## 파일 업로드 기능

- 먼저, pom.xml에 라이브러리를 추가한다.

  ```xml
  <dependency>
  	<groupId>commons-fileupload</groupId>
  	<artifactId>commons-fileupload</artifactId>
  	<version>1.3.3</version>
  </dependency>
  ```

- 이후 servlet-context.xml 설정

  ```xml
  <!--// 파일 업로드를 위해 추가 -->
  	<!-- 반드시 id를 'multipartResolver'로 지정해줘야함.  -->
  	<beans:bean id="multipartResolver" class="org.springframework.web.multipart.commons.CommonsMultipartResolver">
  		<beans:property name="defaultEncoding" value="utf-8"></beans:property>
  		<!-- 1024 * 1024 * 10 bytes  10MB -->
  		<beans:property name="maxUploadSize" value="104857560"></beans:property>		<!-- 한 번의 Reqeust로 전달될 수 있는 최대의 크기 -->
  		<!-- 1024 * 1024 * 2 bytes  2MB -->
  		<beans:property name="maxUploadSizePerFile" value="2097152"></beans:property>	<!-- 하나의 파일 최대 크기 -->
  		<beans:property name="uploadTempDir" value="file:/C:/SpringUpload/upload/tmp"></beans:property>		<!-- 아래 사이즈 이상의 데이터는 임시 파일 형태로 이곳에 보관됨. -->
  		<beans:property name="maxInMemorySize" value="10485756"></beans:property>		<!-- 메모리상에서 유지하는 최대의 크기 -->
  	</beans:bean>
  <!-- 파일 업로드 // -->
  ```

- Controller

  ```java
  @GetMapping("/exUpload")
  	public void exUpload() {	// 리턴타입이 void면 URL 경로 그대로 jsp 파일 이름으로 사용됨.
  		log.info("/exUpload......");
  	}

  @PostMapping("/exUploadPost")
  	public void exUploadPost(ArrayList<MultipartFile> files) {	// 어노테이션 없이 그냥 들어와지던가? 왜?? (form태그에서 넘어옴)

  		files.forEach(file ->{
  			log.info("---------------------");
  			log.info("name:" + file.getOriginalFilename());
  			log.info("size:" + file.getSize());
  		});
  ```

- View

  ```html
  <form
    action="/sample/exUploadPost"
    method="POST"
    enctype="multipart/form-data"
  >
    <div>
      <input type="file" name="files" />
    </div>
    <div>
      <input type="file" name="files" />
    </div>
    <div>
      <input type="file" name="files" />
    </div>
    <div>
      <input type="file" name="files" />
    </div>
    <div>
      <input type="submit" />
    </div>
  </form>
  ```
