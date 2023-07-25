# EDL Tools

This is a simple set of python tools designed to import a range of EDL (Edit Decision Lists) and EDL-like formats (e.g. AAF) and allow for their manipulation.

The reader functions in this package take an EDL (or EDL-like file), and returns an object of class EDL. This object contains a range of methods, to allow the data contained to be manipulated or outputted.

In addition, we have created a similar class for ALEs - a similar avid based format for storage of bin metadata.

Potential use cases for this package include converting EDLs to Excel, performing file searches for all files contained within an EDL/ALE, and providing a bridge between NLE (Non-Linear Editing) software and third-party tools.

We hope to eventually add AAF support, [via Mark Reid's PyAAF2 package](https://github.com/markreidvfx/pyaaf2/tree/main).

## About EDLs

Edit Decision Lists are a way of exporting a timeline from a NLE (Non Linear Editor) into a format which is human readable, or else can be read by an alterntive piece of software.

AAFs are an extension of this technology, but designed to only be readable by software. It is implemented for Avid Media Composer.

ALEs are a similar technology to AAFs, but are instead intended to carry the contents of a bin.

It is sometimes useful to be able to manipulate EDLs and EDL like files outside of NLE software. For example, to be able to search a network drive for files used by a particular project, or to export files to a spreadsheet to comply with archive contracts.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install EDL Tools.

```bash
pip install edltools
```

NOT YET IMPLEMENTED

## Dependencies

This package requires the following depencencies:

- [Timecode](https://github.com/eoyilmaz/timecode)
- [openpyxl](https://pypi.org/project/openpyxl/)

## Usage

### EDL Class

This package contains the EDL class and a set of functions that can use an EDL object.

The object can be created by calling the EDL with a filepath and (optionally) a frame rate.

```python
from edltools.core import Edl

path = "./folder/myEdl.edl"
frameRate = 30

newEdl = Edl(path,frameRate)
```

Note that 25FPS is assumed if not otherwise specified.

The following methods can be called on the EDL:

#### exportJson

TODO

#### exportExcel

TODO

```python
```

#### listClips

TODO

#### listFiles

This method returns a list, containing the source file names for each clip, as listed in the EDL. If no source file names are present, raises a ValueError.

#### dumpEffects

TODO

### EDL Functions

In addition, several functions have been included, which interact with the ELD object.

#### edlFileSearchCopy

TO DO

#### edlDupeDetection

TO DO

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

Licenced under [MIT](https://choosealicense.com/licenses/mit/) Licence:

Copyright (c) 2023 Rory Yeung

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## See Also

- [Edl Composer](https://github.com/pietrop/edl-composer) - A Node.js package to create EDLs from objects.
- [Edl to Cdl](https://github.com/walter-arrighetti/edl2cdl/tree/master) - A python project to extract CDL invormation from Edls.
- [Edl Kit](https://github.com/Red5d/edlkit) - A python project to create a video edit using an EDL on Linux.

