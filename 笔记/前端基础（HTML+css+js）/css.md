# css

## 基础选择器

1. 标签选择器
2. 类选择器
3. id选择器
   1. **id是唯一的不可以重复**
   2. **一个id选择器只能选中一个标签**
4. 通配符选择器（就是`* {}`）

## 选择器进阶

### 补充选择器

1. 后代选择器
    `选择器1 选择器2 ...{css}` 选择器中间用空格隔开,表示2，3，4都是选择器1的后代

2. 子选择器
   `选择器1>选择器2 {}` 只选择下一层子选择器

3. 并集选择器
    `选择器1,选择器2,...{css}` 用,隔开

4. 交集选择器
   同时满足两个条件的选择器

   ```css
   <p class="jiaoji">  标签

   <style>
   <!-- 这里不要空格，直接挨着写 -->
    p.jiaoji{
        css       
    }
   </style>
   ```

5. 伪类选择器
   格式如下：`p:hover`

---

### 结构伪类选择器

根据元素再HTML的关系来查找元素

|选择器|说明|
|--|--|
|E:first-child{}|匹配父元素的第一个元素，并且是E元素|
|E:last-child{}|匹配父元素的最后一个元素，并且是E元素|
|E:nth-child(n){}|匹配父元素的第n个元素，并且是E元素|
|E:nth-last-child(n){}|匹配父元素的倒数第n个元素，并且是E元素|

> (n)是传的参数,可以是0，1，2，3....也可以是公式

公式如下：

- 偶数：`2n`,`even`
- 奇数：`2n+1`,`odd`
- 找到前五个：`-n+5`
- 找到倒数五个：`n+5`

> 直接参考格式填公式，n不用边，查找多少个数字对应填多少个就行了

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

## 背景 background

属性如下：

- `background-color` 取值直接指定为颜色（格式可以为颜色名，或者#fff，或者三原色rgb,rgba）
- `background-image` 取值为url()
- `background-repeat` 背景的平铺方式
  - repeat 水平和垂直方向都平铺
  - no-repeat 不平铺
  - repeat-x 沿x轴平铺
  - repeat-y  ...y...
- `background-position` (背景的定位): x , y
  - 水平方向 left，right，top,center。垂直方向：top,center,bottom
  - 数字+px :以原点（0，0）开始
- `background-size`:
  - 数字+px
  - 百分比： 相当于盒子自身宽高的百分比
  - contain：等比缩放，直到不超出盒子的最大值
  - cover：将图片等比缩放，直到刚好填满盒子

> 背景与img标签的差别：img是个dom元素，不设置宽高就按图片的大小来显示。背景是来装饰盒子模型的

## 元素的显示模式

1. 块元素 （独占一行）：div,p,h...
2. 行内元素（一行可以显示多个）：a,span,b,li...
3. 行内块元素（一行可以显示多个，可以设置宽高）：input,textarea,button,img...

> `display` 可以改变显示模式

## 选择器优先级

不同的选择器有不同的优先级，优先级高的会覆盖优先级低的

1. **优先级公式**
   `！important` > `行内样式` > `id` > `class` > `标签` > `通配符` > `继承`

2. 权重叠加计算
   一级（行内样式） 二级（id选择器） 三级（class选择器） 四级（标签选择器）
   优先比较级别，相同级别再比较个数，级别大于个数！
   > !important最高，加了就是第一

## 盒模型

组成由 margin，padding，border，content。盒子的大小也是由这些东西组合控制的

> css3中盒子模型的计算可以用 `box-size：boeder-box`指定大小，内容会再盒子中自动减去，避免手动计算。（不会被内容撑大）。

## 浮动

### 伪元素

- 元素：HTML元素
- 为元素：css模拟出来的标签效果

为元素就两个，`E::before`,`E::after`。必须设置content才能显示，可以为空，但不能没有。默认为行内元素

### 浮动的特性

直接开启属性`float: left/right`就完事了。
> 早期开启浮动后用来解决文字环绕图片

1. 开启浮动后的元素会脱离标准流，相当于飘在了空中
2. 后面开启浮动的元素会再前一个浮动的盒子左右
3. 开启浮动的盒子具有行内块的特点

>浮动的元素不能设置`margin：0 auto`

### 清除浮动

如果子元素浮动了，此时父元素因为子元素脱标不能撑开父元素，所以需要清楚浮动带来的影响

1. 额外标签法
   在父元素内容最后添加一个块元素，设置clear：both
2. 单伪元素法

   ```css
    .clearfix::after{
        content:'';
        display:block;
        clear:both;
    }
   ```

3. 双伪元素（推荐）

    ```css
    .clearfix::before,
    .clearfix::after{
        content:'';
        display:table;
    }
    .clearfix::after{
        clear:both;
    }
   ```

    > before解决外边距塌陷问题

4. 溢出隐藏
    `overflow:hidden`

## 定位（position）

### 静态定位（static）

### 相对定位（relative）

相对于自己的位置进行定位

### 绝对定位（absulate）

先找开启定位了的父级，如果有则一次为参照。没有就以浏览器窗口为参考。

### 固定定位(fixed)

相对于浏览器固定不动，脱标不占位置。

### 层级问题

不同布局方式的层级关系不同，标准流<浮动<定位
默认定位情况下，后来的盒子会覆盖前面的盒子。
可以用z-index来调整层级，越大越上

## 补充

- `透明属性(opacity)` 取值再0~1之间 越接近0越透明

- `精灵图`：讲多张小图片合拼成一个大图片，通过`background-position ：x,y`来展示

- `鼠标样式(cursor)`:
  - dedfault
  - pointer 小手的效果
  - text 工字型
  - move 十字型

- 垂直对齐
    1. **基线**：浏览器文字类型元素再排版中用于对齐。
    2. vertical-align:属性
    |属性|效果|
    |--|--|
    |baseline|默认，基线对齐|
    |top|顶部|
    |middle|中部|
    |bottom|底部|
    3. 浏览器遇到行内块和行内标签当作文字处理，默认是按照基线对象

- overflow 溢出部分
    1. visible 溢出可见
    2. hidden 隐藏
    3. scroll 无论是否溢出都显示滚动条
    4. auto 自动显示或者隐藏

- 隐藏元素
    1. visibility：hidden
    2. display：none

- 过渡属性`transition`：在元素上添加后填上 `属性+时间`,如果属性过多可以用all。然后悬停的时候可以添加需要变化的属性。
