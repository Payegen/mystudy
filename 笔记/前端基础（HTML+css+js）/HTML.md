# HTML

## 简介

本文包括了基础html内容，以及HTML5新特性。由于HTML5以及被广泛应用到开发中，主流的浏览器以及被支持。因此有必要去学习一下

## HTM5新特性

- 新元素
- 新属性
- 完全支持 CSS3
- Video 和 Audio
- 2D/3D 制图
- 本地存储
- 本地 SQL 数据
- Web 应用

## 基本标签

1. h5音频标签：`<audio>`

   - src: 音频路径 {src:''}
   - controls： 显示播放的控件
   - autoplay: 自动播放
   - loop: 循环播放

2. h5视频标签：`<video>`
    >同上

3. 列表

    |标签名|说明|
    |--|--|
    |ul|无序列表|
    |ol|有序列表|

    > ol标签只能包含li标签

    |标签名|说明|
    |--|--|
    |dl|表示这个自定义列表，用来包裹dt/dd|
    |dt|表示自定义列表的主题|
    |dd|表示每个主题的内容|

4. 表格标签
   1. 基本使用

        |标签名|说明|
        |--|--|
        |table|表格整体，可以包裹多个tr|
        |tr|表格每行，有多个td|
        |td|每个单元格|

        ```html
        <!-- 例子 -->
        <table>
            <tr>
                <td>第一列</td>
                <td>第二列</td>
            </tr>
            <tr>
                <td>1</td>
                <td>2</td>
            </tr>
            <tr>
                <td>3</td>
                <td>4</td>
            </tr>
        </table>
        <!-- 实际中使用css修改样式，这里不展开 -->
        ```

   2. 合并单元格
        |属性名|说明|
        |--|--|
        |rowspan|跨行合并，讲多行的单元格**垂直**合并|
        |colspan|跨列合并，讲多列的单元格**水平**合并|

        > 直接在单元格加属性名，值为要合并多少个单元格例如`<td rowspan="2">`

5. 表单标签
    1. `input`
        通过`type属性`展示不同的效果，常用的属性如下：
        - `text` 文本输入框
        - `password` 密码框
        - `radio` 单选框，多选一
            >可以设置相同的`name`属性来分为一组，`checked`为默认选中
        - `checkbox` 多选框
        - `file` 上传文件
            >如果需要上传多个文件需要添加`multiple`属性
        - `submit` 提交按钮
        - `rest` 重置按钮
        >提示属性`placeholder`

    2. `button`

    3. `select`
        标签组成：
        - select： 下拉菜单的整体
        - option： 每个选项

        ```html
        <select>
            <option>选项1</option>
            <option>选项2</option>
            <option selected>选项3</option>
        </select>
        <!-- seleced 默认选中 -->
        ```

    4. `textarea`

    5. `label`
        用法如下所示

        ```html
        <!-- 第一种用法 -->
        <label for="id1">
            <span>男</span>
        </label>
        <input type='radio' id="id1" name="sex">

        <!-- 第二种 直接包裹 去掉for属性-->
        <label>
            <span>女</span>
            <input type='radio' name="sex">
        </label>
        ```

6. 语义化标签
   1. `div` 块标签 独占一行
   2. `span` 一行显示多个的标签

## HTML5内容

### 内联SVG与Canvas

**简介:** 什么是SVG?

- SVG 指可伸缩矢量图形 (Scalable Vector Graphics)
- SVG 用于定义用于网络的基于矢量的图形
- SVG 使用 XML 格式定义图形
- SVG 图像在放大或改变尺寸的情况下其图形质量不会有损失
- SVG 是万维网联盟的标准
- SVG 与 DOM 和 XSL 之类的 W3C 标准是一个整体

**用法:**

>详情见单独文档

### 拖放（Drag 和 Drop）

### `input`新内容

  1. `datalist`标签
     在输入框添加输入的选项具体用法如下

     ```html
     <input list="browsers">

        <datalist id="browsers">
        <option value="Internet Explorer">
        <option value="Firefox">
        <option value="Chrome">
        <option value="Opera">
        <option value="Safari">
        </datalist>
     ```

  2. `keygen`标签,用户验证.暂时没用到过

### web存储

客户端存储数据的两个对象为：

- `localStorage` - 没有时间限制的数据存储
- `sessionStorage` - 针对一个 session 的数据存储

不管是 localStorage，还是 sessionStorage，可使用的API都相同，常用的有如下几个（以localStorage为例）：

- 保存数据：`localStorage.setItem(key,value);`
- 读取数据：`localStorage.getItem(key);`
- 删除单个数据：`localStorage.removeItem(key);`
- 删除所有数据：`localStorage.clear();`
- 得到某个索引的`key`：`localStorage.key(index);`

### Web Workers

什么是 Web Worker？
当在 HTML 页面中执行脚本时，页面的状态是不可响应的，直到脚本已完成。

web worker 是运行在后台的 JavaScript，独立于其他脚本，不会影响页面的性能。您可以继续做任何愿意做的事情：点击、选取内容等等，而此时 web worker 在后台运行

>使用前检查下浏览器是否指支持

```js
 if(typeof(Worker)!=="undefined")
   {
   // 是的! Web worker 支持!
   // 一些代码.....
   }
 else
   {
   // //抱歉! Web Worker 不支持
   } 
```
