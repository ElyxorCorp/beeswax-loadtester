FROM python:3-slim AS build-env
ENV appdir /app
ADD src/main/python ${appdir}
WORKDIR ${appdir}

COPY ./requirements.txt ${appdir}/requirements.txt

WORKDIR ${appdir}
RUN /usr/bin/apt-get update
RUN /usr/bin/apt-get install wget gcc libssl-dev zlib1g-dev -y

RUN pip3 install --upgrade pip && \
    pip3 install -r ./requirements.txt

LABEL maintainer="<Britt> britt.cagnina@elyxor.com" \
      version="1.0" \
      description="beeswax loadtester for http events"

# Install protobuf
RUN /usr/bin/apt-get install git -y
RUN git clone https://github.com/google/protobuf.git
WORKDIR ${appdir}/protobuf
RUN git checkout tags/v3.5.1

# Install protoc
WORKDIR ${appdir}
RUN wget https://github.com/google/protobuf/releases/download/v3.5.1/protoc-3.5.1-linux-x86_64.zip

RUN /usr/bin/apt-get install unzip -y
RUN unzip protoc-3.5.1-linux-x86_64.zip
ENV PATH $PATH:${appdir}/bin
# RUN echo 'export PATH=$PATH:${appdir}/bin' >> ~/.bashrc && source ~/.bashrc

WORKDIR ${appdir}/protobuf/python
RUN ls -la
RUN python setup.py build
RUN python setup.py install

WORKDIR ${appdir}
ENTRYPOINT locust -f loadtester.py --host=https://beeswax-bidder.website.com
