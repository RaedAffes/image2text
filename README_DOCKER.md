# Docker Usage for image2text

This guide explains how to build and run the `image2text` Python application using Docker and Docker Compose.

## Prerequisites
- [Docker](https://docs.docker.com/get-docker/) installed
- [Docker Compose](https://docs.docker.com/compose/install/) installed

## 1. Build the Docker Image

Open a terminal in the project directory and run:

```sh
docker build -t image2text .
```

## 2. Run the Container

You can run the app using Docker:

```sh
docker run -p 5000:5000 image2text
```

Or use Docker Compose:

```sh
docker compose up --build
```

## 3. Access the Application

The app will be available at: [http://localhost:5000](http://localhost:5000)

## 4. Stopping the Containers

To stop the containers started by Docker Compose:

```sh
docker compose down
```

## Notes
- Update the `EXPOSE` and port mappings if your app uses a different port.
- Make sure your `requirements.txt` is up to date with all dependencies.

---

For more details, see the official [Docker documentation](https://docs.docker.com/).
