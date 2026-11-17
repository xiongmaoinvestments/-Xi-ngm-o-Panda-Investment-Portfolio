"""
Xióngmāo Investment Portfolio - Financial Calculator & Payout Engine
Author: Justice Barnor (CATCO Media Tech Solutions / Xióngmāo Capital)
Description: Python utility to compute 3-cycle payouts, 2x high-yield options, and Silver Lining guarantees.
"""

def calculate_investment(capital, mode="standard"):
    """
    Calculates returns based on capital and investment mode.
    - standard: 3 consecutive cycles (e.g. GH₵ 3,000 each for GH₵ 2,000 base)
    - highyield: 2x accelerated single-window option
    """
    ratio = capital / 2000.0
    
    if mode == "standard":
        cycle_payout = 3000.0 * ratio
        total_payout = cycle_payout * 3
        total_profit = total_payout - capital
        roi = (total_profit / capital) * 100.0
        return {
            "mode": "Standard 3-Cycle",
            "capital": capital,
            "cycle_1": cycle_payout,
            "cycle_2": cycle_payout,
            "cycle_3": cycle_payout,
            "total_payout": total_payout,
            "net_profit": total_profit,
            "roi_percent": roi
        }
    elif mode == "highyield":
        total_payout = capital * 2.0
        total_profit = capital
        roi = 100.0
        return {
            "mode": "2x High Yield Tier",
            "capital": capital,
            "total_payout": total_payout,
            "net_profit": total_profit,
            "roi_percent": roi
        }

if __name__ == "__main__":
    print("==================================================")
    print(" XIÓNGMĀO INVESTMENT PORTFOLIO - CALCULATION ENGINE")
    print("==================================================")
    
    tier_capital = 2000.0
    
    # Standard 3-Cycle calculation
    res_std = calculate_investment(tier_capital, mode="standard")
    print(f"\n[Tier A Base: GH₵ {tier_capital:,.2f}] -> Mode: {res_std['mode']}")
    print(f"  Cycle 1 (20-25d): GH₵ {res_std['cycle_1']:,.2f}")
    print(f"  Cycle 2 (20-25d): GH₵ {res_std['cycle_2']:,.2f}")
    print(f"  Cycle 3 (20-25d): GH₵ {res_std['cycle_3']:,.2f}")
    print(f"  Total Cumulative Payout: GH₵ {res_std['total_payout']:,.2f}")
    print(f"  Total Net Profit: GH₵ {res_std['net_profit']:,.2f} ({res_std['roi_percent']:.1f}% ROI)")

    # 2x High Yield calculation
    res_hy = calculate_investment(tier_capital, mode="highyield")
    print(f"\n[Tier A Base: GH₵ {tier_capital:,.2f}] -> Mode: {res_hy['mode']}")
    print(f"  Total Accelerated Payout: GH₵ {res_hy['total_payout']:,.2f}")
    print(f"  Total Net Profit: GH₵ {res_hy['net_profit']:,.2f} ({res_hy['roi_percent']:.1f}% ROI)")
    print("\nNote: Silver Lining policy active (2x payout eligibility for missed windows).")
    print("==================================================")
