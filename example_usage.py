from client import AgentCostOptimizationOrchestratorClient

def main():
    client = AgentCostOptimizationOrchestratorClient()
    res = client.optimize_route("Generate unit test for python function add(a, b)", max_budget_cents=2.0)
    print(f"Routed Model: {res['routed_model']}")
    print(f"Estimated Cost: ${res['estimated_cost_cents']/100:.4f} (Saved {res['savings_pct']}%)")

if __name__ == "__main__":
    main()
