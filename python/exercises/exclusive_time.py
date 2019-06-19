""" Example problem
Given an array of strings of the form:
[ "1:START:0"
  "2:START:2"
  "2:END:5"
  "1:END:9" ]

Where the first item is the process id, the second is whether the process is starting or ending,
and the third is the time of the action.  Print out a list of the 'exclusive time' spent in each
process id.  Exclusive time is the time spent in that process, but not in a sub-process.  Also note
that calls can be recursive.

"""

test_data = ["1:START:0",
             "2:START:2",
             "2:START:5",
             "2:END:9",
             "2:END:13",
             "1:END:16",
             "3:START:27",
             "3:END:29", ]


def process(data):

    counters = {}
    stack = []
    prev_time = 0

    while len(data) > 0:
        pid, act, time = data.pop(0).split(':')
        if len(stack) == 0 and act == "START":
            prev_time = int(time)
            stack.append(pid)
            continue
        time = int(time)
        delta = time - prev_time
        prev_time = time
        p = stack[-1]
        if p in counters:
            counters[p] += delta
        else:
            counters[p] = delta
        if act == "END":
            stack.pop()
        else:
            stack.append(pid)

    print(counters)


if __name__ == "__main__":
    process(test_data)
