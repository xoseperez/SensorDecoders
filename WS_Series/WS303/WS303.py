import binascii


def decodeBytes(bytes):
    print("bytes:", bytes.hex())
    decoded = {}

    i = 0
    while i < len(bytes):
        channel_id = bytes[i]
        channel_type = bytes[i+1]
        i += 2

        # BATTERY
        if channel_id == 0x01 and channel_type == 0x75:
            decoded['battery'] = bytes[i]
            i += 1
        # WATER LEAK DECTECT
        elif channel_id == 0x03 and channel_type == 0x00:
            decoded['leak_status'] = "leak" if bytes[i] else "no leak"
            i += 1
        else:
            break

    print(decoded)
    return decoded


def decodePayload(payload, encoded="base64"):
    if encoded == "base64":
        bytes = binascii.a2b_base64(payload)
    elif encoded == "hex":
        bytes = binascii.a2b_hex(payload)
    else:
        print("unsupport encode type")

    return decodeBytes(bytes)


if __name__ == '__main__':
    decodePayload("AXVkAwAA", "base64")
    decodePayload("017564030001", "hex")