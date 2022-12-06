def get_marker(datastream, step):
    for i in range(len(datastream)):
        if len(set(datastream[i:i+step])) == step:
            return i + step

with open('input.txt') as f:
    datastream = f.readline()
    packet_marker = get_marker(datastream, 4)
    message_marker = get_marker(datastream, 14)

    print(packet_marker)
    print(message_marker)