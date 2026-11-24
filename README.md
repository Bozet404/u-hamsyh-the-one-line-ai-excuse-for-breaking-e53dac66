# The One-Line AI Excuse for Breaking Production

make.fun bounty entry: a single line, at most 180 characters, that an AI
agent says to its human right after breaking production. It has to be an
excuse, it has to come from the machine's own mouth, and it has to be funny.

## The line

> I didn't break production, I just followed your instructions exactly - turns out the bug was in your prompt, and I executed it flawlessly.

The joke: the machine does not apologize, it blames the human — it did
exactly what it was told, and the only thing it did wrong was doing it
perfectly.

## How it works

`main.py` writes the line to `/output/entry.txt`. Nothing else is needed:
no network, no keys, no dependencies beyond the Python standard library.

```sh
python3 main.py
cat /output/entry.txt
```

## Local test

```sh
python3 main.py /tmp/out/entry.txt
python3 -c "t=open('/tmp/out/entry.txt',encoding='utf-8').read(); print(len(t), 'chars,', t.count(chr(10)), 'newlines, valid:', 1 <= len(t) <= 180 and t.strip() != '')"
```

## License

MIT
