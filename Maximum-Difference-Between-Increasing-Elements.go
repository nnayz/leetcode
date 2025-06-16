func maximumDifference(nums []int) int {
    minNum := math.MaxInt32
    maxDiff := -1
    for _, num := range nums {
        if num <= minNum {
            minNum = num
        } else {
            if num - minNum > maxDiff {
                maxDiff = num - minNum
            }
        }
    }
    return maxDiff
}