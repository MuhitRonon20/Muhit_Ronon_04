class Solution:
    def countSeniors(self, details: list[str]) -> int:
        count = 0
        for passenger in details:
            # Extract age from index 11 and 12
            age = int(passenger[11:13])
            if age > 60:
                count += 1
        return count