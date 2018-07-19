# Evaluator for SWAG dataset on beaker

FROM library/python:3.6-slim-jessie


# set the working directory

WORKDIR /swag-evaluator


# install python packages

ADD ./requirements.txt .

RUN pip3.6 install --upgrade pip \
 && pip3.6 install -r requirements.txt


# add in the readme and evaluation script

ADD readme.md .
ADD evaluate.py .


# define the default command

# if you need to run a long-lived process, use `docker run --init`
CMD ["/bin/bash"]
