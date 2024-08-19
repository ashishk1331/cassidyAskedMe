"""
Question 366

Given an array of function logs, where each log
consists of a function name, a timestamp, and an
event (either start or end), return the total 
execution time for each function. The timestamp 
is an integer representing milliseconds since 
the start of the program.
"""


def calculateExecutionTimes(events):
    result = {}

    for event in events:
        name, time, event_type = event.values()
        if event_type == "start":
            result[name] = time
        else:
            result[name] = time - result[name]

    return result


def main():
    # Test Case 1: Nested Functions with Overlapping Times
    tasks = [
        {"name": "main", "time": 0, "event": "start"},
        {"name": "subTask1", "time": 5, "event": "start"},
        {"name": "subTask1", "time": 10, "event": "end"},
        {"name": "subTask2", "time": 15, "event": "start"},
        {"name": "subTask2", "time": 20, "event": "end"},
        {"name": "main", "time": 25, "event": "end"},
    ]
    assert calculateExecutionTimes(tasks) == {"main": 25, "subTask1": 5, "subTask2": 5}

    # Test Case 2: Single Function with No Subtasks
    tasks = [
        {"name": "main", "time": 0, "event": "start"},
        {"name": "main", "time": 10, "event": "end"},
    ]
    assert calculateExecutionTimes(tasks) == {"main": 10}

    # Test Case 3: Multiple Functions with Overlapping Times
    tasks = [
        {"name": "main", "time": 0, "event": "start"},
        {"name": "subTask1", "time": 2, "event": "start"},
        {"name": "subTask1", "time": 5, "event": "end"},
        {"name": "subTask2", "time": 7, "event": "start"},
        {"name": "subTask2", "time": 9, "event": "end"},
        {"name": "main", "time": 10, "event": "end"},
    ]
    assert calculateExecutionTimes(tasks) == {"main": 10, "subTask1": 3, "subTask2": 2}

    # Test Case 4: Nested Subtasks
    tasks = [
        {"name": "main", "time": 0, "event": "start"},
        {"name": "subTask1", "time": 2, "event": "start"},
        {"name": "subTask2", "time": 3, "event": "start"},
        {"name": "subTask2", "time": 6, "event": "end"},
        {"name": "subTask1", "time": 8, "event": "end"},
        {"name": "main", "time": 10, "event": "end"},
    ]
    assert calculateExecutionTimes(tasks) == {"main": 10, "subTask1": 6, "subTask2": 3}

    # Test Case 5: Multiple Functions with No Overlap
    tasks = [
        {"name": "main", "time": 0, "event": "start"},
        {"name": "main", "time": 3, "event": "end"},
        {"name": "subTask1", "time": 5, "event": "start"},
        {"name": "subTask1", "time": 8, "event": "end"},
        {"name": "subTask2", "time": 10, "event": "start"},
        {"name": "subTask2", "time": 13, "event": "end"},
    ]
    assert calculateExecutionTimes(tasks) == {"main": 3, "subTask1": 3, "subTask2": 3}

    # Test Case 6: Function Ends Before Another Starts
    tasks = [
        {"name": "main", "time": 0, "event": "start"},
        {"name": "main", "time": 3, "event": "end"},
        {"name": "subTask1", "time": 4, "event": "start"},
        {"name": "subTask1", "time": 7, "event": "end"},
    ]
    assert calculateExecutionTimes(tasks) == {"main": 3, "subTask1": 3}

    # Test Case 7: Functions with Same Start and End Time
    tasks = [
        {"name": "main", "time": 0, "event": "start"},
        {"name": "main", "time": 0, "event": "end"},
        {"name": "subTask1", "time": 5, "event": "start"},
        {"name": "subTask1", "time": 5, "event": "end"},
    ]
    assert calculateExecutionTimes(tasks) == {"main": 0, "subTask1": 0}


if __name__ == "__main__":
    main()
