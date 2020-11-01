# 软件需求工程Lab1实验报告

2020.11.1

## 小组成员

| 学号      | 姓名   | 成绩占比 |
| --------- | ------ | -------- |
| 171870559 | 季镇澜 | 20%      |
| 181860013 | 储备   | 20%      |
| 181860077 | 佘帅杰 | 20%      |
| 181860094 | 王佳奕 | 20%      |
| 181860151 | 周清远 | 20%      |



## 实验目的

获取Smart IDE的潜在需求，并对需求进行分类和分析。



## 实验方法、过程分析及结果展示

### 数据获取

我们先在Stack Overflow上通过“IDE”的标签进行搜索，找到了大量关于IDE的问答，这些回答可以作为Smart IDE的潜在需求，因此，我们通过爬虫抓取了这些问答（https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&tagged=ide&pagesize=100&site=stackoverflow&filter=!)5IW-1CBLPxKYw2x*xmfiaebgSti&key=602UeLTB17TQ0y7WP3t*)w((），爬虫抓取的部分数据展示如下，详细内容可在我们的仓库中查看（仓库地址：https://github.com/NJU-Software-Requirement/Software_Requirement_EXP1/blob/master/data/ide_ques.txt）：

<img src="C:\Users\wjy\AppData\Roaming\Typora\typora-user-images\image-20201101230441294.png" alt="image-20201101230441294" style="zoom:80%;" />

另外，很多文字没有很强的结构特征，对于这类的数据，我们需要一个分类器，对这样的数据判断其类型，进而提取Smart IDE的潜在需求。我们还爬取了10000条左右IDE相关的问答数据以此为按照9：1的比例划分训练集和测试机训练了一个分类器，分类器会根据问答的内容对没有打上标签的问答进行分类，将它们归类到某一标签。分类器的效果展示如下：

![img](https://raw.githubusercontent.com/NJU-Software-Requirement/Software_Requirement_EXP1/master/img/%E5%88%86%E7%B1%BB%E8%AE%AD%E7%BB%83%E7%BB%93%E6%9E%9C.png)

最后一轮训练结果准确率高达85.7%。



Stack Overflow只是我们本次实验中众多数据来源中的其中一个，这个开发者问答平台内容丰富，种类繁多。要想获取Smart IDE更多、更详尽的潜在需求，我们还需要综合考虑当前众多知名IDE项目各自的特性和缺陷。于是，我们还爬取了github上JetBrains Intellij IDEA的Pull Request(PR)约1400条内容（https://api.github.com/repos/JetBrains/intellij-community/pulls?state=all&per_page=100），以及Visual Studio Code的Issue约10000条（https://api.github.com/repos/microsoft/vscode/issues?state=all&per_page=100）和Pull Request约8000条（https://api.github.com/repos/microsoft/vscode/pulls?state=all&per_page=100），爬取的部分内容展示如下：

VScode中issue的title（仓库地址：https://github.com/NJU-Software-Requirement/Software_Requirement_EXP1/blob/master/data/vscode_issues_title.txt）：

<img src="C:\Users\wjy\AppData\Roaming\Typora\typora-user-images\image-20201101230529215.png" alt="image-20201101230529215" style="zoom:80%;" />





VScode中PR的title（仓库地址：https://github.com/NJU-Software-Requirement/Software_Requirement_EXP1/blob/master/data/vscode_pr_title.txt）：

<img src="C:\Users\wjy\AppData\Roaming\Typora\typora-user-images\image-20201101230559617.png" alt="image-20201101230559617" style="zoom:80%;" />





IDEA中PR的title（仓库地址：https://github.com/NJU-Software-Requirement/Software_Requirement_EXP1/blob/master/data/idea_pr_title.txt）：

<img src="C:\Users\wjy\AppData\Roaming\Typora\typora-user-images\image-20201101230623864.png" alt="image-20201101230623864" style="zoom:80%;" />



### 对获取数据的初步分析

首先，我们对从Stack Overflow上爬取的含有“IDE”标签的问答进行了各个tag的统计，并做了一个词云图，展示如下：

<img src="C:\Users\wjy\AppData\Roaming\Typora\typora-user-images\image-20201101231018309.png" alt="image-20201101231018309" style="zoom:80%;" />

可以看到，一些知名的开发工具（如Eclipse、Visual-studio、Pycharm、Visual-studio-code、Android-studio等）和一些编程语言（如Java、C、C++、C#、Python、PHP等）在Stack Overflow上伴随“IDE”问答出现的频率极高。

这是在我们预期之内的，一方面，各知名开发工具，即用户常用的IDE，有各自的特点和功能，另一方面，各常用编程语言由于各自的特性，各有自适配的开发环境和开发工具。虽然这些关键词不能给我们展示很直观的Smart IDE的需求，但是它给我们透露了以下信息：

1. Smart IDE需要能够配置各种编程语言的开发环境（包含针对专一语言的IDE的环境配置，如Intellij-IDEA，和针对多种语言的IDE的不同环境配置，如VScode）。
2. 出现频率越高的词显然越值得我们去关注，这即代表该相关语言或开发工具的使用者更多，也代表其存在可改进可完善的内容也更多，因此在后续需求的进一步获取和分类、分析时，我们可以围绕这些关键词方向进行内容的展开。

在筛选掉关于开发工具和编程语言的标签后，对剩下的词生成词云图如下：

<img src="C:\Users\wjy\AppData\Roaming\Typora\typora-user-images\image-20201101231044830.png" alt="image-20201101231044830" style="zoom:80%;" />

可以观察到，系统的名称成了高频词（像Linux、MacOS、Windows等），这直观反映了IDE需要对不同系统进行适配的需求。程序员会使用不同的计算机操作系统进行软件开发，因此Smart IDE需要对各种常用于软件开发的操作系统推出不同的版本，以满足各操作系统用户的使用需求。

另外，除去这些操作系统的名称后，剩下的词语几乎都能体现出IDE的一些具体需求了。引入眼帘的editor反映出IDE的文本编辑相关需求；debugging也是程序员常见的痛处，如果没有易于使用的调试工具、调试器，或许就不会有程序员使用这款(Stupid) IDE了；还有关于git的词语也是频频出现，版本控制已经是目前程序员开发项目工作中不可或缺的一角，Smart IDE确实应该有关于使用git这一分布式版本控制系统的需求。

实验中，我们还利用了wordToVec，对爬取的带有“IDE”标签的问答内容进行词汇向量化，训练了一个模型。根据上面的词云图，我们选出了一些可能有用的关键词，对文本聚类分析后，得到以下结果，部分展示如下。

<img src="https://github.com/NJU-Software-Requirement/Software_Requirement_EXP1/blob/master/img/ide_ques_vec_1.png?raw=true" alt="ide_ques_vec_1.png" style="zoom:80%;" />![ide_ques_vec_2.png](https://github.com/NJU-Software-Requirement/Software_Requirement_EXP1/blob/master/img/ide_ques_vec_2.png?raw=true)

<img src="https://github.com/NJU-Software-Requirement/Software_Requirement_EXP1/blob/master/img/ide_ques_vec_1.png?raw=true" alt="ide_ques_vec_1.png" style="zoom:80%;" />![ide_ques_vec_2.png](https://github.com/NJU-Software-Requirement/Software_Requirement_EXP1/blob/master/img/ide_ques_vec_2.png?raw=true)

词向量聚类结果可以在我们的仓库中查看，由于内容过多，暂不一一截图展示（仓库地址：https://github.com/NJU-Software-Requirement/Software_Requirement_EXP1/blob/master/data/ide_ques_vec.txt）

遗憾的是，结果中的相关词汇很大部分都不能体现出IDE的相关需求，但我们做了一部分筛选后，也能发现一些反映需求的词汇，比如：

在editor类的向量相关词语中，可以发现remote（IDE需要支持远程编辑）、slow/quick（IDE需要快速打开编辑器）、auto-save（IDE的编辑器需要有自动保存的功能）、copy/selected（IDE编辑器支持复制、粘贴、选中等基本文本编辑操作）等。

接着，我们把爬取的VScode的issue内容也做了类似的处理。

我们发现爬取的数据不是所有内容都带有label，所以我们将爬取的数据做了分类，对于没有label的issue，直接采用title生成了词云图，展示如下：
<img src="C:\Users\wjy\AppData\Roaming\Typora\typora-user-images\image-20201101231314095.png" alt="image-20201101231314095" style="zoom:80%;" />

对于带有label的issue，我们用label生成词云图，展示如下：
<img src="C:\Users\wjy\AppData\Roaming\Typora\typora-user-images\image-20201101231329533.png" alt="image-20201101231329533" style="zoom:80%;" />



从issue生成的第一个词云图中可以看出几个比较重要的关键词：File，Code，Terminal，Editor。这些都是有关软件功能的词汇，使用过vscode的同学应该都有体会，vscode的文件交互系统做的非常合理易用且功能强大。说明我们在开发一款新的IDE时，也应该充分考虑到文件的管理。而Code和Editor是最主要的文本编辑功能，这也是我们开发IDE软件的核心业务需求方向，在本项目之后的工作中，应该重点关注其他成功IDE有关需求和用户需求。最后对于Terminal，尽管现在多数IDE都是GUI，但是有些时候Terminal会比GUI更加有用，所以对于Terminal的功能设计分布也是本项目的一个侧重点。


第一张图是从IDE功能本身出发进行总结的，下面我们从用户需求角度出发进行讨论。从issue生成的第二个词云图中可以看出用户对于IDE的需求的一些关键词debug ,UX，verified也就是调试程序，程序员最需求的功能，UX也就是用户体验，当然这个词太过于宽泛，接下来的工作我们会进行更加细致的讨论。最后是verified，说明程序员对于安全性也有比较多的需求。

根据词云图的显示，我们选取了一些可能有用的关键词对爬取的issue内容进行词向量聚类分析，得到以下结果：

![vscode_issues_vec_1.png](https://github.com/NJU-Software-Requirement/Software_Requirement_EXP1/blob/master/img/vscode_issues_vec_1.png?raw=true)

（同上，聚类结果不便于展示，可在仓库中查看保存结果的文本文件：https://github.com/NJU-Software-Requirement/Software_Requirement_EXP1/blob/master/data/vscode_issues_vec.txt）从词向量的聚类结果中，我们观察得到的相关词汇，提取、分类了一些可能的需求，将在下文的结果中列举。

另外，我们把爬取的VScode的Pull Request和IDEA的Pull Request也做了类似的处理。展示如下

<img src="https://github.com/NJU-Software-Requirement/Software_Requirement_EXP1/blob/master/img/idea_pr.png?raw=true" alt="idea_pr.png" style="zoom:80%;" />

<img src="C:\Users\wjy\AppData\Roaming\Typora\typora-user-images\image-20201101231513335.png" alt="image-20201101231513335" style="zoom:80%;" />

对于以上两种主流的IDE的PR内容生成的词云图，可以发现大部分高频词都是关于修复、添加、更新等软件版本更新相关的动词，具体体现为在版本更新中“修复了xxxx的bug”、“添加了xxxx的功能”、“更新了xxxx的内容”等，非常遗憾的是，我们小组现在掌握的NLP技术和机器学习技术并不能很好地帮助我们从中获取出更详细的需求，因此我们也使用了人肉分类器从众多的PR内容中提炼了分类了一些Smart IDE的潜在需求，具体内容会在下面的结论中展示。



## 结论

最终，我们对所有的实验得到的材料进行更详细的分类和分析，形成以下需求。



### 文本编辑类

·支持文本编辑器的常用操作，包括选中、全选、复制、粘贴、撤销、重做。

·具备代码自动补全的功能。

·具备代码自动缩进的功能。

·具备文本内容查找的功能，在查找时，要给文本中出现的查询关键词刷上醒目的颜色。

·具备文本关键词替换的功能，此功能可基于查找功能实现，支持把查找到的关键词替换成新输入的关键词、支持批量替换、一键全部替换。

·支持语法高亮。

·可以同时开启多个窗口/多个文件进行编辑。

·多窗口同时打开同一个文件时进行文件内容的同步控制，具体做法可以有：

1. 禁止同一个文件同时被多窗口打开，如果同一个文件被多窗口二次打开，唤醒之前打开此文件的窗口；
2. 允许多窗口同时打开同一个文件，当文件内容被某一窗口更改时，其他窗口也自动同步更改内容；
3. 允许多窗口同时打开同一个文件，当文件内容被某一窗口更改并保存时，提醒用户当前有多个窗口已经打开此文件，让用户自己选择是否同步更改内容。

以上不同的控制可以由用户在Smart IDE的设置中自行设定。

·对于不同的编程语言，自动补全易错语法，如C++、Java的开发自动补全遗漏的分号，Python自动补全遗漏的冒号，条件语句自动补全判断相等的双等号等。

·支持编辑操作的自动保存，自动保存的频率由使用者自行设定。

·复制粘贴大段代码的时候要保持代码的缩进状态。

·鼠标指针停留在标识符上时，显示标识符的信息，如变量的类型，常量或宏的值（如果有的话），函数的参数列表及返回值。

· 对代码中明显的语法错误、待完善的函数或方法、未初始化的变量用特殊标记在文本中标出，如语法错误可以用红色波浪线在出错处下方标出，只声明、未定义的函数可以用绿色波浪在函数声明处标出。

· 检查英语单词的拼写，对出错词提供更正选择。

· 支持代码块的折叠。

### 调试类

· 支持常见的调试操作
1. 支持断点、条件断点等
2. 逐行运行
3. 调试中显示当前变量
4. 监视系统资源使用情况（如CPU）

· 提供独立的调试界面，包含以下内容
1. 调试器中当前文件的大纲
2. 函数、类列表
3. 控制台
4. 任务(task)
5. 调试输出
6. 变量视图，显示选定变量的运行时值。
7. 断点列表
8. 显示最新的运行时调用堆栈




### 用户界面类
· 用户界面主要包含以下多个视图
1. 文本编辑器（细节见上文）
2. 项目结构
    1. 包含该项目所有相关文件
    2. 能在该视图中对所列出文件进行基本的文件操作，如：复制、粘贴、剪切、重命名、删除、选定两个文件进行比较等 
    3. 提供对文件排列的多种排序方式
    4. 能够搜索文件
    5. 提供过滤筛选操作
4. 当前文档结构
    1. 展示类、函数、全局变量等元素
    2. 点击之后能够在文档编辑器中跳转到被选定元素所在位置
    3. 对元素进行排序
    4. 搜索
    5. 过滤筛选
    6. 收起和展开（适用于一个元素包含多个元素的情况，如一个类中含多个函数）
6. 错误和警告
    1. 显示错误和警告
    2. 定位：点击条目后能够跳转到位置
    3. 复制报错内容
    4. 跳转到浏览器查询错误号或错误描述
8. 相应程序语言文档浏览界面
    1. 显示当前程序语言对应的手册文档内容
    2. 搜索功能
    3. 点击文档中的链接能够跳转到其他条目或在浏览器中打开

· 支持个性化设置，用户可以对IDE的界面进行设置，选择自己喜爱的背景和风格；

· 支持用户自定义字体颜色、大小、样式，对代码的语法高亮也可以自定义颜色；

· 编辑器界面对文本的已保存内容和新增加内容用不同的颜色或字体背景色区分；

· 用户支持页面缩放；

· 支持多国语言。




### 编码支持类
· 设置每个项目的默认编码（用于从资源管理器视图中打开文件的编码方式）；

· 提供可用编码选项打开文件；

· 使用特定的编码或默认编码保存或重新打开当前文件；

· 显示当前文件编码方式；

· 当用户切换编码或者使用不正确的编码打开文件后给出警告。



### 插件类
· 支持加载官方或者是开发者开发的相应插件。

· 提供插件管理界面，能够选择删除、禁用。

· 自动检测插件版本，进行更新。



### 开发效率类

· 能够快速打开上次开发的（最近访问的）项目文件目录，定位到上次修改代码的光标处。

· 能够自动检测文件的编程语言，自动配置不同语言的编程环境。

· 支持多种便捷的快捷键、组合键，且可以由用户自定义设置。

· 能够关联git账户，便于用户进行版本控制，需要保证用户账户的安全。



### 可移植性

· 支持多语言环境下的文本分析。

· 具有各主流操作系统对应的使用版本，包括移动终端操作系统。