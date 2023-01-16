## git常用指令

git init                                                  # 初始化本地git仓库（创建新仓库）

git config --global user.name "xxx"                       # 配置用户名

git config --global user.email "xxx@xxx.com"              # 配置邮件

git clone git+ssh://git@192.168.53.168/VT.git             # clone远程仓库

git status                                                # 查看当前版本状态（是否修改）

git add .                                                 # 增加当前子目录下所有更改过的文件至index

git commit -m 'xxx'                                       # 提交

git commit --amend -m 'xxx'                               # 合并上一次提交（用于反复修改）

git commit -am 'xxx'                                      # 将add和commit合为一步

git log                                                   # 显示提交日志

git remote add origin git+ssh://git@192.168.53.168/VT.git # 增加远程定义（用于push/pull/fetch）

git branch                                                # 显示本地分支

git branch -a                                             # 显示所有分支

git branch -m master master_copy                          # 本地分支改名

git checkout -b master_copy                               # 从当前分支创建新分支master_copy并检出

git merge origin/master                                   # 合并远程master分支至当前分支

git push origin master                                    # 将当前分支push到远程master分支

git fetch                                                 # 获取所有远程分支（不更新本地分支，另需merge）

git pull origin master                                    # 获取远程分支master并merge到当前分支

git reset --hard HEAD                                     # 将当前版本重置为HEAD（通常用于merge失败回退）

git branch -d hotfixes/BJVEP933                           # 删除分支hotfixes/BJVEP933（本分支修改已合并到其他分支）

git branch -D hotfixes/BJVEP933                           # 强制删除分支hotfixes/BJVEP933

git rm --cached +文件名                                    # 不会删除物理文件，只是将已经add进缓存的文件删除。

git rm --f +文件路名                                        # 这个命令不仅将文件从缓存中删除，还会将物理文件删除，所以使用这个命令要谨慎。

git rm -r --cached 文件名								  # 若删除已经添加缓存的某一个目录下所有文件的话需要添加一个参数 -r

git pull --rebase origin master



## .gitignore

| 写法                                                    | 作用                                                         |
| ------------------------------------------------------- | ------------------------------------------------------------ |
| dir/                                                    | 忽略 `(.gitignore)N` 中的dir目录                             |
| /dir/                                                   | 忽略 `(.gitignore)O` 中的dir目录                             |
| file                                                    | 忽略`(.gitignore)N` 中的file 文件&目录（名为file的目录也会被忽略） |
| /file                                                   | 忽略`(.gitignore)O` 中的file文件\|目录                       |
| *.log                                                   | 忽略`(.gitignore)N` 中的*.log 文件&目录（符合名字的目录也将被忽略） |
| /dir/file                                               | 忽略`(.gitignore)O` 中的dir目录下的file文件\|目录            |
| `/dir/Abc*` 和 `/dir/Abc*.java` 和`/dir/*.java`         | 忽略`(.gitignore)O` 中的dir目录下符合Abc*（或Abc*.java或*.java）规则的文件&目录 |
| /dir/Abc*/                                              | 忽略`(.gitignore)O` 中的dir目录下符合Abc*的目录（不忽略dir下的文件!） |
| /dir/*/                                                 | 忽略`(.gitignore)O` 中的dir目录下的**符合\**\*的\**子目录**（注意/sub/file的文件不会忽略） |
| /dir/*/*.txt                                            | 忽略`(.gitignore)O` 中的dir目录下的**符合\**\*的\**子目录**下的，符合*.txt的文件&目录。注意是一个星，仅忽略一层，即/dir/sub/a.txt 和 /dir/sub/sub2/b.txt，仅仅忽略a.txt，不忽略b.txt，另外/dir/k.txt也不会被忽略 |
| /dir/**/*.txt                                           | 忽略 `(.gitignore)O` 中的dir目录下的**直接和间接子目录**下的，符合*.txt的文件&目录。两个星号表示0-n层级的目录 |
| `/sub/**` 和 `/sub/` 是等价的                           | 亲测。前者表示忽略/sub/下的所有直接或间接的目录和文件（***\*表示文件和目录，因为没有/结尾**），后者表示忽略/sub/下的东西 |
| `/sub/**/` 和 `/sub/` 是不等价的                        | 亲测。前者明确表示忽略目录除掉了文件，所以对于/sub/file是不会被忽略的。 |
| `sub/` 和 `/sub/` 含义不同                              | 前者忽略`(.gitignore)N`下的sub目录，后者忽略`(.gitignore)O`下的sub |
| `sub/abc/` 和 `/sub/abc/`                               | 这两个的含义完全相同（有点奇怪，本以为前者是递归所有的目录） |
| `**/src/main/java/` 和 `src/main/java/`                 | 不等价。前者匹配`(.gitignore)N`下的src/main/java/ 目录，要满足这个目录的层级结构的。后者等价于`/src/main/java/`，仅仅忽略`(.gitignore)O`下的该目录 |
| `**/src/main/file.txt` 和 `src/main/file.txt`           | 不等价。前者匹配`(.gitignore)N`下的src/main/file.txt，符合这个目录层级结构的将会被忽略，后者等价于`/src/main/file.txt`，仅仅忽略`(.gitignore)O`下所匹配的 |
| `**/dir/` 和 `dir/`                                     | 是等价的。上面的例子等价这个不等价，就是因为目录的层级数的问题导致的 |
| `**/file.txt` 和 `file.txt`                             | 是等价的。                                                   |
| 先后写`!a.txt`和`*.txt`                                 | 后面的配置覆盖前面的，导致所有*.txt文件都被忽略（有点奇怪，实际测试确实如此） |
| 先后写`*.txt` 和 `!a.txt`                               | 正确。能够忽略除了a.txt外的文件。                            |
| 对于.gitignore文件不在git仓库根目录的情况：参考特殊情况 | （参考特殊情况）                                             |