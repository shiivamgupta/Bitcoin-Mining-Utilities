# Take inputs from user
hashrate_th = float(input("Enter miner's hashrate in TH/s: "))
efficiency_j_per_th = float(input("Enter miner's efficiency in J/TH: "))
electricity_rate_usd_per_kwh = float(input("Enter electricity rate in USD per kWh: "))

# Calculate power in watts
power_watts = hashrate_th * efficiency_j_per_th

# Convert power to kW
power_kw = power_watts / 1000

# Calculate daily OPEX
daily_opex = power_kw * 24 * electricity_rate_usd_per_kwh

# Calculate break-even hash price (USD per TH)
break_even_hash_price = daily_opex / hashrate_th

# Output the results
print(f"Daily OPEX: ${daily_opex:.6f}")
print(f"Break-even hash price: ${break_even_hash_price:.6f} per TH/s per day")
