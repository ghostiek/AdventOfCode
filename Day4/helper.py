def get_ranges_set(elf):
    nums = elf.split("-")
    result = range(int(nums[0]), int(nums[1])+1)
    return set(result)