
# FastText Flask Service

A simple Flask service for language detection using FastText.

## Features

- Language detection via FastText
- Dockerized for easy deployment
- Ready for production with Gunicorn

## Requirements

- Python 3.10
- Docker

## Installation

### Clone the repository

\`\`\`sh
git clone https://github.com/mylukin/FastLid.git
cd fasttext_flask_service
\`\`\`

### Set up Python virtual environment

\`\`\`sh
python -m venv venv
\`\`\`

### Install dependencies

\`\`\`sh
make install
\`\`\`

## Running the Service

### Run locally

\`\`\`sh
make run
\`\`\`

### Stop the service

\`\`\`sh
make stop
\`\`\`

### Restart the service

\`\`\`sh
make restart
\`\`\`

## Docker

### Build Docker image

\`\`\`sh
make docker-build
\`\`\`

### Push Docker image to repository

\`\`\`sh
make docker-push
\`\`\`

### Pull Docker image from repository

\`\`\`sh
make docker-pull
\`\`\`

### Run Docker container

\`\`\`sh
make docker-run
\`\`\`

## API Endpoint

### Detect language

- **URL:** \`/detect_language\`
- **Method:** \`POST\`
- **Content-Type:** \`application/json\`
- **Request Body:**

\`\`\`json
{
  "text": "Hello, world!"
}
\`\`\`

- **Response:**

\`\`\`json
{
  "language": "en"
}
\`\`\`

## Model

Download the FastText language identification model from [official FastText models](https://fasttext.cc/docs/en/language-identification.html) and place the \`lid.176.bin\` file in the project root directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
