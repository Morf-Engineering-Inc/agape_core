import asyncio
import platform
FPS = 60

async def main():
    calc = ValueImpactCalculator()
    # Example usage: Compare Musk as President vs. running companies
    pres_impact = await calc.calculate_impact(utility_per_person=362, num_people=345000000, growth_impact=0, opportunity_cost=15000000000)
    comp_impact = await calc.calculate_impact(utility_per_person=500, num_people=100000000, growth_impact=0, opportunity_cost=0)
    decision = calc.decide_best_option([("President", pres_impact), ("Companies", comp_impact)])
    print(f"Best option: {decision[0]} with impact ${decision[1]:,.2f}")

class ValueImpactCalculator:
    def __init__(self):
        self.options = {}

    async def calculate_impact(self, utility_per_person, num_people, growth_impact=0, opportunity_cost=0):
        """Calculate total impact based on utility, people, growth, and opportunity cost."""
        base_impact = utility_per_person * num_people
        total_impact = base_impact + growth_impact - opportunity_cost
        await asyncio.sleep(1.0 / FPS)  # Simulate frame rate control for Pyodide
        return max(0, total_impact)  # Ensure non-negative impact

    def decide_best_option(self, options):
        """Return the option with the highest impact."""
        if not options:
            return ("None", 0)
        best_option = max(options, key=lambda x: x[1])
        return best_option

    def add_option(self, name, utility_per_person, num_people, growth_impact=0, opportunity_cost=0):
        """Add an option for comparison."""
        impact = asyncio.run(self.calculate_impact(utility_per_person, num_people, growth_impact, opportunity_cost))
        self.options[name] = impact

    def get_all_impacts(self):
        """Return all calculated impacts."""
        return self.options

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())