def citations(nums):
	nums.sort(reverse = True)
	ans = 0
	for i, val in enumerate(nums):
		if i<val:ans += 1
	return ans

if __name__ == "__main__":
	t = int(input("enter number of testcases:\n"))
	while t:
		nums = list(map(int, input().split()))
		ans = citations(nums)
		print(ans)
		t-=1