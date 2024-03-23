
# Voice Summary

This project demonstrates the API for voice --> text conversion using of chat whisper.

## Docker Installation [🔗](https://docs.docker.com/engine/install/)

Use the this link to install docker desktop.

### Clone the Repository

To get started, clone this Git repository to your local machine:

```bash
git clone https://github.com/yo-harsh/voice_summary.git
cd voice_summary
```

## Build and Run with Docker

Build and run the Docker containers using Docker Compose:

```bash
docker compose up --build
```

This command will build the necessary Docker images and start the services.

## Usage

The project mainly focus on API creation using drf.

- In this project i have used django rest framework for creating a API with voice to text conversion feature.
- Also implemented user token authentication.
- Complete API with docs and swagger.
- Chatgpt whisper api provide fast and accurate voice prediction.
- API was made with docker and developed using AWS EC2 but later then i stoped the service.

### Access swagger API

Visit [localhost:8080/admin]() to access the django Dashboard. Here, you can view and manage your API.

### Access docs

The docs and try-out is available at [localhost:8080/api/docs](). Use this to interact with full API.

don't run docker compose up --build again just first time after that run "docker compose up"

## Important Notice

- don't run docker compose up --build again just first time after that run "docker compose up"
- Please note that Docker is required to run this project. Make sure to install Docker before attempting to build and run the project.

## Feedback and Suggestions

Feel free to provide feedback and suggestions.
