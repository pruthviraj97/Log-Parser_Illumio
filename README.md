# Log-Parser_Illumio

## Running the code instructions
1) Download/Clone the files in local folder
2) You can replace the flow_log.txt file with the log file required
3) You can update the lookup.csv table if more combinations are needed
4) Run the parser.py python program, with an IDE or `python parser.py`
 
## Assumption and Declarations
1)  The program only supports default log format, not custom and the only version that is supported is 2. (https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html)

2) The below dictionary in code contains the protocols our program recognizes, if any other protocol number is present in the log file, its protocol is defaulted to **unknown_protocol**. We can add protocols needed to this dictionary (link I used - http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)

`protocol_table = {
    "6" : "tcp",
    "17": "udp",
    "1" : "icmp"
}`

3) File Paths can be changed as needed
`LOOKUP_FILE_PATH = "C:\Github\Log-Parser_Illumio\lookup.csv"
FLOW_LOG_FILE_PATH = "C:\Github\Log-Parser_Illumio\\flow_logs.txt"
OUTPUT_FILE_PATH = "C:\Github\Log-Parser_Illumio\output.txt"`

## Implementation
1) Read `lookup.csv` and create a lookup_table dictionary containing all `(dstpost, protocol)` combinations with value as its tag
2) Read `flow_logs.txt` file line by line , split it with delimiter . Part 6 corresponds to `dstport` and part 7 corresponds to `protocol`
3) Create key `(dstport, protocol)` search in lookup table for tag, if not found tag == Untagged
4) Increment the count in the output dictionaries `tag_counts` and `port_protocol_counts`
5) Iterate through the key value pairs in these dictionaries and write in the file `output.txt`

## Analysis
1) Code can handle tag mappings are plain text (ascii) files
2) As we are reading logs line by line , no issue of log file being too big, as only a single line is present in the memory and processed at a time
3) We are converting all the mappings into dictionary line by line. So the Time complexity to check a combination becomes O(1)
4) Tags can have multiple combinations as dstport, protocol is used as the key for the lookup table dictionary
5) Taken care of converting each value to lowercase to make it case insensitive.

## Test
1) Tested with protocol number not in protocol+table
2) Tested memory usage for large number of logs
3) Tested for case insensitiveness
4) Tested Time of execution for large number of lookups
