# sass

## 1. 变量

定义： $变量名： 参数

使用： 

```css
css{
	属性：$变量名
}

```



## 2. 嵌套



### 2.1 选择器嵌套

```scss
fu{
    zi{
        sun{
            
        }
    }
}
```

如果我们要获取父选择器，可以用&

```scss
fu{
    zi{
        a{
            
        }
        $：hover{
            这里就是zi
        }
    }
    $:hover{
        这个就是fu
        }
}
```



### 2.2 样式的嵌套



首先常规的属性例如：

```scss
body{
    font-family: ...;
    font-size:15px;
    font-weight: normal;
}
```

使用嵌套的写法：

```scss
body{
    font:{
        family: ....;
        size: 15px;
        weight: normal;
    }
}
```



## 3. 混合-mixin



### 3.1 基本使用

```scss
//使用如下

@mixin alert{
    color: '';
	background:...;
    a{
        color: red;
    }
}

.my-class{
    @include alert;
}

```

编译后的css如下

```csss
.my-class{
 	color: '';
	background:...;
}
.my-class a{
	color: red;
}
```



### 3.2 mixin的参数

```scss
@mixin alert($text-clor,$background){
    color: $text-clor;
	background-color:$background;
    
}

//传入参数
.my-class{
    @include alert(red,pink);
}

```



## 4. 继承

```scss
.a{
    padding:10;
}
.b{
    @extend .a;
    margin:10;
}

//编译完后的css
.a .b{
    padding: a0;
}
.b{
    margin:10
}
```

> 与a有关的也会继承下来，比如`.a .c{}` 继承之后  `.a .c .b{}`



## 5. @import

partials文件就是一个单独的小文件，通过导入来实现css模块化

**用_开头的文件就是partials** 这里的文件不会去编译

使用的时候直接导入

```scss
//定义文件_base.scss
body{
    margin:0;
    ...
}   


//导入的时候不需要加_ 
@import 'base'
    

```



## 6.函数

sass中可以对数字，字符串使用一些函数

### 6.1 数字

常用的有 abs(),round(),ceil()

### 6.2 字符串

	1. 定义一个字符串 $str : "hello str"
 	2. 转换为大写to-upper-case($str) 
 	3. 转换为小写to-lower-case($str)
 	4. 获取长度str-lenght($str)
 	5. 获取索引str-index()
 	6. 插入str-insert(字符串，内容，位置)

### 6.3 颜色

1. *颜色的表示方式可以用RGB（），RGBA()来表示

2. hsl（色相，饱和度，明度），hsla()同上

3. adjust-hue()调整色相

   ```scss
   color:adjust-hue($base-color,137deg)
   ```

   

4. lighten和darken 用来设置颜色得到明度和暗度

   1. lighten()变亮
   2. darken()变暗

   ```scss
   $base-color:red;
   $light-colr:lighten($base-color,30%);
   $darken-colr:darken($base-color,20%);
   ```

5. 饱和度函数

   1. saturate（）增加颜色的饱和度
   2. desaturate() 降低颜色的饱和度

6. 透明度函数

   1. 不透明度opacify($base,0.3)
   2. 透明度transparentize($base,0.3)



## 7. interpolation 插入变量

一般要在属性中插入变量的这样写 用#{}占位

例子：

```scss
$version:1.0.1;

$name: "info";
$str: "border";

.my-#{$name}{
    #{$str}-color:red
}
```



## 8. 控制指令

### @if

```scss
@if $isuse{
    //条件为真的话在执行
}@else if 条件{
    
}@else {
    
}


```



### @for

```scss
//语法
@for $var from <开始值> through <结束值> {
    。。。
}

//例子
@$lenght: 4;
@for $i from 1 through $lenght {
    .col-#{$i}{
        height:100%/$i
    }
}
```



### @each

```scss
$icons: success erro warning;

@each $icon in $icons {
    .icon-#{$icon}: {
        background-image：url(../#{$icon}.png)
    }
}
//遍历结果
```



### @while

```scss
@while 条件{
    /*
    *注意结束条件
    */
}
```

