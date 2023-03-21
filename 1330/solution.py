def filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance):
    filtered = []
    for r in restaurants:
        if (not veganFriendly or r[2] == 1) and r[3] <= maxPrice and r[4] <= maxDistance:
            filtered.append(r[0])
    return sorted(filtered, key=lambda x: (-restaurants[x-1][1], -x))