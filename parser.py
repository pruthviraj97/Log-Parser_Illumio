import csv

LOOKUP_FILE_PATH = "C:\Github\Log-Parser_Illumio\lookup.csv"
FLOW_LOG_FILE_PATH = "C:\Github\Log-Parser_Illumio\\flow_logs.txt"
OUTPUT_FILE_PATH = "C:\Github\Log-Parser_Illumio\output.txt"

lookup_table = {}

#referred http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml
protocol_table = {
    "6" : "tcp",
    "17": "udp",
    "1" : "icmp"
}

with open(LOOKUP_FILE_PATH, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        dstport = row['dstport'].lower()        #case insensitive
        protocol = row['protocol'].lower()      #case insensitive

        lookup_table[(dstport, protocol)] = row['tag']

print(lookup_table)

tag_counts = {}
port_protocol_counts = {}

with open(FLOW_LOG_FILE_PATH, 'r') as file:
    for line in file:
        clean_line = line.strip()  # Remove leading/trailing whitespace, including blank lines
        if not clean_line:  # If the line is empty, skip it
            continue
        column = clean_line.split()
        dstport = column[6]

        #checks the protocol, if we dont have it in the protocol table its unknown
        protocol = protocol_table.get(column[7], "unknown_protocol")

        key = (dstport, protocol)

        # Tag count
        tag = lookup_table.get(key, 'Untagged')
        tag_counts[tag] = tag_counts.get(tag, 0) + 1

        # Port/Protocol count
        port_protocol_counts[key] = port_protocol_counts.get(key, 0) + 1


with open(OUTPUT_FILE_PATH, 'w') as file:
    file.write("Tag,Count\n")
    for tag, count in tag_counts.items():
        file.write(f"{tag},{count}\n")

    file.write("\nPort,Protocol,Count\n")
    for (port, protocol), count in port_protocol_counts.items():
        file.write(f"{port},{protocol},{count}\n")