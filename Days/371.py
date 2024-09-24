# Question 371

# You're designing a smart laundry sorting system.
# You have a list of clothing items, each with a
# color and a fabric type. Sort these items into
# the minimum number of loads n and return n,
# where items of the same color can be washed
# together, and some different fabric types
# cannot be mixed together. "Normal" fabric
# types can be mixed with "heavy", but
# "delicate" cannot be mixed with anything.


from collections import defaultdict

fabric_sorter = {
    "normal": 0,  # N
    "heavy": 1,  # H
    "delicate": 2,  # D
}


def minLaundryLoads(load) -> int:
    # fabric types                N  H  D
    legend = defaultdict(lambda: [0, 0, 0])

    for C, F in load:
        legend[C][fabric_sorter[F]] += 1

    T = 0

    for [N, H, D] in legend.values():
        if N or H:
            T += 1
        if D:
            T += 1

    return T


def main():
    # Test Case 1: Provided example
    load1 = [
        ["red", "normal"],
        ["blue", "normal"],
        ["red", "delicate"],
        ["blue", "heavy"],
    ]
    assert minLaundryLoads(load1) == 3

    # Test Case 2: Provided example
    load2 = [
        ["white", "normal"],
        ["white", "delicate"],
        ["white", "normal"],
        ["white", "heavy"],
    ]
    assert minLaundryLoads(load2) == 2

    # Test Case 3: All items same color, different fabric types
    load3 = [
        ["green", "normal"],
        ["green", "delicate"],
        ["green", "heavy"],
    ]
    # Should return 2: one for normal + heavy, and one for delicate
    assert minLaundryLoads(load3) == 2

    # Test Case 4: All items same fabric type, different colors
    load4 = [
        ["green", "normal"],
        ["red", "normal"],
        ["blue", "normal"],
    ]
    # Should return 3: each color has its own load
    assert minLaundryLoads(load4) == 3

    # Test Case 5: Same color with mixable fabrics
    load5 = [
        ["yellow", "normal"],
        ["yellow", "heavy"],
    ]
    # Should return 1: normal + heavy can be washed together
    assert minLaundryLoads(load5) == 1

    # Test Case 6: All delicate fabrics, different colors
    load6 = [
        ["red", "delicate"],
        ["blue", "delicate"],
        ["yellow", "delicate"],
    ]
    # Should return 3: delicate fabrics cannot be mixed, even if colors are different
    assert minLaundryLoads(load6) == 3

    # Test Case 7: Mixed delicate and normal/heavy fabrics
    load7 = [
        ["purple", "normal"],
        ["purple", "delicate"],
        ["purple", "heavy"],
        ["black", "normal"],
        ["black", "heavy"],
        ["black", "delicate"],
    ]
    # Should return 4:
    # - "purple" load for normal + heavy
    # - "purple" load for delicate
    # - "black" load for normal + heavy
    # - "black" load for delicate
    assert minLaundryLoads(load7) == 4

    # Test Case 8: Complex color and fabric combinations
    load8 = [
        ["orange", "normal"],
        ["orange", "delicate"],
        ["orange", "heavy"],
        ["blue", "delicate"],
        ["blue", "heavy"],
        ["blue", "normal"],
        ["orange", "normal"],
    ]
    # Should return 4:
    # - "orange" load for normal + heavy
    # - "orange" load for delicate
    # - "blue" load for normal + heavy
    # - "blue" load for delicate
    assert minLaundryLoads(load8) == 4

    print("All test cases passed!")


if __name__ == "__main__":
    main()
