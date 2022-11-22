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
        # VALVE 1
        elif channel_id == 0x03 and channel_type == 0x01:
            decoded['valve1'] = "on" if bytes[i] else "off"
            i += 1
        # VALVE 2
        elif channel_id == 0x05 and channel_type == 0x01:
            decoded['valve2'] = "on" if bytes[i] else "off"
            i += 1
        # VALVE 1 Pulse
        elif channel_id == 0x04 and channel_type == 0xc8:
            decoded['valve1_pulse'] = int.from_bytes(bytes[i:i + 4], 'little', signed=False)
            i += 4
        # VALVE 2 Pulse
        elif channel_id == 0x06 and channel_type == 0xc8:
            decoded['valve2_pulse'] = int.from_bytes(bytes[i:i + 4], 'little', signed=False)
            i += 4
        # GPIO 1
        elif channel_id == 0x07 and channel_type == 0x01:
            decoded['gpio_1'] = "on" if bytes[i] else "off"
            i += 1
        # GPIO 2
        elif channel_id == 0x08 and channel_type == 0x01:
            decoded['gpio_2'] = "on" if bytes[i] else "off"
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
    decodePayload("AwEABMgAAAAABQEABsgAAAAA", "base64")
    decodePayload("03010004c80000000005010006c800000000", "hex")
