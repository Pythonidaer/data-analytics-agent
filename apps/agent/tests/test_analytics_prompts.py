#!/usr/bin/env python3
"""
Test script to verify analytics prompts are implemented correctly.

Tests:
1. Analytics prompts module can be imported
2. MAIN_SYSTEM_PROMPT exists and is a non-empty string
3. All 4 specialist prompts exist (Analytics Strategist, Product Analyst, Analytics Engineer, Insights Communicator)
4. Prompts contain expected analytics terminology
5. Prompts follow the same structure as PMM prompts
"""

import sys
from pathlib import Path

# Add src to path for imports
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))


def test_analytics_prompts_import():
    """Test that analytics prompts can be imported."""
    print("=" * 60)
    print("Testing Analytics Prompts Import")
    print("=" * 60)
    
    try:
        from pmm_agent.domains.data_analytics.prompts import (
            MAIN_SYSTEM_PROMPT,
            ANALYTICS_STRATEGIST_PROMPT,
            PRODUCT_ANALYST_PROMPT,
            ANALYTICS_ENGINEER_PROMPT,
            INSIGHTS_COMMUNICATOR_PROMPT,
        )
        print("✅ Analytics prompts can be imported")
        return True, {
            "MAIN_SYSTEM_PROMPT": MAIN_SYSTEM_PROMPT,
            "ANALYTICS_STRATEGIST_PROMPT": ANALYTICS_STRATEGIST_PROMPT,
            "PRODUCT_ANALYST_PROMPT": PRODUCT_ANALYST_PROMPT,
            "ANALYTICS_ENGINEER_PROMPT": ANALYTICS_ENGINEER_PROMPT,
            "INSIGHTS_COMMUNICATOR_PROMPT": INSIGHTS_COMMUNICATOR_PROMPT,
        }
    except ImportError as e:
        print(f"❌ Cannot import analytics prompts: {e}")
        return False, None


def test_main_system_prompt(prompts):
    """Test that MAIN_SYSTEM_PROMPT is valid."""
    print("\n" + "=" * 60)
    print("Testing Main System Prompt")
    print("=" * 60)
    
    if prompts is None:
        print("❌ Cannot test - prompts not available")
        return False
    
    main_prompt = prompts["MAIN_SYSTEM_PROMPT"]
    
    # Check it's a string
    if not isinstance(main_prompt, str):
        print(f"❌ MAIN_SYSTEM_PROMPT should be a string, got: {type(main_prompt)}")
        return False
    
    # Check it's not empty
    if len(main_prompt.strip()) == 0:
        print("❌ MAIN_SYSTEM_PROMPT is empty")
        return False
    
    # Check minimum length (should be substantial)
    if len(main_prompt) < 500:
        print(f"⚠️  MAIN_SYSTEM_PROMPT seems short ({len(main_prompt)} chars)")
    
    # Check for analytics-specific terminology
    analytics_keywords = ["analytics", "KPI", "metric", "data", "SQL", "dashboard", "tracking"]
    found_keywords = [kw for kw in analytics_keywords if kw.lower() in main_prompt.lower()]
    
    if len(found_keywords) == 0:
        print("⚠️  MAIN_SYSTEM_PROMPT doesn't contain expected analytics keywords")
    else:
        print(f"✅ Found analytics keywords: {', '.join(found_keywords)}")
    
    # Check for clarification protocol (should be present like PMM)
    if "clarification" in main_prompt.lower() or "clarify" in main_prompt.lower():
        print("✅ Contains clarification protocol")
    else:
        print("⚠️  May be missing clarification protocol")
    
    print(f"✅ MAIN_SYSTEM_PROMPT is valid ({len(main_prompt)} characters)")
    return True


def test_specialist_prompts(prompts):
    """Test that all specialist prompts exist and are valid."""
    print("\n" + "=" * 60)
    print("Testing Specialist Prompts")
    print("=" * 60)
    
    if prompts is None:
        print("❌ Cannot test - prompts not available")
        return False
    
    specialist_prompts = {
        "Analytics Strategist": prompts["ANALYTICS_STRATEGIST_PROMPT"],
        "Product Analyst": prompts["PRODUCT_ANALYST_PROMPT"],
        "Analytics Engineer": prompts["ANALYTICS_ENGINEER_PROMPT"],
        "Insights Communicator": prompts["INSIGHTS_COMMUNICATOR_PROMPT"],
    }
    
    all_valid = True
    for name, prompt in specialist_prompts.items():
        if not isinstance(prompt, str):
            print(f"❌ {name} prompt should be a string, got: {type(prompt)}")
            all_valid = False
            continue
        
        if len(prompt.strip()) == 0:
            print(f"❌ {name} prompt is empty")
            all_valid = False
            continue
        
        if len(prompt) < 200:
            print(f"⚠️  {name} prompt seems short ({len(prompt)} chars)")
        
        print(f"✅ {name} prompt is valid ({len(prompt)} characters)")
    
    return all_valid


def test_prompt_structure(prompts):
    """Test that prompts follow expected structure."""
    print("\n" + "=" * 60)
    print("Testing Prompt Structure")
    print("=" * 60)
    
    if prompts is None:
        print("❌ Cannot test - prompts not available")
        return False
    
    main_prompt = prompts["MAIN_SYSTEM_PROMPT"]
    
    # Check for expected sections (similar to PMM structure)
    expected_sections = [
        "philosophy",  # or "Philosophy"
        "workflow",    # or "Workflow"
        "outputs",     # or "Outputs"
    ]
    
    found_sections = []
    for section in expected_sections:
        if section.lower() in main_prompt.lower():
            found_sections.append(section)
    
    if len(found_sections) >= 2:
        print(f"✅ Found expected sections: {', '.join(found_sections)}")
    else:
        print(f"⚠️  May be missing expected sections. Found: {', '.join(found_sections) if found_sections else 'none'}")
    
    return True


def main():
    """Run analytics prompts tests."""
    print("\n🔍 Testing Analytics Prompts\n")
    
    # Test 1: Import
    import_result = test_analytics_prompts_import()
    if not import_result[0]:
        print("\n❌ Import test failed. Create analytics prompts first!")
        return 1
    
    prompts = import_result[1]
    
    # Test 2: Main system prompt
    main_ok = test_main_system_prompt(prompts)
    
    # Test 3: Specialist prompts
    specialist_ok = test_specialist_prompts(prompts)
    
    # Test 4: Prompt structure
    structure_ok = test_prompt_structure(prompts)
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    print(f"Import:              {'✅ PASS' if import_result[0] else '❌ FAIL'}")
    print(f"Main prompt:         {'✅ PASS' if main_ok else '❌ FAIL'}")
    print(f"Specialist prompts:  {'✅ PASS' if specialist_ok else '❌ FAIL'}")
    print(f"Prompt structure:    {'✅ PASS' if structure_ok else '❌ FAIL'}")
    
    all_passed = import_result[0] and main_ok and specialist_ok and structure_ok
    
    if all_passed:
        print("\n✅ All analytics prompts tests passed!")
        return 0
    else:
        print("\n❌ Some tests failed. Review output above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

