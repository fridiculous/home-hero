FROM api-base:latest

MAINTAINER  Simon Frid <simon.frid@gmail.com>

# Set the PATH variable properly.
ENV PATH $PATH:/root/.local/bin

RUN npm install -g yuglify

# Set default locale and encoding for characters like ’
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8

# Copy the requirements.txt file.
COPY requirements.txt /code/requirements.txt

# Install the dependencies in case they differ from the base image.
WORKDIR /code
RUN pip3 install -r requirements.txt

CMD echo 'hi'
