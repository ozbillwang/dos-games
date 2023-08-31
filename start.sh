docker rm -f dosgame
docker run -d --name dosgame -p 262:262 -v $(pwd)/bin:/app/static/games/bin ozbillwang/dosgame
docker logs -f dosgame
