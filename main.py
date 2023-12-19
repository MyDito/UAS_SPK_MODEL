import sys
from colorama import Fore, Style
from models import Base, Smartphone
from engine import engine
from sqlalchemy import select
from sqlalchemy.orm import Session
from settings import (
    DEV_SCALE_brand,
    DEV_SCALE_ram,
    DEV_SCALE_storage,
    DEV_SCALE_processor,
    DEV_SCALE_battery,
    DEV_SCALE_harga,
)

session = Session(engine)


def create_table():
    Base.metadata.create_all(engine)
    print(f"{Fore.GREEN}[Success]: {Style.RESET_ALL}Database has created!")


class BaseMethod:
    def __init__(self):
        # 1-5
        self.raw_weight = {
            "brand": 3,
            "ram_gb": 4,
            "storage_gb": 4,
            "processor": 5,
            "battery": 1,
            "harga": 2,
        }

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {k: round(v / total_weight, 2) for k, v in self.raw_weight.items()}

    @property
    def data(self):
        query = select(Smartphone)
        return [
            {
                "id": hitung_smartphone.id,
                "brand": DEV_SCALE_brand.get(hitung_smartphone.brand, 0),
                "ram_gb": DEV_SCALE_ram.get(hitung_smartphone.ram_gb, 0),
                "storage_gb": DEV_SCALE_storage.get(hitung_smartphone.storage_gb, 0),
                "processor": DEV_SCALE_processor.get(hitung_smartphone.processor, 0),
                "battery": DEV_SCALE_battery.get(hitung_smartphone.battery, 0),
                "harga": DEV_SCALE_harga.get(hitung_smartphone.harga, 0),
            }
            for hitung_smartphone in session.scalars(query)
        ]

    @property
    def normalized_data(self):
        # x/max [benefit]
        # min/x [cost]
        brand = []  # max
        ram_gb = []  # max
        storage_gb = []  # max
        processor = []  # max
        battery = []  # max
        harga = []  # min
        for data in self.data:
            brand.append(data["brand"])
            ram_gb.append(data["ram_gb"])
            storage_gb.append(data["storage_gb"])
            processor.append(data["processor"])
            battery.append(data["battery"])
            harga.append(data["harga"])

        # Handling empty lists
        max_brand = max(brand) if brand else 0
        max_ram = max(ram_gb) if ram_gb else 0
        max_storage = max(storage_gb) if storage_gb else 0
        max_prosesor = max(processor) if processor else 0
        max_baterai = max(battery) if battery else 0
        min_harga = min(harga) if harga else 0

        return [
            {
                "id": data["id"],
                "brand": data["brand"] / max_brand if max_brand != 0 else 0,  # benefit
                "ram_gb": data["ram_gb"] / max_ram if max_ram != 0 else 0,  # benefit
                "storage_gb": data["storage_gb"] / max_storage
                if max_storage != 0
                else 0,  # benefit
                "processor": data["processor"] / max_prosesor
                if max_prosesor != 0
                else 0,  # benefit
                "battery": data["battery"] / max_baterai
                if max_baterai != 0
                else 0,  # benefit
                "harga": min_harga / data["harga"] if data["harga"] != 0 else 0,  # cost
            }
            for data in self.data
        ]


class WeightedProduct(BaseMethod):
    @property
    def calculate(self):
        weight = self.weight
        # calculate data and weight[WP]
        result = {
            row["id"]: round(
                row["brand"] ** weight["brand"]
                * row["ram_gb"] ** weight["ram_gb"]
                * row["storage_gb"] ** weight["storage_gb"]
                * row["processor"] ** weight["processor"]
                * row["battery"] ** weight["battery"]
                * row["harga"] ** weight["harga"],
                2,
            )
            for row in self.normalized_data
        }
        # sorting
        return dict(
            sorted(result.items(), key=lambda x: x[1], reverse=True)
        )  # Sorting descending


class SimpleAdditiveWeighting(BaseMethod):
    @property
    def calculate(self):
        weight = self.weight
        # calculate data and weight
        result = {
            row["id"]: round(
                row["brand"] * weight["brand"]
                + row["ram_gb"] * weight["ram_gb"]
                + row["storage_gb"] * weight["storage_gb"]
                + row["processor"] * weight["processor"]
                + row["battery"] * weight["battery"]
                + row["harga"] * weight["harga"],
                2,
            )
            for row in self.normalized_data
        }
        # sorting
        return dict(
            sorted(result.items(), key=lambda x: x[1], reverse=True)
        )  # Sorting descending


def run_saw():
    saw = SimpleAdditiveWeighting()
    print("result:", saw.calculate)


def run_wp():
    wp = WeightedProduct()
    print("result:", wp.calculate)


if len(sys.argv) > 1:
    arg = sys.argv[1]

    if arg == "create_table":
        create_table()
    elif arg == "saw":
        run_saw()
    elif arg == "wp":
        run_wp()
    else:
        print("command not found")
