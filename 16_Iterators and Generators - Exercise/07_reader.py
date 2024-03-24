def read_next(*args):
    for seq in args:
        # Option 1
        # for el in seq:
        #     yield el

        # Option 2
        yield from seq
