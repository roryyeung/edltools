# EDL Tools

This is a simple set of python tools designed to import a range of EDL (Edit Decision Lists) and EDL-like formats (e.g. AAF) and allow for their manipulation.

The reader functions in this package take an EDL (or EDL-like file), and returns an object of class EDL. This object contains a range of methods, to allow the data contained to be manipulated or outputted.

Note that this class assumes a frame rate of 25FPS, unless otherwise specified.

In addition, we have created a similar class for ALEs - a similar avid based format for storage of bin metadata.

Potential use cases for this package include converting EDLs to Excel, performing file searches for all files contained within an EDL/ALE, and providing a bridge between NLE (Non-Linear Editing) software and third-party tools.

## About EDLs

WRITE MORE

Edit Decision Lists are a way of exporting 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install EDL Tools.

```bash
pip install edltools
```

NOT YET IMPLEMENTED

## Dependencies

This package requires the following depencencies:

- Timecode

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

TODO

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

PLACEHOLDER

[MIT](https://choosealicense.com/licenses/mit/)