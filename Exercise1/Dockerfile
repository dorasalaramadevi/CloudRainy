# Use an official Python runtime as a parent image
FROM python:3.8-slim
RUN pip install flask
ENV FLASK_APP getapi.py
# Set the working directory in the container
WORKDIR /testwork


# Copy the Python script to the container
COPY getapi.py /testwork/
COPY data.json /testwork/

EXPOSE 5000

# Run the Python script when the container launches
CMD ["flask","run","--host","0.0.0.0"]
