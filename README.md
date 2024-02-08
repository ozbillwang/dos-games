# 🎮 中文 DOS 游戏

## 定制
* 单独建个[game.list](game.list), 免的游戏下载时间过长
* 支持在容器里运行游戏。
* 支持docker volume

## todo list

暂时还不清楚，如何能保持游戏进程。 

以下是搭载环境过程

## 前提条件

* 容器的运行， 因为有几个启动脚本，故暂时只支持在linux 环境下运行。
* [安装了docker 服务](https://docs.docker.com/engine/install/)

## 下载游戏文件

如果不希望下载全部的游戏（总共30+GB，需要从网站https://dos.lol 那里下载，时间会很长，而且有时几乎花上一天，都无法完全下载完的），可以定制文件 game.list, 每行一个游戏名称即可，这样你可以即可开始玩这几个游戏了。
```
# 查看所有的游戏列表：
$ cat all_game.list

# 自己建个想玩的游戏列表， 从 "all_game.list" 复制即可
$ cat game.list

大富翁2
仙剑奇侠传
...
...
```

在根目录下运行 Python 3 脚本

``` python
python download_data.py
```

如果希望下载所有的游戏，那么删除文件 `game.list` 后，再运行上面的下载命令， 记住，这个要花很长的时间，需要有耐心。

## 在容器内运行

```
# 先将游戏 zip 文件，存入一个docker volume 里， 以后可以再利用。 
./volume.sh

# 启动容器
./start.sh
```

运行后， 访问 http://localhost:8080 就可以玩游戏了。 如果端口8080 已经被占用，那就在 [start.sh](start.sh] 里调整一下，再运行即可。 

如果定制了game.list，那么就只能玩game.list 里的游戏。 也就是说，你还是能看到所有游戏的图片，但是只能玩你在 `game.list`里的游戏。 

![image](https://github.com/ozbillwang/dos-games/assets/8954908/a09a6318-0e2e-4e25-a040-223af27b8b44)

若下载出错请参见 [Issue #26](https://github.com/rwv/chinese-dos-games/issues/26)

======

以下是原repo 的 README

# 🎮 中文 DOS 游戏

网址： https://dos.lol


中文 DOS 游戏合集，目前共有 1898 款游戏。

## 下载游戏文件

在根目录下运行 Python 3 脚本

``` python
python download_data.py
```
若下载出错请参见 [Issue #26](https://github.com/rwv/chinese-dos-games/issues/26)

## 游戏列表

参见 https://dos.lol/games

## IPFS

IPNS Hash: [`k2k4r8oyknzob8jjqpj6toer4dw3jc6srsbqlbsalktnw1fopb7iyqd2`](https://ipfs.io/ipns/k2k4r8oyknzob8jjqpj6toer4dw3jc6srsbqlbsalktnw1fopb7iyqd2)

## 网站源代码

请参见 [rwv/chinese-dos-games-web: 🌐 Source code of https://dos.zczc.cz](https://github.com/rwv/chinese-dos-games-web)

## 版权问题

本人明白此项目存在版权上的侵权，如版权方介意的话，请联系 [chinese.dos.games@outlook.com](mailto:chinese.dos.games@outlook.com)，本人将立刻删除有关文件。

## Contributing

欢迎提 [Issue](https://github.com/rwv/chinese-dos-games/issues) 和 [Pull request](https://github.com/rwv/chinese-dos-games/pulls) 来增加新的游戏!

PR 具体参见 [CONTRIBUTING.md](https://github.com/rwv/chinese-dos-games/blob/master/CONTRIBUTING.md)

## Credits

* [dreamlayers/em-dosbox: An Emscripten port of DOSBox](https://github.com/dreamlayers/em-dosbox)
* [db48x/emularity: easily embed emulators](https://github.com/db48x/emularity)
* [衡兰若芷制作的DOS游戏合集](https://tieba.baidu.com/p/3962261741)
