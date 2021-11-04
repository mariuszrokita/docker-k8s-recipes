FROM python:3.9-slim

LABEL maintainer="mariusz.rokita@gmail.com"

# Tools and prerequisites needed down the road
RUN apt-get update && apt-get -y install curl

# Install required dependencies
RUN pip install pipenv

# Change the working directory
WORKDIR /app

# Create a Python environment
COPY ./Pipfile ./Pipfile.lock ./
RUN pipenv sync

# Copy the application source code. Keep the .dockerignore file up to date
# to make sure Docker will contain only the bare minimum.
COPY . .

# The healthcheck can be placed here or in the docker-compose file
# HEALTHCHECK --interval=10s --timeout=30s --start-period=5s --retries=3 \
#     CMD curl --fail http://localhost:5000/health || exit 1

# Run Flask app
CMD ["pipenv", "run", "python", "./app.py"]

# Explicitly inform what ports are in use
EXPOSE 5000