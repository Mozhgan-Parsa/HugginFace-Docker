# Docker Flask Gunicorn

This repository contains a Dockerized Flask application deployed with Gunicorn. The purpose of this application is to provide a scalable and efficient web service.

## Prerequisites

Before running the application, ensure that you have Docker installed on your system. You can download and install Docker from [here](https://docs.docker.com/get-docker/).

## Getting Started

To run the Flask application with Gunicorn, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/docker-flask-gunicorn.git
    ```

2. Navigate to the `docker-flask-gunicorn` directory:

    ```bash
    cd docker-flask-gunicorn
    ```

3. Run the following command to start the application:

    ```bash
    sudo docker-compose up -d --scale app=3
    ```

    This command will create and start three instances of the Flask application using Docker Compose. The `-d` flag runs the containers in detached mode, meaning they will continue to run in the background.

4. Once the containers are up and running, you can access the application by navigating to `http://localhost:5000` in your web browser.



