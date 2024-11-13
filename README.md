# Compressed Beamforming Extractor

## Overview

This tool extracts the Compressed Beamforming Report data from a PCAP file and saves it to a JSON or CSV file.

## Dependencies

```plaintext
python >= 3.9
wireshark >= 4.4.0
```

## Usage

```sh
cbrext test/pcaps/beamforming.pcap -W test_out.json
```

### Options

```plaintext
-h,  --help                     Show this help message and exit

-d,  --dir                      Extract all PCAP files in a directory
-W,  --write    <file or dir>   Write the extracted data to a file

-sa, --src-addr <wlan.sa>       Filter by source address
-su, --single                   Extract SU
-mu, --multi                    Extract MU

-j,  --json                     Write the extracted data to a JSON file (default)
-c,  --csv                      Write the extracted data to a CSV file
-b,  --binary                   Decode the CBR hex to binary
-i,  --info                     Include the decoded CBR info

-v,  --verbose                  Print verbose output
```

## Development

### Installation

```sh
python -m pip install .
```

### Updating

```sh
python -m pip install --upgrade .
```

### Testing

```sh
python -m unittest discover -s tests
```

### Uninstalling

```sh
python -m pip uninstall cbrext
```

## Citation

Meneghello, Francesca, Rossi, Michele, and Restuccia, Francesco. "DeepCSI: Rethinking Wi-Fi Radio Fingerprinting Through MU-MIMO CSI Feedback Deep Learning." In IEEE International Conference on Distributed Computing Systems, 2022.

See: https://github.com/francescamen/DeepCSI for more details.
