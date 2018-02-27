# Nginx-Balance



> * 项目基于 [Django](https://www.djangoproject.com/) + [AdminLTE](https://www.almsaeedstudio.com/) 构建
> * 因为增加了 iptables 自动控制，所以暂时不支持 docker 方式部署；需要本地测试的同学请使用 vagrant 方式
> * 为了后续扩展方便，请大家使用 [Tengine](http://tengine.taobao.org/) 替代 Nginx 服务



## 功能
* Nginx 可视化配置
* Nginx 负载均衡（反向代理）配置
* Nginx 证书支持
* 系统状态监测
* 自动维护防火墙规则（白名单）
* 支持 TCP 被动后端节点宕机检测
* 支持 HTTP 主动后端节点宕机检测
* 日志实时查询
* 请求统计

## 运行
* 克隆代码
``` 
git clone https://github.com/baoyubobo/Nginx_balancer.git

```
* 卸载 nginx
```
sudo apt-get -y purge nginx-* nginx*
sudo apt-get -y autoremove
```
* 安装 tengine
```
git submodule update --init --recursive
cd resource/nginx/tengine
sudo apt-get install -y build-essential libssl-dev libpcre3 libpcre3-dev zlib1g-dev
sudo ./configure --user=www-data --group=www-data --prefix=/etc/nginx --sbin-path=/usr/sbin --error-log-path=/var/log/nginx/error.log --conf-path=/etc/nginx/nginx.conf --pid-path=/run/nginx.pid
sudo make
sudo make install
sudo mkdir -p /etc/nginx/conf.d

```

* 安装依赖
```
sudo apt-get install -y python-dev python-pip iptables libcurl4-openssl-dev
sudo pip install -r requirements.txt  
```
* 初始化数据库
```
python manage.py makemigrations  
python manage.py migrate  
```
* 启动服务
```
sudo python manage.py runserver 
sudo nginx

```




