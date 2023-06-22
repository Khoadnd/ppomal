# Data distribution

| Type       | Count Train | Count Test |
| ---------- | ----------- | ---------- |
| Benign     | 700         | 300        |
| Locker     | 231         | 99         |
| Mediyes    | 1015        | 435        |
| Winwebsec  | 3080        | 1320       |
| Zbot       | 1470        | 630        |
| Zeroaccess | 483         | 207        |

Take 100 from each type from train set and split 50 for train, 50 for test adversarial set.

# Final data distribution

| Type       | Count Train | Count Test | Count Train RL | Count Test RL |
| ---------- | ----------- | ---------- | -------------- | ------------- |
| Benign     | 700         | 300        | 0              | 0             |
| Locker     | 131         | 99         | 50             | 50            |
| Mediyes    | 915         | 435        | 50             | 50            |
| Winwebsec  | 2980        | 1320       | 50             | 50            |
| Zbot       | 1370        | 630        | 50             | 50            |
| Zeroaccess | 383         | 207        | 50             | 50            |