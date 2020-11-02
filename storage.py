import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()

parser.add_argument('--key', action='store', dest='key_name')
parser.add_argument('--val', action='store', dest='value')
args = parser.parse_args()


d = {}
di=[]
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
if os.path.exists(storage_path) is False:
    f = open(storage_path, 'w')
    json.dump([], f)
    f.close()

if args.value is not None:
    with open(storage_path, 'r+') as f:
        json_data = json.load(f)
        flag = True
        for i in json_data:
            if args.key_name in i:
                i[args.key_name].append(args.value)
                f.seek(0)
                json.dump(json_data, f)
                flag = False
        if flag:
            l = []
            l.append(args.value)
            d[args.key_name] = l
            json_data.append(d)
            f.seek(0)
            json.dump(json_data, f)
else:
    with open(storage_path, 'r') as f:
        new_data = json.load(f)
        for i in new_data:
            if args.key_name in i:
                print(", ".join(i[args.key_name]))

