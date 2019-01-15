in_ = input()

for i in range(len(in_) // 10):
    print(in_[(i * 10) : (i * 10) + 10])

print(in_[len(in_) // 10 * 10 : ])
