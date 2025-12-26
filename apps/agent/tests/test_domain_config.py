#!/usr/bin/env python3
"""
Test script to verify domain configuration files are valid.

Tests:
1. data_analytics.json exists and is valid JSON
2. Required fields are present (domain, name, description, experts, tools, frameworks, quick_actions)
3. Experts structure is correct
4. Tools are organized by phase (intake, research, planning, risk)
5. Quick actions have required fields (label, message, icon)
"""

import json
import sys
from pathlib import Path


def test_domain_config_exists():
    """Test that data_analytics.json exists."""
    print("=" * 60)
    print("Testing Domain Config File Exists")
    print("=" * 60)
    
    # Path from test file: tests/ -> apps/agent/ -> project root -> config/domains/
    config_path = Path(__file__).parent.parent.parent.parent / "config" / "domains" / "data_analytics.json"
    
    if not config_path.exists():
        print(f"❌ Domain config file not found: {config_path}")
        return False
    
    print(f"✅ Domain config file exists: {config_path}")
    return True, config_path


def test_domain_config_valid_json(config_path):
    """Test that the config file is valid JSON."""
    print("\n" + "=" * 60)
    print("Testing Domain Config is Valid JSON")
    print("=" * 60)
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        print("✅ Domain config is valid JSON")
        return True, config
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        return False, None
    except Exception as e:
        print(f"❌ Error reading config: {e}")
        return False, None


def test_required_fields(config):
    """Test that all required fields are present."""
    print("\n" + "=" * 60)
    print("Testing Required Fields")
    print("=" * 60)
    
    required_fields = ["domain", "name", "description", "experts", "tools", "frameworks", "quick_actions"]
    missing_fields = []
    
    for field in required_fields:
        if field not in config:
            missing_fields.append(field)
            print(f"❌ Missing required field: {field}")
        else:
            print(f"✅ Required field present: {field}")
    
    if missing_fields:
        return False
    
    # Validate domain value
    if config["domain"] != "data_analytics":
        print(f"❌ Domain value should be 'data_analytics', got: {config['domain']}")
        return False
    print(f"✅ Domain value is correct: {config['domain']}")
    
    return True


def test_experts_structure(config):
    """Test that experts have correct structure."""
    print("\n" + "=" * 60)
    print("Testing Experts Structure")
    print("=" * 60)
    
    if not isinstance(config["experts"], list):
        print(f"❌ Experts should be a list, got: {type(config['experts'])}")
        return False
    
    if len(config["experts"]) < 3:
        print(f"❌ Should have at least 3 experts, got: {len(config['experts'])}")
        return False
    
    print(f"✅ Experts is a list with {len(config['experts'])} experts")
    
    required_expert_fields = ["id", "name", "focus"]
    for i, expert in enumerate(config["experts"]):
        for field in required_expert_fields:
            if field not in expert:
                print(f"❌ Expert {i} missing field: {field}")
                return False
        print(f"✅ Expert {i+1}: {expert.get('name', 'Unknown')} - {expert.get('id', 'no-id')}")
    
    return True


def test_tools_structure(config):
    """Test that tools are organized by phase."""
    print("\n" + "=" * 60)
    print("Testing Tools Structure")
    print("=" * 60)
    
    if not isinstance(config["tools"], dict):
        print(f"❌ Tools should be a dict, got: {type(config['tools'])}")
        return False
    
    required_phases = ["intake", "research", "planning", "risk"]
    missing_phases = []
    
    for phase in required_phases:
        if phase not in config["tools"]:
            missing_phases.append(phase)
            print(f"❌ Missing tools phase: {phase}")
        elif not isinstance(config["tools"][phase], list):
            print(f"❌ Tools phase '{phase}' should be a list, got: {type(config['tools'][phase])}")
            return False
        else:
            print(f"✅ Tools phase '{phase}' has {len(config['tools'][phase])} tools")
    
    if missing_phases:
        return False
    
    # Check total tool count (should have at least 3 as per Exercise 5)
    total_tools = sum(len(tools) for tools in config["tools"].values())
    if total_tools < 3:
        print(f"❌ Should have at least 3 tools total, got: {total_tools}")
        return False
    
    print(f"✅ Total tools: {total_tools}")
    return True


def test_frameworks_structure(config):
    """Test that frameworks have correct structure."""
    print("\n" + "=" * 60)
    print("Testing Frameworks Structure")
    print("=" * 60)
    
    if not isinstance(config["frameworks"], list):
        print(f"❌ Frameworks should be a list, got: {type(config['frameworks'])}")
        return False
    
    print(f"✅ Frameworks is a list with {len(config['frameworks'])} frameworks")
    
    required_framework_fields = ["name", "applied_when"]
    for i, framework in enumerate(config["frameworks"]):
        for field in required_framework_fields:
            if field not in framework:
                print(f"❌ Framework {i} missing field: {field}")
                return False
        print(f"✅ Framework {i+1}: {framework.get('name', 'Unknown')}")
    
    return True


def test_quick_actions_structure(config):
    """Test that quick actions have correct structure."""
    print("\n" + "=" * 60)
    print("Testing Quick Actions Structure")
    print("=" * 60)
    
    if not isinstance(config["quick_actions"], list):
        print(f"❌ Quick actions should be a list, got: {type(config['quick_actions'])}")
        return False
    
    if len(config["quick_actions"]) == 0:
        print("❌ Should have at least 1 quick action")
        return False
    
    print(f"✅ Quick actions is a list with {len(config['quick_actions'])} actions")
    
    required_action_fields = ["label", "message", "icon"]
    for i, action in enumerate(config["quick_actions"]):
        for field in required_action_fields:
            if field not in action:
                print(f"❌ Quick action {i} missing field: {field}")
                return False
        print(f"✅ Quick action {i+1}: {action.get('label', 'Unknown')}")
    
    return True


def main():
    """Run domain config tests."""
    print("\n🔍 Testing Domain Configuration: data_analytics.json\n")
    
    # Test 1: File exists
    exists_result = test_domain_config_exists()
    if not exists_result:
        print("\n❌ Domain config file does not exist. Create it first!")
        return 1
    
    exists_ok, config_path = exists_result
    
    # Test 2: Valid JSON
    json_result = test_domain_config_valid_json(config_path)
    if not json_result[0]:
        print("\n❌ Domain config is not valid JSON. Fix syntax errors!")
        return 1
    
    json_ok, config = json_result
    
    # Test 3: Required fields
    fields_ok = test_required_fields(config)
    
    # Test 4: Experts structure
    experts_ok = test_experts_structure(config)
    
    # Test 5: Tools structure
    tools_ok = test_tools_structure(config)
    
    # Test 6: Frameworks structure
    frameworks_ok = test_frameworks_structure(config)
    
    # Test 7: Quick actions structure
    quick_actions_ok = test_quick_actions_structure(config)
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    print(f"File exists:           {'✅ PASS' if exists_ok else '❌ FAIL'}")
    print(f"Valid JSON:            {'✅ PASS' if json_ok else '❌ FAIL'}")
    print(f"Required fields:       {'✅ PASS' if fields_ok else '❌ FAIL'}")
    print(f"Experts structure:     {'✅ PASS' if experts_ok else '❌ FAIL'}")
    print(f"Tools structure:       {'✅ PASS' if tools_ok else '❌ FAIL'}")
    print(f"Frameworks structure:  {'✅ PASS' if frameworks_ok else '❌ FAIL'}")
    print(f"Quick actions:         {'✅ PASS' if quick_actions_ok else '❌ FAIL'}")
    
    all_passed = all([
        exists_ok, json_ok, fields_ok, experts_ok, 
        tools_ok, frameworks_ok, quick_actions_ok
    ])
    
    if all_passed:
        print("\n✅ All domain config tests passed!")
        return 0
    else:
        print("\n❌ Some tests failed. Review output above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

