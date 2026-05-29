# Task 2 - Production Counter System

import random

target_units = int(input("Enter target units: "))
workers_per_shift = int(input("Enter workers per shift: "))
defect_rate = float(input("Enter defect rate (as percentage, e.g. 10 for 10%): "))

print("\n")
print("=" * 55)
print("         PRODUCTION COUNTER SYSTEM")
print("=" * 55)

total_produced = 0
total_defects = 0
target_reached = False

# 3 shifts x 20 machine cycles
for shift in range(1, 4):
    shift_produced = 0
    shift_defects = 0

    print(f"\n   Shift {shift} Starting...")
    print("-" * 55)

    for cycle in range(1, 21):

        # Randomly mark items as defective using continue
        if random.random() * 100 < defect_rate:
            shift_defects += 1
            total_defects += 1
            continue  # skip defective item

        shift_produced += 1
        total_produced += 1

        # Stop ALL production when target is reached using break
        if total_produced >= target_units:
            print(f"   Target reached at Shift {shift}, Cycle {cycle}!")
            target_reached = True
            break

    # Worker productivity per shift
    worker_productivity = round(shift_produced / workers_per_shift, 2)

    print(f"  Items Produced  : {shift_produced}")
    print(f"  Defects         : {shift_defects}")
    print(f"  Worker Productivity : {worker_productivity} units/worker")

    if target_reached:
        break

print("\n" + "=" * 55)
print("        FINAL PRODUCTION SUMMARY")
print("=" * 55)
print(f"  Target Units    : {target_units}")
print(f"  Total Produced  : {total_produced}")
print(f"  Total Defects   : {total_defects}")
print(f"  Target Reached  : {' Yes' if target_reached else ' No'}")
print("=" * 55)
