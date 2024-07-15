from project.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):
    BUDGET: float = 2500.0
    MIN_ENGAGEMENT_RATE: float = 0.9    #90%

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, self.BUDGET, required_engagement)

    def check_eligibility(self, engagement_rate: float):
        needed_rate = self.MIN_ENGAGEMENT_RATE * self.required_engagement
        return engagement_rate >= needed_rate
