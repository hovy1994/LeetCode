class Solution(object):
    def calculateAvailableSeat(self, availableSeat):
        if availableSeat[0] and availableSeat[2]:
            return 2
        elif availableSeat[0] or availableSeat[1] or availableSeat[2]:
            return 1
        else:
            return 0

    def maxNumberOfFamilies(self, n, reservedSeats):
        reservedSeats = sorted(reservedSeats)

        curRow = reservedSeats[0][0]
        reservedRowCount = 1
        availableSeat = [True for i in range(3)]
        result = 0
        for reservedSeat in reservedSeats:
            print("reservedSeat: ", reservedSeat, ", curRow: ", curRow)
            print(
                "availableSeat: ",
                availableSeat,
                ", reservedRowCount: ",
                reservedRowCount,
            )
            if reservedSeat[0] != curRow:
                result += self.calculateAvailableSeat(availableSeat)
                availableSeat = [True for i in range(3)]
                curRow = reservedSeat[0]
                reservedRowCount += 1

            if 2 <= reservedSeat[1] and reservedSeat[1] <= 5:
                availableSeat[0] = False
            if 4 <= reservedSeat[1] and reservedSeat[1] <= 7:
                availableSeat[1] = False
            if 6 <= reservedSeat[1] and reservedSeat[1] <= 9:
                availableSeat[2] = False

        return (
            result
            + (n - reservedRowCount) * 2
            + self.calculateAvailableSeat(availableSeat)
        )