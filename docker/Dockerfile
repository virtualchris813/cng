FROM centos

EXPOSE 5000

RUN yum update -y
RUN yum install epel-release -y
RUN yum -y install python-pip wget postgresql postgresql-devel gcc make python-devel
RUN cd / && wget -O cng.tar.gz https://github.com/virtualchris813/cng/blob/master/cng.tar.gz?raw=true && tar -zxf /cng.tar.gz && cd /cng
RUN pip install --upgrade pip && pip install -r /cng/requirements.txt

ENTRYPOINT /cng/start.sh

MAINTAINER Chris Adams <virtualchris813@gmail.com>
