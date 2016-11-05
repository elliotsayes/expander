## Expander
"File Expansion" software written in python 3. Like file compression software, but the other way around.

### Usage
    Usage: expand.py [-h] [-e <filename> <N> | -u <filename>]
    -h : show this help
    -e : expand file (N = expansion code)
    -u : unexpand file
Run with no arguments for interactive mode

### What?
Takes in input file name from the [/files/examples](/files/examples) folder, and makes it bigger. The output is placed in the [/files/expanded](/files/expanded) folder.
The process is reversable. You can take a big file from the [/files/expanded](/files/expanded) folder and unexpand it. The output is placed in the [/files/unexpanded](/files/unexpanded) folder.

### How?
Each byte in the file is expanded to be `R` (the expansion ratio) times bigger. `R` must be calculable from the equation `R = 2^N`, where `N` (the expansion code) is an integer between 0 and 255 inclusive. Therefore `R` can be as low as 1 and up to 57 quattuorvigintillion 896 trevigintillion 44 duovigintillion 618 unvigintillion 658 vigintillion 97 novemdecillion 711 octodecillion 785 septendecillion 492 sexdecillion 504 quindecillion 343 quattuordecillion 953 tredecillion 926 duodecillion 634 undecillion 992 decillion 332 nonillion 820 octillion 282 septillion 19 sextillion 728 quintillion 792 quadrillion 3 trillion 956 billion 564 million 819 thousand 969. This application supports up to about `N = 25` before python starts throwing overflow errors, but that's a ratio of 33554432, or enough to turn this Readme into about 75 GiB.

The expansion code `N` is written to the first byte of the  expanded file. The rest of the file consists of each of the bytes in the input file expanded by ratio `R`. The expansion process for a byte `B` is simply to fill the first `R-1` bytes with random data, and set the last byte to `(B-S)%256` (where `S` is the sum of all the previous bytes). This makes the equation `B = S%256` work.

The unexpansion process starts by reading the first byte in the expanded file to find `N`, then calculate `R` through the equation `R = 2^N`. The expanded file is then read in in groups of `R` bytes, and the original byte is calculated from the sum of these bytes using the formula `B = S%256` (where S is the sum, B is the original byte).

### Why?
Useful if you want to waste someone else's (and your own) bandwidth to transfer a file, dial-up simulator. Other than that I don't know, for fun?
