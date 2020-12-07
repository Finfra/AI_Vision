#!/bin/bash

tensorflow_model_server  \
	--port=9018              \
	--rest_api_port=9020     \
	--model_name=iris        \
	--model_base_path=/tmp/saved_model >>/tmp/log &
