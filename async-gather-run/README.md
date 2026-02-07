# The Setup
## **Imagine you need to build a dashboard that displays:**

1. *The Weather (takes ~2 seconds to load)*
2. *Stock Prices (takes ~1.5 seconds to load)*
3. *News Headlines (takes ~3 seconds to load)*

### **You will write two versions of this script to see the difference.**

```bash
sergiu async-gather-run $ python3 main.py
1. Fetching Weather... waiting
   -> Weather received!
2. Fetching Stocks... waiting
   -> Stocks received!
3. Fetching News... waiting
   -> News received!

 All data collected:
1. Sunny, 72°F
2. AAPL: $150
3. Python 4.0 released!
Total time: 6.51 second

1. Fetching Weather... waiting
2. Fetching Stocks... waiting
3. Fetching News... waiting
   -> Stocks received!
   -> Weather received!
   -> News received!

 All data collected:
1. Sunny, 72°F
2. AAPL: $150
3. Python 4.0 released!
Total time: 3.00 second
```

