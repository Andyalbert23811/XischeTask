# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the environment variable for the display (required for running browsers in headless mode)
ENV DISPLAY=:99

# Command to run the tests
CMD ["python", "-m", "unittest", "discover", "-s", "test_cases"]