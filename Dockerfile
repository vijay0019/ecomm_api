FROM python:3.10

# Install MySQL client library
RUN apt-get install -y default-libmysqlclient-dev

# Set environment variables for Django
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE ecomm_apis.settings

# Create and set the working directory
RUN mkdir /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app/
COPY . /app/

# Expose the port that the application will run on
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
