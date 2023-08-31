import hashlib
import inspect
import os
import json
import urllib.request

from concurrent.futures import ThreadPoolExecutor, wait

root = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))

PREFIX = "https://dos-bin.zczc.cz/"
DESTINATION = os.path.join(root, 'bin')
BUF_SIZE = 65536
THREAD_SIZE = 10

# Read game names from game.list if it exists
game_names = []
game_list_path = os.path.join(root, 'game.list')  # Make sure 'root' is defined
if os.path.exists(game_list_path):
    with open(game_list_path, 'r', encoding='utf-8') as game_list_file:
        game_names = game_list_file.read().splitlines()

# Load game info from games.json based on game names if game_names is not empty
game_infos = {}
if game_names:
    games_json_path = os.path.join(root, 'games.json')
    if os.path.exists(games_json_path):
        with open(games_json_path, encoding='utf-8') as games_json_file:
            all_game_infos = json.load(games_json_file)
            game_infos = {game_name: all_game_infos['games'][game_name] for game_name in game_names}

# If game_names is empty or 'game.list' doesn't exist, load all game data from games.json
if not game_names or not game_infos:
    games_json_path = os.path.join(root, 'games.json')
    if os.path.exists(games_json_path):
        with open(games_json_path, encoding='utf-8') as games_json_file:
            game_infos = json.load(games_json_file)['games']

# # read game infos from games.json
# with open(os.path.join(root, 'games.json'), encoding='utf8') as f:
#     game_infos = json.load(f)


def generate_sha256(file):
    sha256 = hashlib.sha256()
    with open(file, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()


def download(identifier, url, file):
    print(f'Downloading {identifier} game file')
    urllib.request.urlretrieve(url, file)


def main(prefix=PREFIX, destination=DESTINATION):
    # create folder
    os.makedirs(destination, exist_ok=True)

    executor = ThreadPoolExecutor(max_workers=THREAD_SIZE)
    all_task = list()

    downloaded = list()
    for identifier in game_infos.keys():
        file = os.path.normcase(os.path.join(destination, identifier + '.zip'))
        url = prefix + urllib.parse.quote(identifier) + '.zip'
        if os.path.isfile(file) and generate_sha256(file) == game_infos[identifier]['sha256']:
            print(f'skip {identifier}')
        else:
            downloaded.append(identifier)
            task = executor.submit(download, identifier, url, file)
            all_task.append(task)

    wait(all_task)
    return downloaded


if __name__ == '__main__':
    main()
