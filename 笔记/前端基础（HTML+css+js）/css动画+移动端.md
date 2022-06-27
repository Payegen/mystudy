# 移动端学习

## Flex布局

在父元素当中设置display：flex，子元素就可以自动挤压和拉伸。

组成为以下四个部分：

- 弹性容器
- 弹性盒子
- 主轴
- 侧轴

此时开启flex的父元素子是弹性容器，元素就是弹性盒子，最后最重要的就是主轴和侧轴。

1. 主轴的对齐方式（justify-content）：
    |属性值|作用|
    |--|--|
    |flex-start|默认，从左到右|
    |flex-end|从终点开始|
    |center|沿主轴居中|
    |space-around|均匀分布在两侧|
    |space-between|均匀分布在相邻的盒子之间，先占两边，在平分|
    |space-evenly|都是相等的|

2. 侧轴的对齐方式（align-items）
    |属性值|作用|
    |--|--|
    |flex-start|默认值，上到下|
    |flex-end|从下到上|
    |center|沿侧轴居中|
    |strech|默认如果子盒子没有高度，自动拉伸，拉满|

    > 单独设置一个弹性盒子的对其方式使用 选出元素后添加`align-self:(侧轴的属性)`

3. 弹性伸缩比（flex）
    属性`flex: 整数值` 占用父盒子的剩余尺寸

4. 使用flex-direction改变元素方向

    |属性值|作用|
    |--|--|
    |row|**默认值**列，水平|
    |column|列，垂直|
    |row-reverse|行，从右到左|
    |column-reverse|列，从下到上|

5. 弹性盒子换行（flex-wrap）

   默认不换行，所以会发生将盒子挤压得情况，如果我们有多个盒子一行放不下需要的话可以开启换行
   `flex-wrap:wrap`

6. 调整行的对齐方式（`align-content`）和主轴差不多参考`justify-content`
   > 注意这个是多行的情况下，我们需要调整的属性

## css动画

### 平面转换形态2D

主要就是使用`transfrom`2D转换，位移，旋转，缩放。
> 在父盒子加个过渡属性先，`transtion: all 2s`

1. 位移**translate**
    - `transform: translate(水平，垂直)` 。取值可以为像素可以为百分比
    - 单方向移动translateX，translateY

2. 旋转**roate**
    - `transform:roate(度数)`
    - 旋转原点默认为盒子中心，改变原点使用`transform-origin：水平位置 垂直位置` 取值可以为方位名词（LEFT,RIGHT,TOP,BOTTOM,CENTER），像素，百分比。

3. 缩放**scale**
   1. 取值大于1放大，小于1缩小。（取值为一个值，为等比缩放）

4. 渐变
    使用background-image属性完成， 一般用于设置盒子的背景。
    1. `background-image: linear-gradient(blue,green,pink,...)`，用逗号隔开。
    2. 半透明渐变`background-image: linear-gradient(tansparent,rgba(0,0,0,0.6))`

### 空间转换

相比与2d转换，多一条z轴。正方向对着我们

1. 空间位移
    1. 用法
        - `transform:translat3d(x,y,z)`
        - `transform:translatX()`
        - `transform:translatY()`
        - `transform:translatZ()`

    2. 透视属性`perspective`进大远小，如果不开启的话，电脑在屏幕上没有效果。在父盒子开启`perspective: 800-1200`建议取值

2. 空间旋转
    1. 用法
        - `transform:rotateX(360deg)`
        - `transform:rotateY()`
        - `transform:rotateZ()`

    2. 单开启透视属性只能增加近大远小的的效果，要有3d效果还要开启`transfoem-style:preseve-3d`

3. 空间缩放
   1. 用法
        - `transform:scale3d(x,y,z)`
        - `transform:scaleX()`
        - `transform:scaleY()`
        - `transform:scaleZ()`

### 动画`animation`

1. 定义动画：

    ```css
        @keyframes 动画名{
            from{}
            to{}
        }
    ```

    ```css
        @keyframes 动画名{
            0%{}
            10%{}
            ...
            100%{}
        }
    ```

2. 使用动画：
    `animation: 动画名称 时间`

3. 动画属性：
    `animation`: 动画名称 时间 运动曲线 延时时间 重复次数 动画方向 执行完毕状态（空格隔开）
    - 动画名称
    - 时间
    - 运动曲线
        - linear
        - steps()步长
    - 延时时间
    - 重复次数
        - infinite
        - 次数
    - 动画方向
        - alternate为反方向
    - 执行完毕状态
        - 停留 forwards
        - 回到初始(默认) backwards

    > `animation-play-state：paused` 暂停动画 通常配合hover使用

4. 逐帧动画

    使用steps来完成逐帧动画

5. 组合动画

    ```css
    animation:
        动画1 ，
        动画2 ，
        动画3...
    ```

> 逗号隔开就行了里面的属性照样跟在动哈名字后面就行
