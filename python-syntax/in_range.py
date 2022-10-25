def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """
    for num in nums:
      # if the lowest value is lowers than our number 
      # and highest number is highest than our num we are set to fits into num
         if (lowest <= num) and (highest >= num):
            print(f"{num} fits")


in_range([10, 20, 30, 40, 50], 15, 30)            
