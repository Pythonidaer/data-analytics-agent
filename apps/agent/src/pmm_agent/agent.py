"""
PMM Deep Agent Factory.

Creates configurable PMM agents with different capability modes.
"""

import json
import os
from pathlib import Path
from typing import Literal

from langchain_anthropic import ChatAnthropic
from langgraph.prebuilt import create_react_agent

from .prompts import (
    MAIN_SYSTEM_PROMPT,
    COMPETITIVE_ANALYST_PROMPT,
    MESSAGING_SPECIALIST_PROMPT,
    LAUNCH_COORDINATOR_PROMPT,
)
from .tools import (
    INTAKE_TOOLS,
    RESEARCH_TOOLS,
    PLANNING_TOOLS,
    RISK_TOOLS,
    ALL_TOOLS,
    HUMAN_APPROVAL_TOOLS,
)


AgentMode = Literal["full", "intake", "research", "planning", "risk"]


def _load_domain_config(domain: str) -> dict:
    """
    Load domain configuration from JSON file.
    
    Args:
        domain: Domain name (e.g., "data_analytics", "pmm")
    
    Returns:
        Domain configuration dictionary
    
    Raises:
        FileNotFoundError: If domain config file doesn't exist
        json.JSONDecodeError: If config file is invalid JSON
    """
    # Path from agent.py: src/pmm_agent/ -> src/ -> apps/agent/ -> apps/ -> project root -> config/domains/
    # __file__ is at: apps/agent/src/pmm_agent/agent.py
    # Go up 4 levels: apps/agent/ -> apps/ -> project root
    project_root = Path(__file__).parent.parent.parent.parent.parent  # project root (contains apps/ and config/)
    config_path = project_root / "config" / "domains" / f"{domain}.json"
    
    if not config_path.exists():
        raise FileNotFoundError(f"Domain config not found: {config_path}")
    
    with open(config_path, 'r') as f:
        return json.load(f)


def create_pmm_agent(
    mode: AgentMode = "full",
    model_name: str = "claude-sonnet-4-20250514",
    with_subagents: bool = True,
):
    """
    Create a PMM agent with the specified capabilities.

    Args:
        mode: Operating mode determining available tools
            - "full": All tools available
            - "intake": Product analysis and requirements only
            - "research": Competitive intelligence and market research
            - "planning": Positioning, messaging, and launch planning
            - "risk": Risk assessment and validation
        model_name: Claude model to use
        with_subagents: Whether to include specialist subagents

    Returns:
        Configured LangGraph agent
    """
    # Select tools based on mode
    tools = []
    if mode == "full":
        tools = ALL_TOOLS
    elif mode == "intake":
        tools = INTAKE_TOOLS
    elif mode == "research":
        tools = RESEARCH_TOOLS + INTAKE_TOOLS  # Research needs intake context
    elif mode == "planning":
        tools = PLANNING_TOOLS + INTAKE_TOOLS
    elif mode == "risk":
        tools = RISK_TOOLS + RESEARCH_TOOLS

    # Initialize model with system prompt
    llm = ChatAnthropic(
        model_name=model_name,
        max_tokens=8192,
        system=MAIN_SYSTEM_PROMPT,
    )

    # Create base agent
    agent = create_react_agent(
        model=llm,
        tools=tools,
    )

    return agent


def create_competitive_analyst(model_name: str = None):
    """Create a specialist agent for competitive intelligence."""
    import os
    if model_name is None:
        model_name = os.getenv("MODEL", "claude-sonnet-4-20250514")
    llm = ChatAnthropic(
        model_name=model_name,
        max_tokens=4096,
        system=COMPETITIVE_ANALYST_PROMPT,
    )
    return create_react_agent(
        model=llm,
        tools=RESEARCH_TOOLS,
    )


def create_messaging_specialist(model_name: str = None):
    """Create a specialist agent for messaging work."""
    import os
    if model_name is None:
        model_name = os.getenv("MODEL", "claude-sonnet-4-20250514")
    llm = ChatAnthropic(
        model_name=model_name,
        max_tokens=4096,
        system=MESSAGING_SPECIALIST_PROMPT,
    )
    return create_react_agent(
        model=llm,
        tools=PLANNING_TOOLS,
    )


def create_launch_coordinator(model_name: str = None):
    """Create a specialist agent for launch planning."""
    import os
    if model_name is None:
        model_name = os.getenv("MODEL", "claude-sonnet-4-20250514")
    llm = ChatAnthropic(
        model_name=model_name,
        max_tokens=4096,
        system=LAUNCH_COORDINATOR_PROMPT,
    )
    return create_react_agent(
        model=llm,
        tools=PLANNING_TOOLS + RISK_TOOLS,
    )


def create_analytics_agent(
    mode: AgentMode = "full",
    model_name: str = "claude-sonnet-4-20250514",
):
    """
    Create a Data Analytics agent with the specified capabilities.
    
    Args:
        mode: Operating mode determining available tools
            - "full": All tools available
            - "intake": Analytics intake and KPI clarification only
            - "research": Benchmark research and context gathering
            - "planning": Metrics dictionary, tracking plans, SQL templates
            - "risk": Data quality checks and risk assessment
        model_name: Claude model to use
    
    Returns:
        Configured LangGraph agent for analytics domain
    
    Raises:
        FileNotFoundError: If analytics domain config not found
        ImportError: If analytics prompts/tools not yet implemented
    """
    # Load analytics domain config
    config = _load_domain_config("data_analytics")
    
    # Import analytics prompts and tools
    # TODO: These will be created in next steps
    try:
        from .domains.data_analytics.prompts import MAIN_SYSTEM_PROMPT as ANALYTICS_SYSTEM_PROMPT
        from .domains.data_analytics.tools import (
            INTAKE_TOOLS as ANALYTICS_INTAKE_TOOLS,
            RESEARCH_TOOLS as ANALYTICS_RESEARCH_TOOLS,
            PLANNING_TOOLS as ANALYTICS_PLANNING_TOOLS,
            RISK_TOOLS as ANALYTICS_RISK_TOOLS,
            ALL_TOOLS as ANALYTICS_ALL_TOOLS,
        )
    except ImportError as e:
        raise ImportError(
            f"Analytics domain prompts/tools not yet implemented: {e}. "
            "Create domains/data_analytics/prompts.py and domains/data_analytics/tools/ first."
        )
    
    # Select tools based on mode
    tools = []
    if mode == "full":
        tools = ANALYTICS_ALL_TOOLS
    elif mode == "intake":
        tools = ANALYTICS_INTAKE_TOOLS
    elif mode == "research":
        tools = ANALYTICS_RESEARCH_TOOLS + ANALYTICS_INTAKE_TOOLS
    elif mode == "planning":
        tools = ANALYTICS_PLANNING_TOOLS + ANALYTICS_INTAKE_TOOLS
    elif mode == "risk":
        tools = ANALYTICS_RISK_TOOLS + ANALYTICS_RESEARCH_TOOLS
    
    # Initialize model with analytics system prompt
    llm = ChatAnthropic(
        model_name=model_name,
        max_tokens=8192,
        system=ANALYTICS_SYSTEM_PROMPT,
    )
    
    # Create base agent
    agent = create_react_agent(
        model=llm,
        tools=tools,
    )
    
    return agent
