# The pcaps/*.pcap files used in this project are sourced from the DeepCSI dataset.
# See: http://researchdata.cab.unipd.it/id/eprint/623 for more details.

# Test PCAP `filtered_4F_0.pcap` file information

The original `4F_0.pcapng` file about 6.44 GB so filtering the file to only include the Compressed Beamforming Report data. The filtered file is saved as `filtered_4F_0.pcap`.

Depends on your CPU, the filtering process may take a while.

```sh
tshark -Y "wlan.vht.compressed_beamforming_report" -r path/to/dataset/4F_0.pcapng -w pcaps/filtered_4F_0.pcap
```

Actual `path/to/dataset/4F_0.pcapng` is `dataset_complete_anonimized/dataset/4F_0.pcapng`.

for example:

```sh
cd path/to/dataset/
tshark -Y "wlan.vht.compressed_beamforming_report" -r 4F_0.pcapng -w ../filtered_4F_0.pcap
```
