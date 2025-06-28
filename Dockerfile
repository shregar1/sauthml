# Use Ubuntu as the base image
FROM --platform=linux/amd64 ubuntu:22.04

RUN echo "Set environment variables to avoid interaction prompts"
ENV DEBIAN_FRONTEND=noninteractive

RUN echo "Set the time zone"
ENV TZ=Asia/Kolkata

RUN echo "Install necessary dependencies in a single layer"
RUN apt-get update && \
    apt-get install -y \
    curl \
    wget \
    gcc \
    g++ \
    software-properties-common \
    apt-transport-https \
    ca-certificates \
    lsb-release \
    gnupg && \
    rm -rf /var/lib/apt/lists/*

RUN echo "Install Azure CLI, .NET SDK, and Python 3.11"
RUN add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y \
    python3.11 \
    python3.11-venv \
    python3.11-dev \
    python3-pip && \
    xmlsec1 && \
    rm -rf /var/lib/apt/lists/*

RUN echo "Set alternatives for python3"
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1

RUN echo "Upgrade pip"
RUN python3 -m pip install --no-cache-dir --upgrade pip

RUN echo "Copy the requirements.txt first to leverage Docker layer caching"
COPY requirements.txt /app/requirements.txt

RUN echo "Install Python dependencies"
RUN pip3 install --no-cache-dir -r /app/requirements.txt

RUN echo "Set the working directory"
WORKDIR /app

RUN echo "Copy the FastAPI application code to the container"
COPY . /app

RUN echo "Expose port"
EXPOSE 8000

RUN echo "Run the FastAPI app with Uvicorn"
CMD ["python3", "app.py"]