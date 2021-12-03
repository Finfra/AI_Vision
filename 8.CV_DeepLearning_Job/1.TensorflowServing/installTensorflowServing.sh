#!/bin/bash

x=$(dpkg -l|grep tensorflow-model-server)
if [ ${#x} -eq 0 ];then
  #apt-get remove tensorflow-model-server
  echo "deb [arch=amd64] http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" | sudo tee /etc/apt/sources.list.d/tensorflow-serving.list && \
  curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | sudo apt-key add -
  apt-get update && apt-get install tensorflow-model-server
fi


pip install tensorflow-serving-api
pip install requests
