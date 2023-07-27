#!/usr/bin/python3
"""returns employee information about TODO list progress."""

import requests, sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "users/{}/todos".format(user_id)).json()

    completed = [t.get("title") for t in todos if t.get("completed")]
    print("Employee {} is done with tasks({}/{})".format(
        user.get("name"),
        len(completed),
        len(todos))
    )
    [print("\t {}".format(c)) for c in completed]
