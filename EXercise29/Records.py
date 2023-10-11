import random

class RecordGenerator:
    def __init__(self, initial_dst_ip1, initial_dst_ip2):
        self.dst_ip1 = initial_dst_ip1
        self.dst_ip2 = initial_dst_ip2

    def generate_record(self, state):
        src_ip = '10.1.2.3'
        sport = random.randint(1024, 65535)
        dport = random.randint(1024, 65535)

        record = f"[{state}] tcp 6 120 {state} src={src_ip} dst={self.dst_ip1} sport={sport} dport={dport} [{state}] src={self.dst_ip1} dst={self.dst_ip2} sport={dport} dport={sport} helper=ftp\n"
        return record

    def generate_records(self, num_records):
        records = []
        for _ in range(num_records):
            state = random.choice(['SYN_SENT', 'SYN_RECV', 'ESTABLISHED'])
            record = self.generate_record(state)
            records.append(record)

            # Update dst_ip1 and dst_ip2 based on the last digits
            last_digit1 = int(self.dst_ip1.split('.')[-1])
            last_digit2 = int(self.dst_ip2.split('.')[-1])
            self.dst_ip1 = '.'.join(self.dst_ip1.split('.')[:-1] + [str(last_digit1 + 1 + random.randint(1, 5))])
            self.dst_ip2 = '.'.join(self.dst_ip2.split('.')[:-1] + [str(last_digit2 + 1 + random.randint(1, 5))])

        return records

    def write_records_to_file(self, filename, input_records, generated_records):
        with open(filename, 'w') as f:
            f.writelines(input_records + generated_records)

if __name__ == "__main__":
    # Provided input records
    input_records = [
        "[NEW] tcp 6 120 SYN_SENT src=10.1.2.3 dst=203.0.113.47 sport=47800 dport=21 [UNREPLIED] src=203.0.113.47 dst=198.51.100.32 sport=21 dport=47800 helper=ftp",
        "[UPDATE] tcp 6 60 SYN_RECV src=10.1.2.3 dst=203.0.113.47 sport=47800 dport=21 src=203.0.113.47 dst=198.51.100.32 sport=21 dport=47800 helper=ftp",
        "[UPDATE] tcp 6 432000 ESTABLISHED src=10.1.2.3 dst=203.0.113.47 sport=47800 dport=21 src=203.0.113.47 dst=198.51.100.32 sport=21 dport=47800 [ASSURED] helper=ftp"
    ]

    # Create an instance of the RecordGenerator class
    generator = RecordGenerator('203.0.113.47', '198.51.100.32')

    # Generate 1000 records
    records_to_generate = 1000
    generated_records = generator.generate_records(records_to_generate)

    # Write records to a file
    generator.write_records_to_file('output_records.txt', input_records, generated_records)

    print("Records generated and written to 'output_records.txt'")
