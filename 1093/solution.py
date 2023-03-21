class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        min_val = 256
        max_val = -1
        sum_val = 0
        count_val = 0
        mode_val = 0
        mode_count = 0
        for i in range(256):
            if count[i] > 0:
                min_val = min(min_val, i)
                max_val = max(max_val, i)
                sum_val += i * count[i]
                count_val += count[i]
                if count[i] > mode_count:
                    mode_count = count[i]
                    mode_val = i
        mean_val = sum_val / count_val
        median_val = 0
        median_count = count_val // 2
        if count_val % 2 == 0:
            found_first = False
            for i in range(256):
                median_count -= count[i]
                if not found_first and median_count <= 0:
                    median_val += i
                    found_first = True
                elif found_first and median_count <= 0:
                    median_val += i
                    return [min_val, max_val, mean_val, median_val / 2, mode_val]
        else:
            for i in range(256):
                median_count -= count[i]
                if median_count <= 0:
                    median_val = i
                    return [min_val, max_val, mean_val, median_val, mode_val]
        return [min_val, max_val, mean_val, median_val, mode_val]