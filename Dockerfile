# Use the official Ubuntu 24.04 image as the base
FROM ubuntu:24.04

# Set an environment variable for the application directory
ENV APP_HOME=/app

# Set the working directory to the application directory
WORKDIR $APP_HOME

# Install Python, build-essential (includes gcc, g++, and make), and other necessary tools
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt $APP_HOME

# starting from ubuntu 24.04 installing Python packages system-wide using pip 
# without a virtual environment is restricted
# Create a virtual environment
RUN python3 -m venv venv

# Activate the virtual environment and install dependencies
RUN . venv/bin/activate && pip install --no-cache-dir --upgrade -r $APP_HOME/requirements.txt

# Copy the application code into the container
COPY . $APP_HOME

# Expose port 8000 to allow external access
EXPOSE 8000

# Command to run the FastAPI application using uvicorn
CMD ["sh", "-c", ". venv/bin/activate && uvicorn main:app --host 0.0.0.0 --port 8000"]