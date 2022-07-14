# git基本使用

## 1.创建命令

- 初始化仓库

```git
git init
```

- 添加文件到仓库

```git
git add
```

- 提交代码到仓库

```git
git commit -m 'add a new file ... / some new change ' 
```

## 2.版本管理

`git status`命令可以让我们时刻掌握仓库当前的状态

但如果能看看具体修改了什么内容使用`git diff`

`git log` 查看我们提交信息

### 2.1版本回退

> 回退到上一个版本

```git
git reset --hard HEAD^
```

> 当我们回退一个版本后，后悔了再重新回退怎么办？

```git
git rest --hard 1092a
```

我们可以用提交log 中 commit 版本号进行回退
> 版本号不需要全部输入

### 2.2工作区和暂存区

- 工作区（Working Directory）

> 就是你电脑能看到的目录

- 版本库（Repository）

> 工作区有一个隐藏目录.git，这个不算工作区，而是Git的版本库。
> Git的版本库里存了很多东西，其中最重要的就是称为stage（或者叫index）的暂存区，还有Git为我们自动创建的第一个分支master，以及指向master的一个指针叫HEAD。

### 2.3撤销修改

#### 2.3.1 修改内容还未提交

```git
git checkout -- readme.txt
```

命令`git checkout -- readme.txt`意思就是，把readme.txt文件在工作区的修改全部撤销，这里有两种情况：

一种是readme.txt自修改后还没有被放到暂存区，现在，撤销修改就回到和版本库一模一样的状态；

一种是readme.txt已经添加到暂存区后，又作了修改，现在，撤销修改就回到添加到暂存区后的状态。

总之，就是让这个文件回到最近一次`git commit`或`git add`时的状态

#### 2.3.2 add提交到暂存区了，未提交

用命令`git reset HEAD <file>`可以把暂存区的修改撤销掉（unstage），重新放回工作区

```git
git reset HEAD readme.txt
```

`git reset`命令既可以回退版本，也可以把暂存区的修改回退到工作区。当我们用HEAD时，表示最新的版本。

#### 2.3.3删除文件

另一种情况是删错了，因为版本库里还有呢，所以可以很轻松地把误删的文件恢复到最新版本：

```git
git checkout -- test.txt
```

`git checkout`其实是用版本库里的版本替换工作区的版本，无论工作区是修改还是删除，都可以“一键还原

> 注意：从来没有被添加到版本库就被删除的文件，是无法恢复的！

## 3.分支管理

### 3.1 创建切换分支

```git
git checkout -b dev
```

`checkout` 命令加参数`-b`表示创建并切换分支
> 等同于如下两条

```git
git branch dev  //创建
git checkout dev //切换
```

使用`git branch`查看当前分支

### 3.2 合并分支

在分支完成提交后`git add ..`
切换回主分支`git checkout mater`

```git
git merge dev //合并分支
```

`git merge`命令用于合并指定分支到当前分支。合并后，再查看就可以看到，和dev分支的最新提交是完全一样的。

删除分支：`git branch -d <name>`

## 4.分支冲突

1. 首先，可以试图用`git push origin <branch-name>`推送自己的修改；

2. 如果推送失败，则因为远程分支比你的本地更新，需要先用git pull试图合并；

3. 如果合并有冲突，则解决冲突，并在本地提交；

4. 没有冲突或者解决掉冲突后，再用`git push origin <branch-name>`推送就能成功！

> 如果`git pull`提示`no tracking information`，则说明本地分支和远程分支的链接关系没有创建

用命令

```git
git branch --set-upstream-to <branch-name> origin/<branch-name>
```

小结

- 查看远程库信息，使用`git remote -v`;

- 本地新建的分支如果不推送到远程，对其他人就是不可见的；

- 从本地推送分支，使用`git push origin branch-name`，如果推送失败，先用`git pull`抓取远程的新提交；

- 在本地创建和远程分支对应的分支，使用`git checkout -b branch-name origin/branch-name`，本地和远程分支的名称最好一致；

- 建立本地分支和远程分支的关联，使用`git branch --set-upstream branch-name origin/branch-name`；

- 从远程抓取分支，使用`git pull`，如果有冲突，要先处理冲突。
