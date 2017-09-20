import argparse

def calc_gc_percent(seq):
    """
    Calculates the GC percentage of the given sequence.

    Arguments:
        - seq - the input sequence (string).

    Returns:
        - GC percentage (float).

    The returned value is always <= 100.0
    """
    at_count, gc_count = 0, 0
    for char in seq.upper():
        if char in ('A', 'T'):
            at_count += 1
        elif char in ('G', 'C'):
            gc_count += 1
        else:
            raise ValueError("Unecpected characther found: {}. Only ACTGs are allowed." .format(char))

# Corner case handling: empty input sequence.
    try:
        return gc_count * 100.0 / (gc_count + at_count)
    except ZeroDivisionError:
        return 0.0
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', type=str, choices=['file', 'text'], help="Input type of script")
    parser.add_argument('value', type=str, help="Input value of script")
    args = parser.parse_args()
    print "The sequence {} has a %GC of {:.2f}".format(args.Input_seq,
                  calc_gc_percent(args.Input_seq))

    if args.mode == 'file':
        try:
            f = open(args.value, 'r')
            for line in f:
                seq = line.strip()
                gc = calc_gc_percent(seq)
                print message.format(seq, gc)
        finally:
            f.close()
    else:
        seq = args.value
        gc = calc_gc_percent(seq)
        print message.format(seq, gc)