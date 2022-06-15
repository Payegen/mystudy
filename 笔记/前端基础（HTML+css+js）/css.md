# css

## 基础选择器

1. 标签选择器
2. 类选择器
3. id选择器
   1. **id是唯一的不可以重复**
   2. **一个id选择器只能选中一个标签**
4. 通配符选择器（就是`* {}`）

```css

/*标签选择器*/
标签名 {}

/* 类选择器 */
.类名{}...

/*  id选择器*/
#id属性值{}
```

## 字体

### 字体样式

1. 字体大小：`font-size`
    >单位为像素

2. 字体粗细：`font-weihgt`
    - 关键字取值：
        - `normal` 正常
        - `bold` 加粗
    - 数字取值：100-900的**整百数**

3. 样式：`font-style`
    - 正常 `nomal`
    - 倾斜 `italic`

4. 类型：`font-family`

> 层叠问题：设置相同的样式，写在最后面的生效

### 文本样式

1. 文本缩进：`text-indent`
   1. 取值有两种，`px`,`em`
   2. **(1em=font-size)**

2. 对其方式：`text-align`
    - left
    - center
    - right

3. 文本修饰：text-decoration
   1. 取值
        |属性|效果|
        |--|--|
        |underline|下划线|
        |line-through|删除线|
        |overline|上划线|
        |none|正常|

### 行高：line-height
