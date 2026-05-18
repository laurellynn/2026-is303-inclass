"""
FreshCart POS System
====================
IS 303 — Day 6: Functions Unlocked

Each department fills in their functions below.
The main() function at the bottom wires everything together.

DEPARTMENTS:
  Team 1: CHECKOUT  — scan_item(), calculate_subtotal()
  Team 2: INVENTORY — check_stock(), update_stock()
  Team 3: LOYALTY   — check_membership(), apply_discount()
  Team 4: RECEIPTS  — calculate_tax(), generate_receipt()
"""

# ============================================================
# SHARED DATA — Everyone uses these (do NOT edit)
# ============================================================

INVENTORY = {
    "apple":   {"price": 1.25, "stock": 50},
    "bread":   {"price": 3.49, "stock": 30},
    "milk":    {"price": 4.99, "stock": 20},
    "cheese":  {"price": 6.75, "stock": 15},
    "chips":   {"price": 3.99, "stock": 40},
    "soda":    {"price": 1.99, "stock": 60},
    "eggs":    {"price": 5.49, "stock": 25},
    "chicken": {"price": 8.99, "stock": 10},
}

MEMBERS = {
    "M001": {"name": "Sarah Johnson",  "discount": 0.10},
    "M002": {"name": "Mike Chen",      "discount": 0.15},
    "M003": {"name": "Emma Davis",     "discount": 0.05},
}


# ============================================================
# 1: CHECKOUT — Scan items and calculate subtotal
# ============================================================




# ============================================================
# 2: INVENTORY — Check and update stock levels
# ============================================================




# ============================================================
# 3: LOYALTY — Membership lookup and discounts
# ============================================================
customer_id = input("Enter Membership ID (or enter to skip)" )

def check_membership(customer_id, MEMBERS):
    if customer_id in MEMBERS.keys():
        name = MEMBERS [customer_id]["name"]
        discount = MEMBERS [customer_id]["discount"]
        return f"Welcome back, {name}! Your discount is {discount*100}%."
    else:
        return "No membership found. No discount applied."

print(check_membership(customer_id, MEMBERS))
# ============================================================
# 4: RECEIPTS & TAX — Tax calculation and receipt
# ============================================================




# ============================================================
# MAIN — The CEO wires everything together
# (Do NOT edit until integration phase)
# ============================================================