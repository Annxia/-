def progress_weeks(mileWeeks):
    times = 0
    idx = 0
    for mile in mileWeeks:
        if idx == 0:
            idx += 1
            continue

        if mile > mileWeeks[idx-1]:
            times += 1

        idx += 1

    return times


t = progress_weeks([3,4,1,2])
print(t)