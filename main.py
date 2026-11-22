#!/usr/bin/env python3
"""Write the competition plan to /output/entry.txt.

Plan: sell a small, boring, already-paid-for service (product-photo
cleanup for Etsy sellers) via Fiverr, using free code and free samples
to win the first orders.
"""

import os

PLAN = (
    "Day 1: list a $15 Fiverr gig: clean and stage 10 product photos in "
    "24h. Use free rembg code. DM 100 Etsy sellers a free before/after "
    "sample of their own photo. Reinvest profits in Fiverr ads. Edge: "
    "sellers already pay for this chore; agents chase crypto. Target: "
    "20 orders = $300."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
