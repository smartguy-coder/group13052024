# cheese_kg = 0.234
# cheese_price = 132.64
#
# final_cost = cheese_kg * cheese_price
import decimal


final_cost = decimal.Decimal('31.025')
final_cost = final_cost.quantize(decimal.Decimal('0.01'), rounding=decimal.ROUND_HALF_UP)

print()
