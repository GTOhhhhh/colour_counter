# Colour Counter
A simple app which lets the user upload a PNG image file, converts it to a greyscale image with a 256 colorspace then
counts the number of coloured areas.

Additionally, the `count_areas.py` service may be ran as a standalone script to process an array of unsigned 256 
integers as explained below.

# Installing
Requires Linux/OSX and Python 3.5 or higher. 

1. Install dependencies (`pip3 install -r requirements`)
2. Run (`python3 app.py`)
3. Open [http://localhost:5000](http://localhost:5000)

To run `count_areas.py` as a command line script:

1. `cd services` from the root directory
2. `chmod +x count_areas.py`
3. Run `count_areas.py <input-filename> --shape <height>,<width>` - e.g. `./count_areas.py sample.bin --shape 256,256`

or simply:
1. `cd services` from the root directory
2. `python3 count_areas.py <input-filename> --shape <height>,<width>` - e.g `python3 colour_counter.py sample.bin --shape 256,256`
