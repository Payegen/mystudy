### 服务命令

| 服务         | 命令                       |
| ------------ | -------------------------- |
| 启动         | `systemctl start docker`   |
| 停止         | `systemctl stop docker`    |
| 重启         | `systemctl restart docker` |
| 查看状态     | `systemctl status docker`  |
| 设置开机启动 | `systemctl enable docker`  |



### 镜像操作

| 镜像操作                   | 命                 |
| -------------------------- | ------------------ |
| `docker images`            | 查看本地的所有镜像 |
| `docker images -q`         | 查看所用的镜像id   |
| `docker search  [args]`    | 查找镜像           |
| `docker pull [arg]:版本号` | 拉取镜像           |
| `docker rmi [id]`          | 删除镜像，后接id   |

### 容器命令：

**1.查看容器**

`docker ps` 查看正在运行的容器

`docker ps -a` 查看所有的容器



**2.创建运行容器**

`docker run 【参数】`

参数说明：

- `-i`保持容器运行。通常与-t同时使用。加入it这两个参数后，容器创建后自动进入容器中，退出容器后，容器自动关闭。
- `.-t`为容器重新分配一个伪输入终端，通常与-i同时使用。
- `-d`:以守护（后台)模式运行容器。创建一个容器在后台运行，需要使用docker exec进入容器。退出后，容器不会关闭。
- ` -it`创建的容器一般称为交互式容器，`-id`创建的容器一般称为守护式容器
-  `--name`:为创建的容器命名。
- `-p` 端口映射 主机端口:容器端口

**3.操作容器**

- 进入容器： 

  `docker exec [参数]`

- 停止/启动容器：

  `docker stop/start [容器名]`

- 删除：

  `docker rm [容器名]`

- 查看容器信息：

  `docker inspect [容器名]`



### 数据卷

![1665930118729](C:\Users\Linkys\AppData\Roaming\Typora\typora-user-images\1665930118729.png)

**作用：**

容器数据持久化，外部机器与容器间接通信，容器之间数据交换。

**概念：**

数据卷是宿主机的一个目录或者一个文件，一个数据卷可以被多个容器挂载，一个容器也可以挂载多个数据卷。

**配置数据卷：**

在创建容器的时候使用参数-v设置数据卷

`docker run ... -v [宿主机目录/文件]:[容器内目录或者文件]`

- 注意：目录必须是绝对路径，如果不存在，会自动创建。



### **数据卷容器**：

![1665932843893](C:\Users\Linkys\AppData\Roaming\Typora\typora-user-images\1665932843893.png)

概念：

​	宿主机的一个目录或者文件

作用：

	- 容器数据持久化
	- 客户端和容器数据交换
	- 容器之间数据交换

创建一个容器，挂载一个目录，让其他容器继承该容器（--vol）。

**配置数据卷容器**：

1. 创建数据卷容器，使用-v 设置数据卷。

`docker run -it --name=c3 -v /volume ...`

> docker会自动分配一个目录在宿主机上，这里设置的是容器的目录

2. 创建c1,c2容器，使用--volumes-from参数设置数据卷

`docker run -it --name=c1 --volumes-from c3 ...`

`docker run -it --name=c2 --volumes-from c3 ...`



### 镜像制作：

1.容器转为镜像

`docker commit 容器id 镜像名称:版本号`

`docker save -o 压缩文件名 镜像名称:版本号`

`docker load -i 压缩文件名`

2.dockerfile

`docker bulid -f dockerfile文件路径 -t 镜像名称:版本号 `

