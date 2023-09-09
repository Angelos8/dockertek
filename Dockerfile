# container based on python
FROM python:3.9
# if your Django application logs messages or prints output, 
# setting PYTHONUNBUFFERED ensures that these messages 
# are displayed in real-time in the container's logs 
# when you run docker logs.
ENV PYTHONUNBUFFERED 1
# create a fulder that will have the container
RUN mkdir /app
# work directory for all project files to exist
WORKDIR /app
# install modules and dependencies
COPY requirements.txt /app/
# install the requirements
RUN pip install -r requirements.txt
# copy the folder from vs code to the container in the app folder
COPY . /app/
# Copy the MongoDB initialization script to the container
COPY init_mongo.py /app/
# Run the MongoDB initialization script when the container starts
CMD ["python", "init_mongo.py"]