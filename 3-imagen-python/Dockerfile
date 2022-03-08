FROM ubuntu
RUN apt-get update
RUN apt-get install -y python && apt-get install -y pip
RUN echo 1.0>>/etc/version && apt-get install -y git \
                        && apt-get install -y iputils-ping
RUN mkdir /app
WORKDIR /app
COPY app.py .

## COPY ##
COPY requirements.txt .
RUN pip install -r requirements.txt
ADD examples examples

ENTRYPOINT ["/bin/bash"]