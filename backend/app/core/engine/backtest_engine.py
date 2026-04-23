def run_backtest(strategy, market_data):
    return {
        "strategy": strategy,
        "trades": [],
        "metrics": {
            "total_trades": 0,
            "net_pnl": 0.0,
            "win_rate": 0.0,
        },
        "market_data_points": len(market_data or []),
    }
