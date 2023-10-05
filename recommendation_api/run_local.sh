#!/bin/bash
 DIR=`dirname "$0"`
 cd ${DIR}

 docker stop rec
 docker rm rec
 docker build . -t recommendation_api
 docker run -d --name rec -p 80:80 recommendation_api
