import subprocess
import json

def process_pcap(file_path):
    try:
        result = subprocess.run(
            ["tshark", "-r", file_path, "-T", "json"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )

        json_data = json.loads(result.stdout)

        values = []
        for packet in json_data:
            if "_source" in packet and "layers" in packet["_source"]:
                layers = packet["_source"]["layers"]

                if "wlan.mgt" in layers:
                    compressed_beamforming_report = layers["wlan.mgt"]["Fixed parameters"]["wlan.vht.compressed_beamforming_report"] # wlan.vht.compressed_beamforming_report
                    ncindex = layers["wlan.mgt"]["Fixed parameters"]['wlan.vht.mimo_control.control_tree']['wlan.vht.mimo_control.ncindex'] # wlan.vht.mimo_control.ncindex
                    nrindex = layers["wlan.mgt"]["Fixed parameters"]['wlan.vht.mimo_control.control_tree']['wlan.vht.mimo_control.nrindex'] # wlan.vht.mimo_control.nrindex

                    reportlen = len(compressed_beamforming_report)
                    nc = int(ncindex, 16) + 1
                    nr = int(nrindex, 16) + 1
                    min_antenna = min(nc, nr)

                    # for resolve wireshark bug
                    # if reportlen == 2993:
                    #     pass
                    # if reportlen == 3005:
                    #     compressed_beamforming_report = compressed_beamforming_report[:2993]
                    #     reportlen = 2993

                    values.append(compressed_beamforming_report)

                    # for resolve wireshark bug
                    # if curlen == -1:
                    #     curlen = reportlen
                    # elif curlen != reportlen:
                    #     pass

        return values, reportlen

    except Exception as e:
        print(f"Error: {e}")
        return []