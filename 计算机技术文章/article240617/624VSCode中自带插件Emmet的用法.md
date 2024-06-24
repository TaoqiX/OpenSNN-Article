# VSCode中自带插件Emmet的用法

Emmet 是一个强大的工具，集成在 Visual Studio Code (VSCode) 中，可以大大提高编写 HTML 和 CSS 的效率。以下是如何使用 Emmet 插件的一些基本方法：

## 使用Emmet编写html代码
- 输入 `!` 然后按 `Tab` 或 `Enter` 键，可以生成一个基本的 HTML 模板：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```
### 分类一
- 输入 `h1#xxx`,可以生成一个h1的标签，并且id属性为xxx
```html
<h1 id="xxx"></h1>
<!-- 直接输入`#abcd` -->
<div id="abcd"></div>
```
- 输入 `h1.xxx`,可以生成一个h1的标签，并且class属性为xxx
```html
<h1 class="xxx"></h1>
<!-- 直接输入`.abcd` -->
<div class="abcd"></div>
```
- 输入 `h1[aaa=bbb]`,可以生成一个h1的标签，添加aaa属性为bbb
```html
<h1 aaa="bbb"></h1>
```
- 输入 `h1{xxx}`,可以生成一个h1的标签，标签包含的内容是xxx
```html
<h1>xxx</h1>
```
- 综合例子，输入 `h1#aaa.b.ab[ccc=ddd eee=fff]{ggg}`,生成内容如下
```html
<h1 id="aaa" class="b ab" ccc="ddd" eee="fff">ggg</h1>
```
- 使用`:`和使用缩写
```html
<!-- 输入`input:password` -->
<input type="password" name="" id="">
<!-- 输入`a:mail` -->
<a href="mailto:"></a>
<!-- 输入`btn` -->
<button></button>
<!-- 输入`btn:s` -->
<button type="submit"></button>
```

### 分类二
- 输入 `h1>h2>h3`,生成内容如下
```html
<h1>
    <h2>
        <h3></h3>
    </h2>
</h1>
```
- 输入 `h1+h2+h3`,生成内容如下
```html
<h1></h1>
<h2></h2>
<h3></h3>
```
- 输入 `h1>h2^h3`,生成内容如下
```html
<h1>
    <h2></h2>
</h1>
<h3></h3>
```
- 综合例子，输入 `h1>h2>h3+h4>p>a^h5+div^^h6+span`,生成内容如下
```html
<h1>
    <h2>
        <h3></h3>
        <h4>
            <p><a href=""></a></p>
            <h5></h5>
            <div></div>
        </h4>
    </h2>
    <h6></h6>
    <span></span>
</h1>
```
- 总结：
```txt
使用`>`符号：表示生成子元素
使用`+`符号：表示生成同级元素
使用`^`符号：表示生成父级元素的同级元素
```
### 分类三（其他）
- `()`分组操作符
```html
<!-- 输入`h1>(h2>h3)>h4` -->
<h1>
    <h2>
        <h3></h3>
    </h2>
    <h4></h4>
</h1>
```
- `*`乘法
```html
<!-- 输入`ul>li*5` -->
<ul>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
</ul>
```
- `$`自动计数
```html
<!-- 输入`ul>li.item${test$$}*5` -->
<ul>
    <li class="item1">test01</li>
    <li class="item2">test02</li>
    <li class="item3">test03</li>
    <li class="item4">test04</li>
    <li class="item5">test05</li>
</ul>
```

### 分类四（奇奇怪怪）
- `tbody>tr>(td.item$$@-)lorem5*5`
- `tbody>tr>(td.item$$@->lorem5)*5` 和 `tbody>tr>((td.item$$@-)>lorem5)*5` 和 `((td.item$$@-)>lorem5*3)*5`
- 直接`giao`不会出现提示，可以在后边加一个`*1`或者`+xxx`,就会出现提示
- `()`的使用，如果以`)`结尾则不会出现提示，可以在后边加一个`*1`或者`+xxx`,就会出现提示
- `()`的用法，`(h1)h2`无效，`h5>(h1)h2`有效且等价于`h5>h1+h2`,奇怪的用法一般转换成`+`号。
- `lorem`的用法，`ul>lorem`和`ul>lorem*1`效果不相同。后者自动为lorem补上了标签。含`*`。
- `lorem`的用法，`lorem5*3`和`ul>lorem5*3`效果不相同。后者自动为lorem补上了标签。含`>`。
- **总结**：巧用`*`号,巧用`()`号,lorem自动补标签,奇怪的用法一般转换成`+`号。



## 使用Emmet编写css代码
Emmet 官方文档：https://docs.emmet.io/



######

-----

【转载自:】**开思通智网** ---- “一起来o站，玩转AGI！”  
【官网:】[https://www.opensnn.com/](https://www.opensnn.com/)  
【原文链接:】[https://www.opensnn.com/os/article/10000897](https://www.opensnn.com/os/article/10000897)

##### 结束





