nodes = [10, 12, 15, 100]   # times (100 = outlier)
threshold = 20

print("PHASE 1: DRIFT")

valid = []
master = nodes[0]

for t in nodes:
    drift = t - master
    print("Time:", t, "Drift:", drift)

    if abs(drift) <= threshold:
        valid.append(t)
    else:
        print("OUTLIER")

# average
avg = sum(valid) / len(valid)
print("\nAVERAGE:", avg)

print("\nADJUSTMENTS")
for t in nodes:
    print("Adjust:", round(avg - t, 2))

print("\nSYNC DONE")