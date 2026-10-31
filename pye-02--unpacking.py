"""Programmer: python_scripts (Abhijith Warrier)
PYTHON EVERYDAY — Unpacking: Less Indexing, Clearer Code

Replace repeated positional lookups with meaningful names, collect remaining
values with a starred target, and recognize length mismatches. These runnable
examples use tuples and lists; no external packages are required.
"""


def main():
    # 1. Before: three positional lookups for one fixed-shape record.
    row = ("Asha", 92, "Kochi")
    name = row[0]
    score = row[1]
    city = row[2]
    before = (name, score, city)

    # After: unpack in iteration order. Names do not select fields by meaning.
    name, score, city = row
    print(f"Record: {name} | {score} | {city}")
    assert (name, score, city) == before == row

    # 2. A starred target collects remaining items into a NEW list.
    scores = (92, 85, 88, 96)
    first, *rest = scores
    print(f"First: {first} | Rest: {rest}")
    assert first == 92 and rest == [85, 88, 96]
    assert isinstance(rest, list)  # Even though the source is a tuple.

    # No remaining values is valid when all ordinary targets are satisfied.
    only, *empty_rest = (92,)
    print(f"Only: {only} | Rest: {empty_rest}")
    assert only == 92 and empty_rest == []

    # 3. The star may be in the middle; one star per unpacking level.
    first, *middle, last = scores
    print(f"Endpoints: {first}, {last} | Middle: {middle}")
    assert (first, middle, last) == (92, [85, 88], 96)
    assert scores == (92, 85, 88, 96)  # The input was not changed.
    first, *middle, last = (92, 96)
    assert middle == []

    # 4. Exact unpacking rejects both too many and too few values.
    for values in [(1, 2, 3), (1,)]:
        try:
            left, right = values
        except ValueError:
            print(f"Exact unpacking {values}: ValueError")
        else:
            raise AssertionError("Expected a length mismatch")

    # A star does not remove the need to supply the ordinary targets.
    try:
        first, *middle, last = (92,)
    except ValueError:
        print("Two endpoints from one value: ValueError")
    else:
        raise AssertionError("Two ordinary targets require at least two values")

    # Unpacking is positional; wrong field names do not validate the record.
    city, score, name = row
    assert city == "Asha" and name == "Kochi"
    print("All demonstration checks passed.")


if __name__ == "__main__":
    main()
