from day3_practice import Campaign


class CampaignManager:
    """Holds a list of Campaign objects and provides aggregate operations."""

    def __init__(self) -> None:
        self.campaigns: list[Campaign] = []

    def add(self, campaign: Campaign) -> None:
        self.campaigns.append(campaign)

    def total_spend(self) -> float:
        total = 0.0
        for campaign in self.campaigns:
            total += campaign.spend
        return total

    def best_performing(self) -> Campaign:
        best = None
        for campaign in self.campaigns:
            if campaign.conversions == 0:
                continue
            if best is None or campaign.cpa() < best.cpa():
                best = campaign
        if best is None:
            raise ValueError("No campaigns with conversions")
        return best

    def __repr__(self) -> str:
        return f"CampaignManager({len(self.campaigns)} campaigns, total_spend=${self.total_spend():.2f})"

    def __len__(self) -> int:
        return len(self.campaigns)


if __name__ == "__main__":
    manager = CampaignManager()
    manager.add(Campaign("Meta_BF", 1200.00, 450, 23))
    manager.add(Campaign("Google_Q4", 2100.50, 320, 18))
    manager.add(Campaign("Meta_Lead", 800.00, 200, 0))

    print(manager)
    print(f"Number of campaigns: {len(manager)}")
    print(f"Total spend: ${manager.total_spend():.2f}")
    print(f"Best performing: {manager.best_performing()}")

    print("\n--- Empty manager test ---")
    empty = CampaignManager()
    print(f"Empty manager: {empty}")
    print(f"Length: {len(empty)}")
    print(f"Total spend: ${empty.total_spend():.2f}")
    try:
        empty.best_performing()
    except ValueError as e:
        print(f"Caught: {e}")

    print("\n--- Zero-conversion manager test ---")
    zero_mgr = CampaignManager()
    zero_mgr.add(Campaign("Test1", 100.0, 50, 0))
    zero_mgr.add(Campaign("Test2", 200.0, 80, 0))
    print(f"Manager: {zero_mgr}")
    try:
        zero_mgr.best_performing()
    except ValueError as e:
        print(f"Caught: {e}")

        