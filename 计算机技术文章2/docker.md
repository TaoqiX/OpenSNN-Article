在 Deepin 系统中安装 Docker 可以通过以下步骤完成：

1. **更新软件包列表**：
   
   打开终端，执行以下命令来更新软件包列表，确保安装过程中使用的是最新的信息：
   ```
   sudo apt update
   ```

2. **安装依赖包**：

   确保安装以下软件包，以便安装 Docker：
   ```
   sudo apt install apt-transport-https ca-certificates curl software-properties-common
   ```

3. **添加 Docker 官方 GPG 密钥**：

   ```
   curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
   ```

4. **添加 Docker 软件包库**：

   ```
   sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
   ```

   如果你的 Deepin 系统不是基于 Debian 的，可以将上面命令中的 `debian` 替换为你系统对应的发行版。

5. **更新软件包列表**：

   为了使新添加的 Docker 软件包库生效，需要再次更新软件包列表：
   ```
   sudo apt update
   ```

6. **安装 Docker CE**：

   ```
   sudo apt install docker-ce
   ```

7. **启动 Docker 服务**：

   安装完成后，Docker 服务应该会自动启动，但你可以使用以下命令手动启动：
   ```
   sudo systemctl start docker
   ```

8. **验证 Docker 安装**：

   使用以下命令验证 Docker 是否成功安装：
   ```
   docker --version
   ```

   如果一切顺利，应该能看到 Docker 的版本信息。

9. **配置 Docker 用户权限（可选）**：

   为了避免每次运行 Docker 命令时都需要使用 `sudo`，你可以将自己添加到 Docker 用户组中：
   ```
   sudo usermod -aG docker $USER
   ```

   请确保退出当前终端会话并重新登录以使更改生效。

现在，Docker 应该已经成功安装在你的 Deepin 系统中了。

------------------

----------------------------------------------------

> https://mirrors.tuna.tsinghua.edu.cn/help/docker-ce/?eqid=8ff6dcd600015a6200000006648c8b89

```bash
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
sudo vim /etc/apt/sources.list.d/docker.list

# 清华源
# deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/debian buster stable

# 中科大源
# deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://mirrors.ustc.edu.cn/docker-ce/linux/debian buster stable

```
----------------------------------------------------
```bash
# add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
Traceback (most recent call last):
  File "/usr/bin/add-apt-repository", line 95, in <module>
    sp = SoftwareProperties(options=options)
  File "/usr/lib/python3/dist-packages/softwareproperties/SoftwareProperties.py", line 109, in __init__
    self.reload_sourceslist()
  File "/usr/lib/python3/dist-packages/softwareproperties/SoftwareProperties.py", line 599, in reload_sourceslist
    self.distro.get_sources(self.sourceslist)    
  File "/usr/lib/python3/dist-packages/aptsources/distro.py", line 93, in get_sources
    (self.id, self.codename))
aptsources.distro.NoDistroTemplateException: Error: could not find a distribution template for Deepin/apricot

报错了，为什么？
```
---------------------------

这个报错是因为 `add-apt-repository` 命令在 Deepin 系统上无法识别你当前的发行版。这可能是因为 Deepin 并不是基于标准的 Debian 或 Ubuntu 发行版，而是具有自己的发行版标识。

在这种情况下，你可以手动添加 Docker 软件包库，而不使用 `add-apt-repository` 命令。请按照以下步骤操作：

1. 打开 `/etc/apt/sources.list.d/docker.list` 文件，如果文件不存在则创建它：
   ```
   sudo nano /etc/apt/sources.list.d/docker.list
   ```

2. 在打开的文件中添加以下内容：
   ```
   deb [arch=amd64] https://download.docker.com/linux/debian buster stable
   ```

   注意，上面的 `buster` 是 Docker 对应的 Debian 发行版代号，你需要根据你的 Deepin 版本选择合适的代号。如果你的 Deepin 版本不是基于 Debian 的，请根据实际情况更改。

3. 保存并关闭文件。在 Nano 编辑器中，你可以按下 `Ctrl + O` 来保存，然后按下 `Enter`，最后按下 `Ctrl + X` 来关闭编辑器。

4. 更新软件包列表：
   ```
   sudo apt update
   ```

5. 现在你可以继续按照之前的步骤安装 Docker CE：
   ```
   sudo apt install docker-ce
   ```

完成上述步骤后，你应该能够在 Deepin 系统中成功安装 Docker。

----------------

```bash
docker images
docker pull nginx:latest
docker run -d -p 80:80 --name my_nginx_container nginx
docker ps # 显示正在运行的容器,获取容器ID
mkdir -p /usr/local/myusr/docker_nginx
mkdir -p /usr/local/myusr/docker_nginx/conf
mkdir -p /usr/local/myusr/docker_nginx/www
mkdir -p /usr/local/myusr/docker_nginx/logs
docker cp c8ecba885887:/etc/nginx/nginx.conf /usr/local/myusr/docker_nginx/
docker cp c8ecba885887:/etc/nginx/conf.d/. /usr/local/myusr/docker_nginx/conf/
docker cp c8ecba885887:/usr/share/nginx/html/. /usr/local/myusr/docker_nginx/www/
docker cp c8ecba885887:/var/log/nginx/. /usr/local/myusr/docker_nginx/logs/
docker stop c8ecba885887  # 停止容器
docker rm c8ecba885887  # 删除容器

docker run -p 80:80 \
-v /usr/local/myusr/docker_nginx/nginx.conf:/etc/nginx/nginx.conf \
-v /usr/local/myusr/docker_nginx/logs:/var/log/nginx \
-v /usr/local/myusr/docker_nginx/www:/usr/share/nginx/html \
-v /usr/local/myusr/docker_nginx/conf:/etc/nginx/conf.d \
-e TZ=Asia/Shanghai \
--privileged=true \
--name my_nginx_container \
--restart=always \
-d nginx



```

----------------

要通过 Docker 安装 Nacos，你可以使用官方提供的 Docker 镜像。Nacos 是一个开源的服务发现、配置管理和服务管理平台。以下是通过 Docker 安装 Nacos 的步骤：

1. **拉取 Nacos 镜像**：

   执行以下命令来拉取 Nacos 镜像：

   ```
   docker pull nacos/nacos-server
   ```

   这将从 Docker Hub 上拉取官方的 Nacos 镜像。

2. **运行 Nacos 容器**：

   一旦镜像拉取完成，你可以使用以下命令来运行一个 Nacos 容器。这个命令会创建一个名为 `nacos_server` 的容器，并暴露 Nacos 默认的端口（8848）：

   ```
   docker run -d --name nacos_server -p 8848:8848 nacos/nacos-server

      
   ###jwh
   docker run --env MODE=standalone --name my_nacos_server -d -p 8848:8848 nacos/nacos-server
   ###jwh
   ```

3. **验证容器是否正常运行**：

   运行以下命令来查看正在运行的容器列表，并确认 Nacos 容器是否在其中：

   ```
   docker ps
   ```

4. **访问 Nacos 控制台**：

   打开 Web 浏览器并访问 `http://localhost:8848/nacos`，这将打开 Nacos 控制台登录页面。默认用户名和密码为 `nacos/nacos`。

5. **使用 Nacos**：

   现在你可以使用 Nacos 控制台来管理你的服务注册、配置管理等功能。

通过以上步骤，你就成功地使用 Docker 安装和运行了 Nacos。如果有任何疑问或需要进一步帮助，请随时提问。

----------------

`-env MODE=standalone` 参数是用来设置 Nacos 运行的模式，这个参数是根据你的需求来决定是否添加的。

- 如果你想要在独立模式下运行 Nacos，也就是说 Nacos 不依赖外部的数据库或集群，那么添加这个参数是合适的。独立模式适用于小规模或者测试环境中。

- 如果你打算将 Nacos 与其他组件组成集群，或者使用外部的数据库存储 Nacos 的数据，那么你不需要添加这个参数。

所以，是否添加 `-env MODE=standalone` 参数取决于你的具体需求。


----------------------

要通过 Docker 安装 Redis 并设置密码，可以按照以下步骤进行：

1. **拉取 Redis 镜像**：

   执行以下命令来拉取 Redis 镜像：

   ```
   docker pull redis
   ```

   这将从 Docker Hub 上拉取官方的 Redis 镜像。

2. **运行 Redis 容器**：

   使用以下命令来运行一个 Redis 容器，并设置 Redis 的密码：

   ```
   docker run -d --name my_redis_container -p 6379:6379 redis redis-server --requirepass your_password
   ```

   将 `your_password` 替换为你想要设置的 Redis 密码。

3. **验证容器是否正常运行**：

   运行以下命令来查看正在运行的容器列表，并确认 Redis 容器是否在其中：

   ```
   docker ps
   ```

4. **连接到 Redis 容器**：

   如果你想要连接到正在运行的 Redis 容器，并在其中执行 Redis 命令，可以使用以下命令：

   ```
   docker exec -it my_redis_container redis-cli -a your_password
   ```

   将 `your_password` 替换为你设置的 Redis 密码。

现在，你已经成功地使用 Docker 安装了 Redis 并设置了密码。你可以通过容器的主机 IP 地址和端口（默认为 6379）以及密码连接到 Redis 服务。如果有任何问题或需要进一步帮助，请随时提问。

----------------------

之后要再次修改 Redis 的密码，你可以通过以下步骤操作：

1. **连接到 Redis 容器**：

   首先，使用以下命令连接到正在运行的 Redis 容器：

   ```
   docker exec -it my_redis_container redis-cli -a your_current_password
   ```

   将 `your_current_password` 替换为当前设置的 Redis 密码。

2. **使用 CONFIG SET 命令修改密码**：

   连接成功后，可以使用 `CONFIG SET` 命令来修改 Redis 的密码。执行以下命令：

   ```
   CONFIG SET requirepass your_new_password
   ```

   将 `your_new_password` 替换为你想要设置的新密码。

3. **退出 Redis 客户端**：

   完成密码修改后，可以使用 `QUIT` 命令退出 Redis 客户端。

4. **验证密码是否修改成功**：

   重新连接到 Redis 容器并使用新密码进行验证，确保密码修改成功。

现在，你已经成功地修改了 Redis 的密码。如果有任何问题或需要进一步帮助，请随时提问。

----------------





