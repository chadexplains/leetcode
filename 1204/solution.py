def find_last_person(people, limit):
    people.sort(reverse=True)
    weight_sum = 0
    for i, person in enumerate(people):
        weight_sum += person[0]
        if weight_sum > limit:
            return i - 1
    return len(people) - 1