python download_data.py
docker volume create dosgame
docker run --rm -v dosgame:/data -v $(pwd)/bin:/apps/bin alpine sh -c "cp -r /apps/bin/* /data/"
docker run --rm -v dosgame:/data alpine find /data
