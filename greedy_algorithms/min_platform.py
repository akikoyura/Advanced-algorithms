def min_platform(arrival, departure):
    """
    :param: arrival - list of arrival time
    :param: departure - list of departure time
    """
    if len(arrival) != len(departure):  # Mismatch in the length of the lists
        return -1
    # Sort both the lists
    arrival.sort()
    arrival.sort()

    platform_required = 1  # Count of platforms required the moment when comparing ith arrival and jth departure
    max_platform_required = 1  # keep track of the max value of platform_required

    # Iterate such (i-j) will represent platform_required at that moment
    i = 1
    j = 0

    # Traverse the arrival list wit iterator `i` and departure with iterator `j`
    while i < len(arrival) and j < len(departure):
        # if ith arrival is scheduled before than jth departure.
        # increment platform_required and i as well

        if arrival[i] < departure[j]:
            platform_required += 1
            i += 1

            # Update the max value of platform_required
            if platform_required > max_platform_required:
                max_platform_required = platform_required
        else:
            platform_required -= 1
            j += 1

    return max_platform_required


def test_function(test_case):
    arrival = test_case[0]
    departure = test_case[1]
    solution = test_case[2]

    output = min_platform(arrival, departure)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    arrival = [900, 940, 950, 1100, 1500, 1800]
    departure = [910, 1200, 1120, 1130, 1900, 2000]
    test_case = [arrival, departure, 3]

    test_function(test_case)

    arrival = [200, 210, 300, 320, 350, 500]
    departure = [230, 340, 320, 430, 400, 520]
    test_case = [arrival, departure, 2]
    test_function(test_case)
