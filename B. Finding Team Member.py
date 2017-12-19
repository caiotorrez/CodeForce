import sys

def solve(element):
	return dic[element] if element in dic else 0

n = int(raw_input())
seq = [int(i) for i in raw_input().split(' ')]
maior = max(seq)
dic = {}

for e in seq:
	dic[e] = dic[e] + 1 if e in dic else 1

dp = [0] * (maior + 1)
dp[1] = 1 * solve(1)
for i in range(2, maior + 1):
	dp[i] = max(dp[i - 2] + i * solve(i), dp[i - 1])

sys.stdout.write(str(dp[maior]) + '\n')

