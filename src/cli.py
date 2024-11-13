import os
import argparse
from src.extract import process_pcap

def main():
    parser = argparse.ArgumentParser(description="extract Compressed Beamforming Data from PCAP file")

    parser.add_argument("input", help="Input .pcap or .pcapng file path or directory", type=str)
    parser.add_argument("-d", "--dir", action="store_true", help="Treat the input as a directory and process all .pcap and .pcapng files")
    parser.add_argument('-W', '--write', help="Write the extracted data as JSON file", type=str)

    args = parser.parse_args()

    result = f"Processing {args.input} and generating output..."
    print(result)

    if args.dir:
        if os.path.isdir(args.input):
            for root, _, files in os.walk(args.input):
                for file in files:
                    if file.endswith(".pcap") or file.endswith(".pcapng"):
                        file_path = os.path.join(root, file)

                        cbr_list, cbr_len = process_pcap(file_path)

                        print(cbr_list)
                        print(f"Report Length: {cbr_len}")
        else:
            print(f"Error: {args.input} is not a valid directory.")
    else:
        if os.path.isfile(args.input) and (args.input.endswith(".pcap") or args.input.endswith(".pcapng")):
            cbr_list, cbr_len = process_pcap(args.input)

            print(cbr_list)
            print(f"Report Length: {cbr_len}")
        else:
            print(f"Error: {args.input} is not a valid pcap or pcapng file.")

if __name__ == "__main__":
    main()
