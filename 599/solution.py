class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        restaurant_indices = {restaurant: i for i, restaurant in enumerate(list1)}
        min_index_sum = float('inf')
        common_restaurants = []
        for i, restaurant in enumerate(list2):
            if restaurant in restaurant_indices:
                index_sum = i + restaurant_indices[restaurant]
                if index_sum < min_index_sum:
                    min_index_sum = index_sum
                    common_restaurants = [restaurant]
                elif index_sum == min_index_sum:
                    common_restaurants.append(restaurant)
        return common_restaurants