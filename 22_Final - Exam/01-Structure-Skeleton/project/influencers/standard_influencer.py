from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):
    INITIAL_PAYMENT_PERCENTAGE = 0.45

    def calculate_payment(self, campaign: BaseCampaign):
        return float(campaign.budget * self.INITIAL_PAYMENT_PERCENTAGE)

    def reached_followers(self, campaign_type: str):
        result = 0

        if campaign_type == "HighBudgetCampaign":
            result = (self.followers * self.engagement_rate) * 1.20
        elif campaign_type == "LowBudgetCampaign":
            result = (self.followers * self.engagement_rate) * 0.90

        return int(result)

