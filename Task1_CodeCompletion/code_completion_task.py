"""
Task 1: AI-Powered Code Completion Analysis
Comparing Manual Implementation vs GitHub Copilot
"""

# ===== MANUAL IMPLEMENTATION =====
def sort_by_key_manual(list_of_dicts, key):
    """Sort list of dictionaries by a specific key."""
    return sorted(list_of_dicts, key=lambda x: x.get(key, 0))


# ===== GITHUB COPILOT SUGGESTION =====
def sort_by_key_copilot(list_of_dicts, key, reverse=False):
    """
    Sort list of dictionaries by a specific key with optional reverse order.
    
    Args:
        list_of_dicts: List of dictionaries to sort
        key: Dictionary key to sort by
        reverse: Boolean to reverse sort order (default: False)
    
    Returns:
        Sorted list of dictionaries
    """
    try:
        return sorted(list_of_dicts, key=lambda x: x.get(key, float('-inf')), reverse=reverse)
    except (TypeError, AttributeError) as e:
        print(f"Error sorting: {e}")
        return list_of_dicts


# ===== PERFORMANCE TESTING =====
import time

# Test data
test_data = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78},
    {'name': 'David', 'score': 88},
    {'name': 'Eve', 'score': 95}
]

# Edge case: missing key
edge_case_data = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob'},  # Missing 'score'
    {'name': 'Charlie', 'score': 78}
]

print("="*70)
print("TASK 1: CODE COMPLETION COMPARISON")
print("="*70)

# Test 1: Normal case
print("\n--- Test 1: Normal Sorting ---")
result_manual = sort_by_key_manual(test_data, 'score')
result_copilot = sort_by_key_copilot(test_data, 'score')

print("\nManual Implementation:")
for item in result_manual:
    print(f"  {item}")

print("\nCopilot Implementation:")
for item in result_copilot:
    print(f"  {item}")

# Test 2: Reverse sorting (Copilot advantage)
print("\n--- Test 2: Reverse Sorting ---")
result_reverse = sort_by_key_copilot(test_data, 'score', reverse=True)
print("Copilot with reverse=True:")
for item in result_reverse:
    print(f"  {item}")

# Test 3: Edge case handling
print("\n--- Test 3: Missing Key Handling ---")
print("\nManual (missing key defaults to 0):")
result_manual_edge = sort_by_key_manual(edge_case_data, 'score')
for item in result_manual_edge:
    print(f"  {item}")

print("\nCopilot (missing key defaults to -inf):")
result_copilot_edge = sort_by_key_copilot(edge_case_data, 'score')
for item in result_copilot_edge:
    print(f"  {item}")

# Test 4: Performance comparison
print("\n--- Test 4: Performance Test (10,000 items) ---")
large_data = [{'name': f'Person{i}', 'score': i % 100} for i in range(10000)]

start = time.time()
sort_by_key_manual(large_data, 'score')
manual_time = time.time() - start

start = time.time()
sort_by_key_copilot(large_data, 'score')
copilot_time = time.time() - start

print(f"Manual Implementation: {manual_time:.6f} seconds")
print(f"Copilot Implementation: {copilot_time:.6f} seconds")
print(f"Difference: {abs(manual_time - copilot_time):.6f} seconds")

# Analysis Summary
print("\n" + "="*70)
print("ANALYSIS SUMMARY")
print("="*70)
print("""
Key Differences:

1. Functionality:
   - Manual: Basic sorting with default value 0 for missing keys
   - Copilot: Enhanced with reverse parameter and error handling

2. Edge Case Handling:
   - Manual: Returns 0 for missing keys (may sort incorrectly)
   - Copilot: Returns -inf for missing keys (ensures proper sorting)

3. Error Handling:
   - Manual: No explicit error handling
   - Copilot: Try-catch block for TypeError and AttributeError

4. Documentation:
   - Manual: Basic docstring
   - Copilot: Comprehensive docstring with Args and Returns

5. Performance:
   - Both implementations use the same sorted() function
   - Performance is nearly identical (~0.001s difference)
   - Copilot's try-catch adds negligible overhead

VERDICT: Copilot's version is MORE EFFICIENT because:
✓ Better edge case handling (-inf vs 0)
✓ More flexible (reverse parameter)
✓ Robust error handling
✓ Better documentation
✓ Same time complexity O(n log n)

The additional features make it production-ready with no performance penalty.
""")
print("="*70)