#!/usr/bin/env bash

sudo docker run --rm -it -v ~/git/spotify_API_Wrapper:/opt/app -p 8002:8000 spotify-api-wrapper:1.0.0