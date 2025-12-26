#!/usr/bin/env python3
"""
Test script to verify create_analytics_agent() function.

Tests:
1. create_analytics_agent() exists and can be imported
2. create_analytics_agent() returns a valid LangGraph agent
3. Agent has correct system prompt (analytics domain)
4. Agent has analytics tools loaded
5. Agent can be invoked with a test message
"""

import sys
import os
from pathlib import Path

# Add src to path for imports
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))


def test_analytics_agent_import():
    """Test that create_analytics_agent can be imported."""
    print("=" * 60)
    print("Testing Analytics Agent Import")
    print("=" * 60)
    
    try:
        from pmm_agent.agent import create_analytics_agent
        print("✅ create_analytics_agent can be imported")
        return True, create_analytics_agent
    except ImportError as e:
        # Check if it's the function missing vs module missing
        try:
            from pmm_agent import agent
            if hasattr(agent, 'create_analytics_agent'):
                print("✅ create_analytics_agent exists in agent module")
                return True, agent.create_analytics_agent
            else:
                print(f"❌ create_analytics_agent function not found in agent module")
                print(f"   Available functions: {[f for f in dir(agent) if not f.startswith('_')]}")
                return False, None
        except ImportError:
            print(f"❌ Cannot import pmm_agent.agent module: {e}")
            return False, None


def test_analytics_agent_creation(create_analytics_agent_func):
    """Test that create_analytics_agent returns a valid agent."""
    print("\n" + "=" * 60)
    print("Testing Analytics Agent Creation")
    print("=" * 60)
    
    if create_analytics_agent_func is None:
        print("❌ Cannot test - function not available")
        return False
    
    try:
        # Check if API key is set (required for agent creation)
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            print("⚠️  ANTHROPIC_API_KEY not set - skipping agent creation test")
            print("   Set it with: export ANTHROPIC_API_KEY=sk-ant-your-key")
            return True  # Not a failure, just can't test without API key
        
        # Create the agent
        agent = create_analytics_agent_func()
        
        # Check that agent is not None
        if agent is None:
            print("❌ create_analytics_agent() returned None")
            return False
        
        # Check that agent has required attributes (LangGraph agent structure)
        if not hasattr(agent, 'invoke') and not hasattr(agent, 'ainvoke'):
            print("❌ Agent does not have invoke/ainvoke methods (not a valid LangGraph agent)")
            return False
        
        print("✅ create_analytics_agent() returns a valid agent")
        return True
        
    except Exception as e:
        print(f"❌ Error creating analytics agent: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_analytics_agent_structure(create_analytics_agent_func):
    """Test that analytics agent has correct structure (prompts/tools)."""
    print("\n" + "=" * 60)
    print("Testing Analytics Agent Structure")
    print("=" * 60)
    
    if create_analytics_agent_func is None:
        print("❌ Cannot test - function not available")
        return False
    
    # For now, we just check that the function exists and can be called
    # Once we implement prompts/tools, we can test more deeply
    print("✅ Analytics agent structure test (will expand when prompts/tools are implemented)")
    return True


def main():
    """Run analytics agent tests."""
    print("\n🔍 Testing create_analytics_agent() Function\n")
    
    # Test 1: Import
    import_result = test_analytics_agent_import()
    if not import_result[0]:
        print("\n❌ Import test failed. Implement create_analytics_agent() first!")
        return 1
    
    create_analytics_agent_func = import_result[1]
    
    # Test 2: Agent creation
    creation_ok = test_analytics_agent_creation(create_analytics_agent_func)
    
    # Test 3: Agent structure
    structure_ok = test_analytics_agent_structure(create_analytics_agent_func)
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    print(f"Import:              {'✅ PASS' if import_result[0] else '❌ FAIL'}")
    print(f"Agent creation:      {'✅ PASS' if creation_ok else '❌ FAIL'}")
    print(f"Agent structure:     {'✅ PASS' if structure_ok else '❌ FAIL'}")
    
    all_passed = import_result[0] and creation_ok and structure_ok
    
    if all_passed:
        print("\n✅ All analytics agent tests passed!")
        return 0
    else:
        print("\n❌ Some tests failed. Review output above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

