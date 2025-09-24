def calculate_mining_opex():
    # Take inputs from user
    hashrate_th = float(input("Enter miner's hashrate in TH/s: "))
    efficiency_j_per_th = float(input("Enter miner's efficiency in J/TH: "))
    electricity_rate_usd_per_kwh = float(input("Enter electricity rate in USD per kWh: "))
    
    # Calculate power in watts
    power_watts = hashrate_th * efficiency_j_per_th
    
    # Convert power to kW
    power_kw = power_watts / 1000
    
    # Calculate average hours in a month
    avg_hours_per_month = (365 * 24) / 12
    
    # Calculate monthly OPEX in USD
    opex_usd = power_kw * avg_hours_per_month * electricity_rate_usd_per_kwh
    
    print(f"\nPower consumption: {power_kw:.3f} kW")
    print(f"Monthly OPEX: ${opex_usd:.2f} USD")

# Run the function
calculate_mining_opex()
