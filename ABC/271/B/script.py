num_count, query_count = map(int, input().split())

numbers = {}
for i in range(num_count):
    tmp_n = list(map(int, input().split()))[1::]
    numbers[i] = tmp_n

queries = []
for i in range(query_count):
    tmp_q = list(map(int, input().split()))
    queries.append(tmp_q)

for q in queries:
    print(numbers[q[0] - 1][q[1] - 1])
