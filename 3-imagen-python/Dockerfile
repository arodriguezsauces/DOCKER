FROM ubuntu
RUN apt-get update
RUN apt-get install -y python
RUN echo 1.0>>/etc/version && apt-get install -y git \

                        && apt-get install -y iputils-ping
CMD ["/bin/bash"]
ENTRYPOINT ["df"]