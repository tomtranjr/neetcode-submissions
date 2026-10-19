class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # stack
        # create a zipped list of position and speed
        # sort by position descending
        # init stack
        # init res
        # append the current time to target given position and speed
        # for next car, if TtT is less than stack, they will become fleet, res += 1
        # otherwise its more so we add it to the stack

        stack = []

        cars = [(position, speed) for position, speed in zip(position, speed)]
        cars.sort(reverse=True)

        for position, speed in cars:
            time = (target - position) / speed
            stack.append(time)

            if len(stack) >= 2 and time <= stack[-2]:
                stack.pop()

        return len(stack)