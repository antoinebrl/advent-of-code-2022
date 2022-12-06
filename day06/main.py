import os


def parse(filename):
    with open(filename) as f:
        return f.read()

def first_packet(stream, marker_size=4):
    for i in range(len(stream) - marker_size):
        packet = stream[i:i+marker_size]
        if len(packet) == len(set(packet)):
            return i + marker_size


if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(__file__),  "input.txt")
    datastream = parse(input_file)

    solution1 = first_packet(datastream)
    print(f"part 1 - solution : {solution1}")

    solution2 = first_packet(datastream, marker_size=14)
    print(f"part 2 - solution : {solution2}")
