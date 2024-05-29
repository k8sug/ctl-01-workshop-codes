# Use an official lightweight Python image.
# alpine is much smaller than the default python image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Install dependencies:
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the local directory contents into the container at /app
COPY . /app

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run frontend_app.py when the container launches
CMD ["python", "frontend_app.py"]
