FROM python:3.9-slim

LABEL maintainer="mariusz.rokita@gmail.com"

# Install required dependencies
RUN pip install pipenv

# Create a non-root user to run the application
ARG USERNAME=appuser
ARG USERID=999
RUN useradd --create-home --system --shell /bin/bash --uid ${USERID} ${USERNAME}
USER ${USERNAME}
WORKDIR /home/${USERNAME}

# Create a Python environment
COPY ./Pipfile ./Pipfile.lock ./
RUN pipenv sync

# Copy the application source code. Keep the .dockerignore file up to date
# to make sure Docker will contain only the bare minimum.
COPY . .

# Run our custom application
CMD ["pipenv", "run", "python", "./app.py"]
