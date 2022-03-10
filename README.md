# Prohibitus

Music Generation AI by Juho Kim, Minchan Kim, and Nikolas Marinkovich

## Requirements

- [PyTorch](https://pytorch.org/)
- [NumPy](https://numpy.org/)
- [tqdm](https://github.com/tqdm/tqdm)
- [PrettyMIDI](https://github.com/craffel/pretty-midi)

## Guides

### Generate Music in ABC file format

1. Download mscz music samples

Example:

```shell
python ./utilities/download_mscz.py 1000 ./utilities/mscz-files.csv ./resources/mscz
```

If you get some type of HTTP error, simply wait a bit and run the above script
again (maybe with reduced downloade speed). The server is complaining that you
are downloading too many things. Don't worry, already created files are skipped
automatically.

2. Convert mscz to xml

Example:

```shell
python ./utilities/mscz2xml.py ./resources/mscz/ ./resources/xml/ "C:\Program Files\MuseScore 3\bin\MuseScore3.exe"
```

If it gets stuck, press Ctrl+C and try running again. It should still be stuck.
Then, go to ./resources/xml/job.json and look at the first entry in the json
list. That is the problematic .mscz file. Simply delete that file and rerun the
above script. Don't worry, already created files are skipped automatically.

3. Convert xml to abc

Example:

```shell
./utilities/xml2abc.exe -o ./resources/abc/ ./resources/xml/*.xml
```

## Credits

- Inspiration
    - [karpathy: mingpt](https://github.com/karpathy/minGPT)
- Music score file format conversion
    - [Willem Vree: xml2abc.exe](https://wim.vree.org/svgParse/xml2abc.html)
    - [Willem Vree: abc2xml.exe](https://wim.vree.org/svgParse/abc2xml.html)
    - [MuseScore](https://musescore.org/)
- Datasets
    - [Xmader: MuseScore dataset](https://github.com/Xmader/musescore-dataset)
    - [asigalov61: Tegridy-MIDI-Dataset](https://github.com/asigalov61/Tegridy-MIDI-Dataset)
    - [fredrik-johansson: midi](https://github.com/fredrik-johansson/midi)
    - [Classical Archives - The Greats (MIDI)](https://thepiratebay.org/description.php?id=6734800)

## License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
