FROM centos

EXPOSE 5000

RUN yum update -y
RUN yum install epel-release -y 
RUN yum -y install python-pip wget postgresql postgresql-devel gcc make python-devel
RUN cd / && wget 192.168.1.99/cng.tar.gz && tar -zxf /cng.tar.gz && cd /cng
RUN pip install --upgrade pip && pip install -r /cng/requirements.txt

ENTRYPOINT /cng/start.sh 

MAINTAINER Chris Adams <virtualchris813@gmail.com>
