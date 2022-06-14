# springMVC

## RequestMapping注解

### 1.value属性

```java
@RequestMapping(value="toUser")
@RequestMapping("toUser")
```

> value 属性是 @RequestMapping 注解的默认属性，因此如果只有 value 属性时，可以省略该属性名，如果有其它属性，则必须写上 value 属性名称

### 2.path属性

path 属性和 value 属性都用来作为映射使用。即 `@RequestMapping(value="toUser")`和` @RequestMapping(path="toUser") `都能访问 toUser() 方法。

path 属性支持通配符匹配，如` @RequestMapping(path="toUser/*") `表示`http://localhost:8080/toUser/1` 或 `http://localhost:8080/toUser/hahaha` 都能够正常访问

### 3.name属性

name属性相当于方法的注释，使方法更易理解。如 `@RequestMapping(value = "toUser",name = "获取用户信息")`

### 4.method属性*

method 属性用于表示该方法支持哪些 HTTP 请求。如果省略 method 属性，则说明该方法支持全部的 HTTP 请求。

`@RequestMapping(value = "toUser",method = RequestMethod.GET)` 表示该方法只支持 GET 请求。也可指定多个 HTTP 请求，如`@RequestMapping(value = "toUser",method = {RequestMethod.GET,RequestMethod.POST})`，说明该方法同时支持 GET 和 POST 请求。

### 5.params属性*

params 属性用于指定请求中规定的参数

```java
@RequestMapping(value = "toUser",params = "type")
public String toUser() {
    
    return "showUser";
}
```

> 以上代码表示请求中必须包含 type 参数时才能执行该请求。即 `http://localhost:8080/toUser?type=xxx` 能够正常访问 toUser() 方法，而 `http://localhost:8080/toUser` 则不能正常访问 toUser() 方法。

```java
@RequestMapping(value = "toUser",params = "type=1")
public String toUser() {
    
    return "showUser";
}
```

> 上代码表示请求中必须包含 type 参数，且 type 参数为 1 时才能够执行该请求 即`/toUser?ytpe=1`才能请求

 ## 通过请求URL进行映射

### 1.方法级别注解

```java
@Controller
public class IndexController {
    @RequestMapping(value = "/index/login")
    public String login() {
        return "login";
    }
    @RequestMapping(value = "/index/register")
    public String register() {
        return "register";
    }
}
```

### 2.类级别注解(推荐，结构清晰)

```java
@Controller
@RequestMapping("/index")
public class IndexController {
    @RequestMapping("/login")
    public String login() {
        return "login";
    }
    @RequestMapping("/register")
    public String register() {
        return "register";
    }
}
```

## 通过请求参数、请求方法进行映射

```java
@RequestMapping(value = "/index/success" method=RequestMethod.GET, Params="username")
    public String success(@RequestParam String username) {
        
        return "index";
}
```

## 传递参数

### 1.通过实体Bean接收请求参数

> 实体 Bean 接收请求参数适用于 get 和 post 提交请求方式。需要注意，Bean 的属性名称必须与请求参数名称相同

```java
@RequestMapping("/login")
public String login(User user, Model model) {
    if ("bianchengbang".equals(user.getName())
            && "123456".equals(user.getPwd())) {
       
        model.addAttribute("message", "登录成功");
        return "main"; // 登录成功，跳转到 main.jsp
    } else {
        model.addAttribute("message", "用户名或密码错误");
        return "login";
    }
}
```

### 2.通过处理方法的形参接收请求参数

```java
@RequestMapping("/login")
public String login(String name, String pwd, Model model) {
    if ("bianchengbang".equals(user.getName())
            && "123456".equals(user.getPwd())) {
       
        model.addAttribute("message", "登录成功");
        return "main"; // 登录成功，跳转到 main.jsp
    } else {
        model.addAttribute("message", "用户名或密码错误");
        return "login";
    }
}
```

通过处理方法的形参接收请求参数就是直接把表单参数写在控制器类相应方法的形参中，即形参名称与请求参数名称完全相同。该接收参数方式适用于 get 和 post 提交请求方式。

### 3.通过HttpServletRequest接收请求参数

```java
public String login(HttpServletRequest request, Model model) {
    String name = request.getParameter("name");
    String pwd = request.getParameter("pwd")
}
```

把request传进去，参考servlet。。。

### 4.通过@PathVariable接收URL中的请求参数

```java
@RequestMapping("/login/{name}/{pwd}")
public String login(@PathVariable String name, @PathVariable String pwd, Model model){

}
```

在访问`“login/bianchengbang/123456”`路径时，上述代码会自动将 URL 中的模板变量`{name}` 和 `{pwd}` 绑定到通过 `@PathVariable` 注解的同名参数上，即 `name=bianchengbang、pwd=123456`

### 5.通过@RequestParam接收请求参数

```java
@RequestMapping("/login")
public String login(@RequestParam String name, @RequestParam String pwd, Model model) {
}
```

该方式与`2.通过处理方法的形参接收请求参数`部分的区别如下：当请求参数与接收参数名不一致时，`2.通过处理方法的形参接收请求参数`不会报 404 错误，而“通过 `@RequestParam` 接收请求参数”会报 404 错误。

## 自定义类型转换器

Spring MVC 框架的 Converter<S，T> 是一个可以将一种数据类型转换成另一种数据类型的接口，这里 S 表示源类型，T 表示目标类型。开发者在实际应用中使用框架内置的类型转换器基本上就够了，但有时需要编写具有特定功能的类型转换器。

## JSON 数据转换

在使用注解开发时需要用到两个重要的 JSON 格式转换注解，分别是@RequestBody 和 @ResponseBody。

- @RequestBody：用于将请求体中的数据绑定到方法的形参中，该注解应用在方法的形参上。
- @ResponseBody：用于直接返回 return 对象，该注解应用在方法上。

需要注意的是，在该处理方法上，除了通过 @RequestMapping 指定请求的 URL，还有一个 @ResponseBody 注解。该注解的作用是将标注该注解的处理方法的返回结果直接写入 HTTP Response Body（Response 对象的 body 数据区）中。一般情况下，@ResponseBody 都会在异步获取数据时使用，被其标注的处理方法返回的数据都将输出到响应流中，客户端获取并显示数据。

## 拦截器的定义

在 Spring MVC 框架中定义一个拦截器需要对拦截器进行定义和配置，主要有以下 2 种方式。

1. 通过实现 `HandlerInterceptor` 接口或继承 `HandlerInterceptor` 接口的实现类（例如 HandlerInterceptorAdapter）来定义；

2. 通过实现 `WebRequestInterceptor` 接口或继承 `WebRequestInterceptor` 接口的实现类来定义。

### **在springboot中注册**

创建一个实现了 WebMvcConfigurer 接口的配置类（使用了 @Configuration 注解的类），重写 addInterceptors() 方法，并在该方法中调用 registry.addInterceptor() 方法将自定义的拦截器注册到容器中。

```java
@Configuration
public class MyConfig implements WebMvcConfigurer {
    ......
    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        log.info("注册拦截器");
        registry.addInterceptor(new LoginInterceptor()).addPathPatterns("/**") //拦截所有请求，包括静态资源文件
                .excludePathPatterns("/", "/login", "/index.html", "/user/login", "/css/**", "/images/**", "/js/**", "/fonts/**"); //放行登录页，登陆操作，静态资源
    }
}
```

在指定拦截器拦截规则时，调用了两个方法，这两个方法的说明如下：

- `addPathPatterns`：该方法用于指定拦截路径，例如拦截路径为“/**”，表示拦截所有请求，包括对静态资源的请求。
- `excludePathPatterns`：该方法用于排除拦截路径，即指定不需要被拦截器拦截的请求。