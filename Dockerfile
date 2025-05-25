# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port (change if your app uses a different port)
EXPOSE 5000

# Run the application (update if your app uses a different entrypoint)
CMD ["python", "app.py"]
