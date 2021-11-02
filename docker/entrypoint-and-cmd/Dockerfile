FROM python:3.9-slim

# Copy the application source code. Keep the .dockerignore file up to date
# to make sure Docker will contain only the bare minimum.
COPY . .

# Specify default executable for the image and also provide default agrument
ENTRYPOINT ["python", "./app.py", "--direction"]
CMD ["right"]
