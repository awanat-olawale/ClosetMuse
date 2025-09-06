from django.test import TestCase
from django.contrib.auth import get_user_model
from wardrobe.models import WardrobeItem
from planner.models import OutfitPlanner
from datetime import date

User = get_user_model()

class OutfitPlannerModelTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )

        # Create wardrobe item
        self.item = WardrobeItem.objects.create(
            name="Blue Abaya",
            category="TOP",
            colour="Blue",
            owner=self.user
        )

    def test_create_outfit_planner(self):
        # Create planner with wardrobe item
        planner = OutfitPlanner.objects.create(
            owner=self.user,
            date=date.today(),
            occasion="Casual"
        )
        planner.items.add(self.item)  # many-to-many relationship

        self.assertEqual(planner.owner, self.user)
        self.assertEqual(planner.items.count(), 1)
        self.assertIn(self.item, planner.items.all())
