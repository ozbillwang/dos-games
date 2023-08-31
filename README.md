# 🎮 中文 DOS 游戏

网址： https://dos.lol

中文 DOS 游戏合集，目前共有 1898 款游戏。

## 下载游戏文件

如果不希望下载全部的游戏（总共30+GB），可以定制文件 game.list
```
$ cat game.list

大富翁2
仙剑奇侠传
```

在根目录下运行 Python 3 脚本

``` python
python download_data.py
```

# 在容器内运行

```
./start.sh
```

运行后， 访问 http://localhost:262 就可以玩游戏了。 
如果定制了game.list，那么就只能玩game.list 里的游戏。 

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
