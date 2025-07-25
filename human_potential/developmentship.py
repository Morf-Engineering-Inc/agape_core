# Usage Tips:
# Run calculate_hp with your inputs.
# For AI decision-making: Use decide_best_scenario to pick the highest HP option (e.g., optimize team size/creativity).
# Customize: Add weights (e.g., for virtue or skills from Murff's book) or integrate with our prior Value Impact code.
# Data Sources: Estimate C from surveys (e.g., innovation self-assessments); M from team sizes.



import asyncio
import platform
FPS = 60  # For Pyodide compatibility

async def main():
    calc = HumanPotentialCalculator()
    # Example: Individual with moderate creativity
    hp_individual = await calc.calculate_hp(mass=1, creativity=0.7)
    print(f"Individual HP: {hp_individual}")

    # Example: Team with high creativity
    hp_team = await calc.calculate_hp(mass=100, creativity=0.95, growth=50, opportunity_cost=20)
    print(f"Team HP: {hp_team}")

    # Compare scenarios
    decision = calc.decide_best_scenario([
        ("Individual", hp_individual),
        ("Team", hp_team)
    ])
    print(f"Best scenario: {decision[0]} with HP {decision[1]}")

class HumanPotentialCalculator:
    def __init__(self):
        self.scenarios = {}

    async def calculate_hp(self, mass, creativity, growth=0, opportunity_cost=0):
        """Calculate Human Potential: HP = M * C² + Growth - Opportunity Cost."""
        if mass <= 0 or creativity < 0:
            raise ValueError("Mass must be >0, Creativity >=0")
        base_hp = mass * (creativity ** 2)
        total_hp = base_hp + growth - opportunity_cost
        await asyncio.sleep(1.0 / FPS)  # Pyodide frame rate simulation
        return max(0, total_hp)  # Ensure non-negative

    def decide_best_scenario(self, scenarios):
        """Return the scenario with the highest HP."""
        if not scenarios:
            return ("None", 0)
        best = max(scenarios, key=lambda x: x[1])
        return best

    def add_scenario(self, name, mass, creativity, growth=0, opportunity_cost=0):
        """Add a scenario for comparison."""
        hp = asyncio.run(self.calculate_hp(mass, creativity, growth, opportunity_cost))
        self.scenarios[name] = hp

    def get_all_hp(self):
        """Return all calculated HP values."""
        return self.scenarios

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())
