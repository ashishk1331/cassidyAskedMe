# Question 365

# Given an array of logs and variable assignments,
# return a list of all unused variables.

from collections import defaultdict


def findUnused(cmds):
    dmap = defaultdict(list)
    dmap["log"] = []

    declared = set()

    for cmd in cmds:
        if cmd.startswith("log"):
            var = cmd[cmd.index("(") + 1 : cmd.index(")")]
            dmap["log"].append(var)
        else:
            left, right = cmd.split(" = ")
            declared.add(left)
            if right.isalpha():
                dmap[left].append(right)

    used = set()

    def dfs(var):
        if var in used:
            return

        used.add(var)

        if var in dmap:
            for dependency in dmap[var]:
                dfs(dependency)

    for var in dmap["log"]:
        if var not in used:
            dfs(var)

    unused = list(declared - used)
    unused.sort()

    return unused


def main():
    # test cases given in the newsletter
    assert findUnused(["a = 1", "b = a", "c = 2", "log(b)"]) == ["c"]
    assert findUnused(["a = 1", "b = a", "c = 2", "log(c)"]) == ["a", "b"]

    # chatgpt-generated test cases

    # Case where all variables are used in logs
    assert findUnused(["a = 1", "b = a", "log(a)", "log(b)"]) == []

    # Case with a variable defined but not used at all
    assert findUnused(["x = 5", "y = x + 1", "z = y", "log(y)"]) == ["x", "z"]

    # Case where only one variable is defined and used
    assert findUnused(["a = 100", "log(a)"]) == []

    # Case with multiple unused variables
    assert findUnused(["a = 3", "b = 4", "c = 5", "log(b)"]) == ["a", "c"]

    # Case where all variables are defined but none are used in logs
    assert findUnused(["m = 10", "n = 20", "o = 30"]) == ["m", "n", "o"]

    # Case where a variable is used in multiple logs
    assert findUnused(["p = 15", "q = 25", "log(p)", "log(p)", "log(p)"]) == ["q"]

    # Case with nested variable usage
    assert findUnused(["u = 7", "v = u * 2", "w = v + 3", "log(w)"]) == ["u", "v"]

    # Case with no variables defined
    assert findUnused(["log(1)", "log(2)"]) == []

    # Case with complex expressions
    assert findUnused(["a = 5", "b = a + 10", "c = b * 2", "log(c)"]) == ["a", "b"]

    # Case with a mix of used and unused variables
    assert findUnused(["x = 100", "y = x * 2", "z = y + 50", "log(y)", "log(z)"]) == [
        "x"
    ]


if __name__ == "__main__":
    main()
