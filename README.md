Beeswax LoadTester 
-----------
#### Description

#### System Configuration - Quick Start
First, ensure that python3 and protoc is installed on your machine.  

The easiest way to install protoc is by downloading the binary from [protoc](https://github.com/google/protobuf/releases), though compiling it from source is also an option.  Afterwards, make sure you add the bin folder to your PATH env variable.

Additionally, you must install protobuf for python.  The easiest way is to clone the repo [protobuf](https://github.com/google/protobuf)

```
cd protobuf/python
python setup.py build
python setup.py test
python setup.py install
```
Once protobuf is installed, you should be able to run the service: 

#### Docker

The provided Dockerfile will build an image for the Alyvant Beeswax Augmentor.  

You can build the image by running:
```
docker build -t beeswax-loadtester:1.0 -f Dockerfile .
```

After building, verify that your image is listed and find your IMAGE ID with `docker images`

Run the new image in a docker container with:
```
sudo docker run -v /var/log/loadtester:/var/log/loadtester <IMAGE ID> 
```
