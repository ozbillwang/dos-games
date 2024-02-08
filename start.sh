#!/usr/bin/env bash

echo "make sure you have creatd the volumen "dosgame" and copy the zip file in it"

docker rm -f dosgame
docker run -d --name dosgame -p 8080:262 -v dosgame:/app/static/games/bin ozbillwang/dosgame
