#地址：https://leetcode-cn.com/
```
Git 使用方法

git init 初始化

git  status  状态

git  add XXX  添加文件

git commit -m "XXX" 版本控制
```
* 注意：
* 红色未添加
* 绿色已添加 
* git 三大区域：工作区 暂存区 版本库
* git 回滚： git reset --hard 版本号
* git log 回滚到之前的版本/reflog回滚到之后的版本


**git 分支**
```
git branch

git branch dev

get merge

git checkout dev 切换分支

git branch -d dev 删除分支

git remote add origin https://XXXXXXXXXX 别名

git push  -u origin master 推送到master分支

```

**分支合并**
```
git merge master
```
 继续开发
 ```
 git status
 
 git add . 
 
 git commit -m "DDD"

```
**推送代码**
git push origin dev

**拉取代码**
```
git pull origin dev
```



**总结**

 添加远程连接（别名）
```
git remote add origin xxxx地址
```

推送代码
```
git  push origin dev
```
下载代码
```
git clone 地址
```
**拉取代码**
```
* git pull origin dev

等价于

* git fectch origin dev
* git merge orogin/dev
```
保持代码提交整洁（变基）
git rebase 分支

记录图形展示
```
git log --graph --pretty=format:"%h,%s"
```

**解决冲突**
下载beyond compare 软件
git 配置  bc3 命令：

 * 1、git config --local merge.tool bc3
 * 2、git config --local mergetool.path "/usr/local/bin/bcomp"
 * 3、git config --local mergetool.keepBackup false



