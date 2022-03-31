# Group 17 Project

## Single-student project
- Public endpoint:
   - [x] Retrieve list of ski types with model filter
- Storekeeper:
   - [ ] Create records newly produced skis
- Customer:
   - [x] Retrieve a four week production plan summary
   - [x] Delete a given order
- Customer rep:
   - [ ] Retrieve orders with status filter set to new
   - [ ] Change the order state from new to open for an unassigned order

## Double-student project extra:
- Public endpoint:
   - [ ] Add ski size filter to the Retrieve operations
- Planner:
   - [x] Create new production plans
- Customer endpoint:
   - [ ] Create new orders
- Customer rep:
   - [ ] Adding filter for status = skis-available
   Retrieve orders with status filter set to skis-available
- Shipper endpoint:
   - [x] Create a transition record for the order from ready-for-shipping to shipped for a ready-for-shipping order

## Triple-student project extra:
- Customer endpoint:
   - [ ] Retrieve orders with since filter
   - [ ] Retrieve a specific order
   - [ ] Creating a new order for the unassigned items in a current order, making the current one ready-for-shipping
- Storekeeper:
   - [ ] Retrieve orders
   - [ ] Create a transition record for the order when more skis are assigned to the order
- Customer rep:
   - [ ] Retrieve orders with filters status set to skis-available
