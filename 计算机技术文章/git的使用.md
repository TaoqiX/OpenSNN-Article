## git clone命令做了什么
1. 创建一个新的目录，并将远程仓库的所有文件和提交历史复制到这个目录。
    - 解释：就是将远程的仓库(包含了所有的分支)下载到了本地
2. 自动为你**检出默认分支**（通常是 `master` 或 `main`）。
    - 解释：关键字“检出”，就是运行`git branch`显示的是`master` 或 `main`，远程的其他非默认分支**不会**显示。
3. **设置远程仓库**（通常命名为 `origin`）并添加所有远程分支为**远程跟踪分支**。**为默认分支设置了上游分支**。
    - 解释与个人理解：
    - 运行`git branch -r`查看所有**远程跟踪分支**。
    - 类似于`git branch --set-upstream-to=origin/master master`。
    - 设置了上游分支后，使得在执行`git pull`或者`git push`等操作时更加方便。
    - **远程跟踪**分支，远程**上游**分支，分支的**跟踪**信息，分支的**追踪**关系。前者是站在整个本地仓库和远程仓库的角度上；后面三个意思一样，是站在本地仓库的**某一个分支**的角度上。

## git branch的相关命令
- git branch
列出当前 Git 仓库中存在的所有分支，并标识当前所在的分支
- git branch -r
查看所有远程跟踪分支，这个命令会列出所有远程仓库中的分支。
- **git branch -a**
等于`git branch`加上`git branch -r`。
- **git branch -vv**
查看所有本地分支和它们所跟踪的远程分支，以及提交差异。
- git remote show origin
查看特定远程仓库的仓库信息。

### 分支的新建、切换与删除
`git branch aaa` ：新建分支aaa
`git checkout aaa` ：切换到分支aaa
`git checkout -b bbb` ：新建并切换到分支bbb
`git checkout -b dev origin/dev`：创建并切换到一个名为 dev 的本地分支，并将其设置为跟踪 origin/dev。
`git branch -d aaa` ：安装删除分支aaa
`git branch -D aaa` ：强制删除分支aaa


```bash
$ git clone https://gitee.com/XXX/vue3
正克隆到 'vue3'...
remote: Enumerating objects: 74, done.
remote: Counting objects: 100% (74/74), done.
remote: Compressing objects: 100% (64/64), done.
remote: Total 74 (delta 7), reused 0 (delta 0), pack-reused 0
展开对象中: 100% (74/74), 完成.
$ 
$ cd vue3
$ 
$ git branch 
* master
$ 
$ git branch -r
  origin/HEAD -> origin/master
  origin/dev
  origin/master
$ 
$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/dev
  remotes/origin/master
$ 
$ git branch -vv
* master 84ebdd3 [origin/master: 落后 3] 完成版本1.1
$ 
$ git remote show origin
* 远程 origin
  获取地址：https://gitee.com/XXX/vue3
  推送地址：https://gitee.com/XXX/vue3
  HEAD 分支：master
  远程分支：
    dev    已跟踪
    master 已跟踪
  为 'git pull' 配置的本地分支：
    master 与远程 master 合并
  为 'git push' 配置的本地引用：
    master 推送至 master (最新)
$
```
### 配置远程跟踪分支
```bash
git clone https://gitlab.xxx.com/frontendgroup/xxx-web
cd xxx-web
git branch -r
git config --get-all remote.origin.fetch
git config --unset-all remote.origin.fetch
git config remote.origin.fetch "+refs/heads/master:refs/remotes/origin/master"
git config --add remote.origin.fetch "+refs/heads/dev:refs/remotes/origin/dev"
git config --get-all remote.origin.fetch
git branch -r
git fetch origin
git branch -r

```
### git操作
```bash
git merge --squash jimdev   #不保留提交历史
git merge --no-ff jimdev
git merge --no-commit feature-branch  #保留提交历史
git merge origin/dev  #将origin的dev分支，合并到本地当前所在分支上

git branch -vv
git branch --set-upstream-to=origin/dev jimdev 
git branch --unset-upstream jimdev
git checkout -b new-branch abcd1234
git checkout -b dev origin/dev


git clone --branch master --single-branch https://gitlab.xxx.com/x/xxx-web
git rm -r --cached .
git add .
git status

git fetch origin
git fetch origin main feature-branch
git fetch origin "^ignored_branch"
git fetch --prune origin "^ignored_branch"

git merge --ff-only <branch_name_to_merge>
git merge --no-commit --no-ff jimdev    # good
git merge --squash jimdev

git reset --hard 7bff7b6
git reset --hard HEAD^
git reset --hard HEAD~7
git reflog
git checkout 7bff7b6
#reset和checkout的区别?

git push --depth=1 origin <branch_name>
git push -d 1 origin <branch_name>
git push --depth=1 origin mydev:dev     # 本地mydev，远程dev
#`--depth=1`这会将最新提交推送到远程仓库，并忽略历史记录
git push --set-upstream origin mydev:main
git push --set-upstream gitlab mydev:master
# 一个本地分支可以添加多个远程分支,只能绑定一个上流分支。

```
## git fetch的相关命令

## git merge的相关命令

#####

----------

```
获取更多计算机知识，请访问网站：开思通智网
官网地址：https://www.opensnn.com/
“一起来O站，玩转AGI！”

```