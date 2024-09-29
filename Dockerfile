# Use an official Python runtime as a parent image
FROM python:3.13.0rc2-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 to the outside world
EXPOSE 8080

# Run app.py when the container launches
CMD ["python", "app.py"]
