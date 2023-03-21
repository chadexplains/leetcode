class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        units = 0
        for boxes, unit_per_box in boxTypes:
            if truckSize >= boxes:
                units += boxes * unit_per_box
                truckSize -= boxes
            else:
                units += truckSize * unit_per_box
                break
        return units