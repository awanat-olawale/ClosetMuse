from django.utils import timezone
from django.test import TestCase
from django.contrib.auth import get_user_model
from wardrobe.models import WardrobeItem
from declutter.models import OutfitDeclutter

User = get_user_model()

class OutfitDeclutterModelTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="declutteruser",
            password="password123"
        )

        # Create wardrobe item
        self.item = WardrobeItem.objects.create(
            name="Old Hijab",
            category="HIJAB",
            colour="Black",
            owner=self.user
        )

    def test_create_outfit_declutter(self):
        declutter = OutfitDeclutter.objects.create(
            owner=self.user,
            item=self.item,
            last_worn=timezone.now(),
            wear_count=20,
            reason="DONATE"
        )

        self.assertEqual(declutter.owner, self.user)
        self.assertEqual(declutter.item, self.item)
        self.assertEqual(declutter.reason, "DONATE")
