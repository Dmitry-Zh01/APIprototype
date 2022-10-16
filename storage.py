import argparse
import os
import json
import tempfile

parsing = argparse.ArgumentParser()
parsing.add_argument("--key", help='input key')
parsing.add_argument("--val", help='input value')
args = parsing.parse_args()

storepath = os.path.join(tempfile.gettempdir(), 'storage.data') 

if os.path.isfile(storepath):
    if args.val:
        with open(str(storepath), "r") as x:
            j = json.load(x)
            if args.key in j:
                j[args.key] = j[args.key] + [args.val]
            else:
                j.update({args.key: [args.val]})
        with open(str(storepath), "w") as x:
            json.dump(j, x)
    else:
        try:
            with open(str(storepath), "r") as x:
                j = json.load(x)
                if j[args.key] == None:
                    print('\n')
                if len(j[args.key]) > 1:
                    print(', '.join(j.get(args.key)))
                else:
                    print(*j.get(args.key))
        except:
            print(None)
else:
    d = {}
    with open(str(storepath), "w") as x:
        if args.val:
            d = {args.key: [args.val]}
            json.dump(d, x)
        else:
            d = {args.key: None}
            print(None)