# 使用官方的 Python 基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 安装构建工具和必要的库
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# 复制 requirements.txt 并安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用程序代码
COPY . .

# 暴露端口
EXPOSE 5000

# 使用 Gunicorn 启动 Flask 应用
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]

