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
