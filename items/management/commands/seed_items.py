from lib2to3.pytree import Base
import random
from datetime import datetime
from typing import Any, Optional
from unicodedata import category
from django.core.management.base import BaseCommand
from django_seed import Seed

from items.models import Benefits, Category, Items, Owners


class Command(BaseCommand):
    help = "it seeds the items and fields related to it "

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        category = Category.objects.all()
        items = Items.objects.all()
        owner = Owners.objects.all()

        category_seeder = Seed.seeder()
        items_seeder = Seed.seeder()
        owner_seeder = Seed.seeder()
        owner_seeder.add_entity(Owners, 10)
        benefites_seeder = Seed.seeder()
        benefites_seeder.add_entity(Benefits, 10)
        category_seeder.add_entity(Category, 10)
        items_seeder.add_entity(
            Items,
            150,
            {
                "img_source_link": "https://picsum.photos/200/300",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                "popular_ind": True,
                "recent_customer_name": "https://picsum.photos/200/300",
                "recent_customer_desc": "https://picsum.photos/200/300",
                "recent_customer_score": random.randint(1, 5),
            },
        )

        # owner_seeder.execute()
        # benefites_seeder.execute()
        # category_seeder.execute()
        items_seeder.execute()
        print("Everything is seeded")
