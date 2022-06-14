# 基于JWT实现token的登录验证

## 1.导入依赖

```xml
<dependency>
    <groupId>com.auth0</groupId>
    <artifactId>java-jwt</artifactId>
    <version>3.10.3</version>
</dependency>
```

## 2.JWT的生成与解析方法

### 2.1生成JWT的token

```java
public class JWTTest {
    @Test
    public void testGenerateToken(){
        // 指定token过期时间为10秒
        Calendar calendar = Calendar.getInstance();
        calendar.add(Calendar.SECOND, 10);

        String token = JWT.create()
                .withHeader(new HashMap<>())  // Header
                .withClaim("userId", 21)  // Payload
                .withClaim("userName", "baobao")
                .withExpiresAt(calendar.getTime())  // 过期时间
                .sign(Algorithm.HMAC256("!34ADAS"));  // 签名用的secret

        System.out.println(token);
    }
}
```

> 注意**多次运行方法生成的token字符串内容是不一样的**，尽管我们的payload信息没有变动。因为**JWT中携带了超时时间**，所以每次生成的token会不一样，我们利用base64解密工具可以发现payload确实携带了超时时间

### 2.2解析JWT字符串

```java
@Test
public void testResolveToken(){
    // 创建解析对象，使用的算法和secret要与创建token时保持一致
    JWTVerifier jwtVerifier = JWT.require(Algorithm.HMAC256("!34ADAS")).build();
    // 解析指定的token
    DecodedJWT decodedJWT = jwtVerifier.verify("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyTmFtZSI6ImJhb2JhbyIsImV4cCI6MTU5OTkyMjUyOCwidXNlcklkIjoyMX0.YhA3kh9KZOAb7om1C7o3vBhYp0f61mhQWWOoCrrhqvo");
    // 获取解析后的token中的payload信息
    Claim userId = decodedJWT.getClaim("userId");
    Claim userName = decodedJWT.getClaim("userName");
    System.out.println(userId.asInt());
    System.out.println(userName.asString());
    // 输出超时时间
    System.out.println(decodedJWT.getExpiresAt());
}
```

## 简单封装一个token的工具类

```
public class TakenUtil {
		//传入我们的实体类
        public static String getToken(User user){
            // 指定token过期时间为10秒
            Calendar calendar = Calendar.getInstance();
            calendar.add(Calendar.SECOND, 60);
			//用用户信息生成token
            String token = JWT.create()
                    .withHeader(new HashMap<>())  // Header
                    .withClaim("userId", user.getId())  // Payload
                    .withClaim("userName", user.getName())
                    .withExpiresAt(calendar.getTime())  // 过期时间
                    .sign(Algorithm.HMAC256("!34ADAS"));  // 签名用的secret

            System.out.println(token);
            return token;
        }

        public static DecodedJWT resolveToken(String token){
            // 创建解析对象，使用的算法和secret要与创建token时保持一致
            JWTVerifier jwtVerifier = JWT.require(Algorithm.HMAC256("!34ADAS")).build();
            // 解析指定的token
            DecodedJWT decodedJWT = jwtVerifier.verify(token);
            return decodedJWT;
        }

}
```

## 3.编写测试方法测试一下

### 3.1编写一个service从数据库查询一个对象出来

```java
public class UserServiceImp implements UserService{
    @Autowired
    UserMapper userMapper;
    @Override
    public User getUserByid() {
        User user = userMapper.selectById(3);//这里我们直接获取
        return user;
    }
}
```

### 3.2编写测试类

```java
 @Test
    void getTokenTest(){
        User user = userService.getUserByid();
        String token = TakenUtil.getToken(user);
        System.out.println(token+"\n");
        TakenUtil.resolveToken(token);
    }
```

![image-20220407000853544](C:\Users\Yushuai\AppData\Roaming\Typora\typora-user-images\image-20220407000853544.png)

![image-20220407000904423](C:\Users\Yushuai\AppData\Roaming\Typora\typora-user-images\image-20220407000904423.png)

这里我们分别打印出我们的结果，分别是token，和解析结果。

解析结果就是我们查询到的对象的id和name,最后一条是过期的时间。